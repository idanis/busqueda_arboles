# This class represent a graph
class Graph:
    # Initialize the class
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    # Create an undirected graph by adding symmetric edges
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist

    # Add a link from A and B of given distance, and also add the inverse link if the graph is undirected
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance

    # Get neighbors or a neighbor
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    # Return a list of nodes in the graph
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)


# This class represent a node
class Node:
    # Initialize the class
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = 0  # Total cost

    # Compare nodes
    def __eq__(self, other):
        return self.name == other.name

    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f

    # Print node
    def __repr__(self):
        return '({0},{1})'.format(self.name, self.f)


# A* search
def A_Star(graph, heuristics, start, end):
    # Create lists for open nodes and closed nodes
    open = []
    close = []

    # Create a start node and an goal node
    start_node = Node(start, None)
    start_node.h = heuristics[start]
    start_node.f = start_node.g + start_node.h
    end_node = Node(end, None)

    # Add the start node
    open.append(start_node)

    # Loop until the open list is empty
    while open:
        # Sort the open list to get the node with the lowest cost first
        open.sort()

        # Get the node with the lowest cost
        current_node = open.pop(0)
        # Add the current node to the closed list
        close.append(current_node)

        # Check if we have reached the goal, return the path (From Current Node to Start Node By Node.parent)
        if current_node == end_node:
            # Return reversed path (Hint: Return Llist of path in this Fashion for Reverse return path[::-1])
            print("Cost:", current_node.f)
            path = []
            while current_node != start_node:
                path.append(current_node)
                current_node = current_node.parent
            path.append(start_node)
            return path[::-1]

        # Get neighbours
        neighbors = graph.get(current_node.name)

        # Loop neighbors
        for key, value in neighbors.items():
            # Create a neighbor node
            neighbor = Node(key, current_node)

            # Check if the neighbor is in the closed list
            if neighbor in close:
                continue
            # Calculate cost to goal
            neighbor.g = value + current_node.g
            neighbor.h = heuristics[neighbor.name]
            neighbor.f = neighbor.g + neighbor.h

            # Check if neighbor is in open list and if it has a lower f value
            if In_Open(open, neighbor):
                # Everything is green, add neighbor to open list
                open.append(neighbor)

    # Return None, no path is found
    return None


# Check if a neighbor should be added to open list
def In_Open(open, neighbor):
    for node in open:
        if neighbor == node and neighbor.f >= node.f:
            return False
    return True


# The main entry point for this module
def main():
    # Create a graph
    graph = Graph()

    # Create graph connections (Actual distance)
    graph.connect('Arad', 'Zerind', 75)
    graph.connect('Arad', 'Timisoara', 118)
    graph.connect('Arad', 'Sibiu', 140)
    graph.connect('Zerind', 'Oradea', 71)
    graph.connect('Lugoj', 'Mehadia', 70)
    graph.connect('Mehadia', 'Dobreta', 75)
    graph.connect('Oradea', 'Sibiu', 151)
    graph.connect('Timisoara', 'Lugoj', 111)
    graph.connect('Craiova', 'Rimnicu Vilcea', 146)
    graph.connect('Rimnicu Vilcea', 'Pitesti', 97)
    graph.connect('Dobreta', 'Craiova', 120)
    graph.connect('Craiova', 'Pitesti', 138)
    graph.connect('Sibiu', 'Rimnicu Vilcea', 80)
    graph.connect('Sibiu', 'Fagaras', 99)
    graph.connect('Fagaras', 'Bucharest', 211)
    graph.connect('Pitesti', 'Bucharest', 101)
    graph.connect('Giurgiu', 'Bucharest', 90)

    # Make graph undirected, create symmetric connections
    graph.make_undirected()

    # Create heuristics (straight-line distance, air-travel distance) for Destination Bucharest
    heuristics = {'Arad': 366, 'Bucharest': 0, 'Zerind': 374, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161,
                  'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241,
                  'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329,
                  'Urziceni': 80, 'Vaslui': 199}

    # Print Graph Nodes
    print(graph.nodes())
    print('\n')

    # Run search algorithm
    path = A_Star(graph, heuristics, 'Arad', 'Bucharest')
    print('Solución:', path)


# Tell python to run main method
if __name__ == "__main__":
    main()
