from graph import Graph
import os
import shutil
from make_gif import make_gif
import oscar

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
g = oscar.graph_from_actors()
path = ['Kirby Howell-Baptiste', 'Emma Stone', 'Emma Thompson', 'Joel Fry', 'Paul Walter Hauser', 'Emily Beecham']
g.set_color_to_all_nodes('#000000')
g.set_color_to_path(path, '#ff0000')
g.write_png('.tests/animation.png', splines='false')
print(path) 
make_gif('.tests', 'animation.gif')