from graph import Graph
import os
import shutil
from make_gif import make_gif

def simple_graph() -> Graph:
    g = Graph()
    g.add_edges([
        ('A', 'B'),
        ('A', 'C'),
        ('A', 'D'),
        ('B', 'C'),
        ('B', 'D'),
        ('C', 'D'),
        ('C', 'E'),
        ('D', 'E'),
        ('D', 'F'),
        ('E', 'F'),
        ('F', 'H'),
        ('I', 'G'),
    ])
    
    return g

shutil.rmtree('.tests', ignore_errors=True)
os.mkdir('.tests')
g = simple_graph()
path = g.longest_path_export()
print(path)
make_gif('.tests', 'animation.gif')