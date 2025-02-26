# Taken from: https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
# a sample graph
from collections import namedtuple 

Coord = namedtuple('Coord', ['x', 'y'])

Nfilas = 5
Ncolumnas = 5

laberinto = [[0,0,0,1,1],
             [0,1,0,0,1],
             [0,1,0,1,1],
             [1,0,0,0,0],
             [1,0,1,1,0]
             ] 

def devuelve_vecinos(pos):
    vecinos = []
    if pos.x > 0:
        vecinos.append(Coord(pos.x-1, pos.y))
    if pos.x < Nfilas-1:
        vecinos.append(Coord(pos.x+1, pos.y))
    if pos.y > 0:
        vecinos.append(Coord(pos.x, pos.y-1))
    if pos.y < Ncolumnas-1:
        vecinos.append(Coord(pos.x, pos.y+1))
    
    true_vecinos = []
    for p in vecinos : 
        if laberinto[p.x][p.y] == 0 :
           true_vecinos.append(p)

    return true_vecinos

def bfs_paths(pos_ini, goal):
    queue = [(pos_ini, [pos_ini])]
    while queue:
        (vertex, path) = queue.pop(0)
          
        l = list(set(devuelve_vecinos(vertex)) - set(path))
        for next in l:
            if next.x == goal.x and next.y == goal.y:
                print(path + [next])
                return 1
            else:
                queue.append((next, path + [next]))
        
    return 0

pos_ini = Coord(x=0, y=0)
pos_meta = Coord(x=4, y=4)
print("BFS solución: ")
if not (bfs_paths(pos_ini, pos_meta)):
   print('No encontró solución para el laberinto')
 
