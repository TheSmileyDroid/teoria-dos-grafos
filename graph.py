import csv
import io
import random
from typing import Any, Iterator
import convert
import pydot


class Node:
    def __init__(self, name: str):
        self.name: str = name
        self.neighbors: list[Node] = []
        self.data = {
        }
    
    def add_neighbor(self, neighbor: 'Node'):
        self.neighbors.append(neighbor)
        
    def convert(self) -> pydot.Node:
        return pydot.Node(
            self.name,
            **self.data,
        )
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __hash__(self):
        return hash(self.name)
    
class Edge:
    def __init__(self, source: Node, target: Node, label: str, weight: float):
        self.source = source
        self.target = target
        self.data = {
            'label': label,
            'weight': weight,
        }
        
    def convert(self) -> pydot.Edge:
        return pydot.Edge(
            self.source.name,
            self.target.name,
            **self.data,
        )
    
    def __str__(self) -> str:
        return f'{self.source} -|{self.data["label"]}|-> {self.target} [weight={self.data["weight"]}]' if self.data["label"] else f'{self.source} -> {self.target} [weight={self.data["weight"]}]'
    
    def __repr__(self) -> str:
        return f'({self.source}, {self.target})'
    
    def __eq__(self, other: 'Edge') -> bool:
        return self.source == other.source and self.target == other.target
    
    def __hash__(self) -> int:
        return hash((self.source, self.target))
    

class Graph:
    def __init__(self):
        self.nodes: dict[str, Node] = {}
        self.edges: dict[tuple[str, str], Edge] = {}
        self.data_nodes: dict[str, Any] = {}
        self.data_edges: dict[str, Any] = {}
    
    def add_node(self, node: Node):
        self.nodes.update({node.name: node})
        
    def add_nodes(self, nodes: list[Node]):
        for node in nodes:
            self.add_node(node)
    
    def add_edges(self, edges: list[tuple[str, str]]):
        for source, target in edges:
            self.add_edge(source, target)
    
    def add_edge(self, source: str, target: str, label='', weight: float = 1):
        if source not in self.nodes:
            self.add_node(Node(source))
        if target not in self.nodes:
            self.add_node(Node(target))
        if source == target:
            return
        if self.nodes[source] in self.nodes[target].neighbors:
            return
        if self.nodes[target] in self.nodes[source].neighbors:
            return
    
        self.nodes[source].add_neighbor(self.nodes[target])
        self.nodes[target].add_neighbor(self.nodes[source])
    
        self.edges.update({(source, target): Edge(self.nodes[source], self.nodes[target], label, weight)})
    
    def get_edge(self, source: str, target: str):
        if (source, target) in self.edges:
            return self.edges[(source, target)]
        return None
    
    def get_node(self, name: str):
        if name in self.nodes:
            return self.nodes[name]
        return None
    
    def remove_node(self, name: str):
        if name in self.nodes:
            for node in self.nodes[name].neighbors:
                if self.edges.get((node.name, name)) is not None:
                    self.edges.pop((node.name, name))
                if self.edges.get((name, node.name)) is not None:
                    self.edges.pop((name, node.name))
                node.neighbors.remove(self.nodes[name])
            del self.nodes[name]
    
    def remove_edge(self, source: str, target: str):
        if (source, target) in self.edges:
            del self.edges[(source, target)]
            self.nodes[source].neighbors.remove(self.nodes[target])
            self.nodes[target].neighbors.remove(self.nodes[source])
        if (target, source) in self.edges:
            del self.edges[(target, source)]
            self.nodes[source].neighbors.remove(self.nodes[target])
            self.nodes[target].neighbors.remove(self.nodes[source])
    
    def __repr__(self) -> str:
        return str(self.nodes)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Graph):
            return NotImplemented
        return self.nodes == other.nodes
    
    def __hash__(self) -> int:
        return hash(self.nodes)
    
    def __iter__(self) -> Iterator[Node]:
        return iter(self.nodes.values())
    
    def __len__(self) -> int:
        return len(self.nodes)
    
    def __contains__(self, node: Node) -> bool:
        return node in self.nodes
    
    def random_node(self) -> Node:
        return self.nodes[random.choice(list(self.nodes.keys()))]
    
    def random_walk(self, start: str, length: int) -> list[str]:
        path = [start]
        current = self.nodes[start]
        for _ in range(length):
            next_node = None
            for i in range(len(current.neighbors)):
                next_node = current.neighbors[i]
                if next_node.name not in path:
                    break
            if next_node is None or next_node.name in path:
                break
            path.append(next_node.name)
            current = next_node
        return path
    
    def set_color_to_node(self, node: str, color):
        if color == None:
            if self.nodes[node].data.get('color') is not None:
                del self.nodes[node].data['color']
        else:
            self.nodes[node].data['color'] = color
    
    def set_color_to_edge(self, source: str, target: str, color):
        if color == None:
            if (source, target) in self.edges:
                if self.edges[(source, target)].data.get('color') is not None:
                    del self.edges[(source, target)].data['color']
            if (target, source) in self.edges:
                if self.edges[(target, source)].data.get('color') is not None:
                    del self.edges[(target, source)].data['color']
        else:
            if (source, target) in self.edges:
                self.edges[(source, target)].data['color'] = color
            if (target, source) in self.edges:
                self.edges[(target, source)].data['color'] = color
    
    def set_color_to_path(self, path: list[str], color):
        for node in path:
            self.set_color_to_node(node, color)
        for i in range(len(path) - 1):
            source = path[i]
            target = path[i + 1]
            self.set_color_to_edge(source, target, color)
    
    def set_color_to_nodes(self, nodes: list[str], color):
        for node in nodes:
            self.set_color_to_node(node, color)
    
    def set_attr_to_node(self, node: str, attr: str, value: Any):
        if value == None:
            if self.nodes[node].data.get(attr) is not None:
                del self.nodes[node].data[attr]
        else:
            self.nodes[node].data[attr] = value
        
    def set_attr_to_edge(self, source: str, target: str, attr: str, value: Any):
        if value == None:
            if (source, target) in self.edges:
                if self.edges[(source, target)].data.get(attr) is not None:
                    del self.edges[(source, target)].data[attr]
            if (target, source) in self.edges:
                if self.edges[(target, source)].data.get(attr) is not None:
                    del self.edges[(target, source)].data[attr]
        else:
            if (source, target) in self.edges:
                self.edges[(source, target)].data[attr] = value
            if (target, source) in self.edges:
                self.edges[(target, source)].data[attr] = value
            
    def set_attr_to_path(self, path: list[str], attr: str, value: Any):
        for node in path:
            self.set_attr_to_node(node, attr, value)
        for i in range(len(path) - 1):
            source = path[i]
            target = path[i + 1]
            self.set_attr_to_edge(source, target, attr, value)
    
    def set_attr_to_nodes(self, nodes: list[str], attr: str, value: Any):
        for node in nodes:
            self.set_attr_to_node(node, attr, value)
    
    def set_attr_to_edges(self, edges: list[tuple[str, str]], attr: str, value: Any):
        for edge in edges:
            self.set_attr_to_edge(edge[0], edge[1], attr, value)
    
    def set_color_to_edges(self, edges: list[tuple[str, str]], color):
        for edge in edges:
            self.set_color_to_edge(edge[0], edge[1], color)
    
    def set_color_to_all_nodes(self, color: str):
        self.data_nodes = {'color': color}
            
    def set_color_to_all_edges(self, color: str):
        self.data_edges = {'color': color}
        
    def get_edges_from_node(self, node: str) -> list[Edge]:
        edges = []
        for edge in self.edges.values():
            if edge.source.name == node or edge.target.name == node:
                edges.append(edge)
        return edges

    def convert_to_pydot(self, *args, **kwargs):
        print('Convertendo para Pydot...')
        g = convert.new_graph(*args, **kwargs)
        g.set_node_defaults(**self.data_nodes)
        g.set_edge_defaults(**self.data_edges)
        for node in self.nodes.keys():
            g.add_node(self.nodes[node].convert())
        for edge in self.edges.values():
            g.add_edge(edge.convert())
        
        return g
    
    def write_dot(self, filename, *args, **kwargs):
        g = self.convert_to_pydot(*args, **kwargs)
        g.write(filename, format='dot')
        
    def write_png(self, filename, *args, **kwargs):
        g = self.convert_to_pydot(*args, **kwargs)
        print('Convertendo para PNG...')
        err = g.write(filename, format='png')
        if err != True:
            print('Erro ao converter para PNG!')
            print(err)
        else:
            print('PNG gerado com sucesso!')
        
    def write_svg(self, filename, *args, **kwargs):
        g = self.convert_to_pydot(*args, **kwargs)
        print('Convertendo para SVG...')
        g.write(filename, format='svg')
    
    def convert_to_adjacency_matrix(self):
        matrix = []
        
        for node in self.nodes.values():
            row = []
            
            for neighbor in self.nodes.values():
                if neighbor in node.neighbors:
                    row.append(1)
                else:
                    row.append(0)
            
            matrix.append(row)
        
        return matrix
    
    def convert_from_adjacency_matrix(self, matrix: list[list[int]]):
        self.nodes = {}
        self.edges = {}
        
        for i in range(len(matrix)):
            self.add_node(Node(str(i)))
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    self.add_edge(str(i), str(j))
    
        return self
    
    def convert_to_incidence_matrix(self):
        matrix = []
        
        for node in self.nodes.values():
            row = []
            
            for edge in self.edges:
                if edge[0] == node.name or edge[1] == node.name:
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        
        return matrix
    
    def convert_from_incidence_matrix(self, matrix: list[list[int]]):
        self.nodes = {}
        self.edges = {}
        
        for i in range(len(matrix)):
            self.add_node(Node(str(i)))
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    for k in range(len(matrix)):
                        if matrix[k][j] == 1 and k != i:
                            self.add_edge(str(i), str(k))
    
        return self
    
    def convert_to_adjacency_list(self) -> dict[str, list[str]]:
        adjacency_list = {}
        
        for node in self.nodes.values():
            adjacency_list[node.name] = []
            
            for neighbor in node.neighbors:
                adjacency_list[node.name].append(neighbor.name)
        
        return adjacency_list
    
    def convert_from_adjacency_list(self, adjacency_list: dict[str, list[str]]):
        self.nodes = {}
        self.edges = {}
        
        for node in adjacency_list.keys():
            self.add_node(Node(node))
        
        for node in adjacency_list.keys():
            for neighbor in adjacency_list[node]:
                self.add_edge(node, neighbor)
        
        return self
    
    def save(self, filename):
        with open(f'{filename}_edges.csv', 'w') as f:
            f.write('source,target,label,weight\n')
            for edge in self.edges.values():
                f.write(f'{edge.source.name},{edge.target.name},{edge.data["label"]},{edge.data["weight"]}\n')
        with open(f'{filename}_nodes.csv', 'w') as f:
            f.write('name\n')
            for node in self.nodes.values():
                f.write(f'{node.name}\n')
    
    @staticmethod
    def load(filename) -> 'Graph':
        g = Graph()
        
        with open(f'{filename}_edges.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                g.add_edge(row['source'], row['target'], row['label'], float(row['weight']))
        with open(f'{filename}_nodes.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['name'] not in g.nodes:
                    g.add_node(Node(row['name']))
        
        return g
    
    def shortest_path(self, source: str, target: str):
        if source not in self.nodes or target not in self.nodes:
            return None
        
        visited = []
        queue = [[source]]
        
        i = 0
        while queue:
            i += 1
            path = queue.pop(0)
            node = path[-1]
            
            if node not in visited:
                neighbors = self.nodes[node].neighbors
                
                for neighbor in neighbors:
                    if neighbor.name in visited:
                        continue
                    new_path = list(path)
                    new_path.append(neighbor.name)
                    queue.append(new_path)
                    
                    if neighbor.name == target:
                        return new_path
                
                visited.append(node)
        
        return None
    
    def shortest_path_export(self, source: str, target: str):
        if source not in self.nodes or target not in self.nodes:
            print('Source ou target não existem')
            return None
        
        visited = []
        queue = [[source]]
        
        self.set_attr_to_node(source, 'fillcolor', '#c3e88d')
        self.set_attr_to_node(target, 'fillcolor', '#c3e88d')
        
        self.write_png('.tests/graph_00.png', splines='false')
        
        self.set_color_to_all_edges('#08306b30')
        self.set_color_to_all_nodes('#8dd3c730')
        
        i = 0
        print('---------------------')
        print(f'Iteração: {i}')
        print(f'Visited: {visited}')
        print(f'Queue: {queue}')
        while queue:
            i += 1
            path = queue.pop(0)
            node = path[-1]
            
            print('---------------------')
            print(f'Node: {node}')
            print(f'Iteração: {i}')
            print(f'Path: {path}')
            print(f'Visited: {visited}')
            print(f'Queue: {queue}')
            
            self.set_color_to_path(path, '#f03b20')
            self.set_attr_to_node(node, 'fillcolor', '#e3cc16')
            self.set_color_to_nodes(visited, '#1a9641')
            
            self.write_png(f'.tests/graph_{i:02}.png', splines='false')
            
            if node not in visited:
                neighbors = self.nodes[node].neighbors
        
                for neighbor in neighbors:
                    if neighbor.name in visited:
                        continue
                    new_path = list(path)
                    new_path.append(neighbor.name)
                    queue.append(new_path)
                    
                    if neighbor.name == target:
                        print('---------------------')
                        print(f'Iteração: {i}')
                        print(f'Visited: {visited}')
                        print(f'Queue: {queue}')
                        self.set_color_to_path(new_path, '#f03b20')
                        self.set_color_to_node(node, '#d7191c')
                        self.write_png(f'.tests/graph_{i:02}.png', splines='false')
                        self.set_color_to_path(new_path, None)
                        self.set_color_to_node(node, None)
                        
                        return new_path
                
                visited.append(node)
                
            self.set_color_to_path(path, None)
            self.set_color_to_node(node, None)
            self.set_attr_to_node(node, 'fillcolor', None)
        
        return None
    
    def is_connected(self) -> bool:
        visited = []
        queue = [list(self.nodes.keys())[0]]
        
        while queue:
            node = queue.pop(0)
            
            if node not in visited:
                neighbors = self.nodes[node].neighbors
                
                for neighbor in neighbors:
                    if neighbor.name in visited:
                        continue
                    queue.append(neighbor.name)
                
                visited.append(node)
        
        return len(visited) == len(self.nodes)
    
    def is_subgraph(self, subgraph: 'Graph') -> bool:
        for node in subgraph.nodes.values():
            if node.name not in self.nodes:
                return False
            
            for neighbor in node.neighbors:
                if neighbor.name not in self.nodes:
                    return False
        
        return True

    
    def random_subgraph(self, n: int):
        if n > len(self.nodes):
            return None
        
        nodes = []
        node = self.random_node()
        nodes.append(node.name)
        for i in range(n):
            for neighbor in self.nodes[node.name].neighbors:
                if neighbor.name not in nodes:
                    node = neighbor
                    nodes.append(node.name)
                    break
        
        return nodes
    
    def random_cycle(self, source: str):
        if source not in self.nodes or len(self.nodes[source].neighbors) < 2:
            return None
        
        last_visited = None
        queue = [[source]]
        
        while queue:
            path = queue.pop(0)
            node = path[-1]
            
            if node is not last_visited:
                neighbors = self.nodes[node].neighbors
        
                for neighbor in neighbors:
                    if neighbor.name in path and neighbor.name != source:
                        continue
                    new_path = list(path)
                    new_path.append(neighbor.name)
                    queue.append(new_path)
                    
                    if neighbor.name == source and len(new_path) > 3:
                        return new_path
                
                last_visited = node
                
            self.set_color_to_path(path, None)
            self.set_color_to_node(node, None)
            self.set_attr_to_node(node, 'fillcolor', None)
        
        return None

        
    def random_cycle_export(self, source: str):
        if source not in self.nodes or len(self.nodes[source].neighbors) < 2:
            return None
        
        last_visited = None
        queue = [[source]]
        
        self.set_attr_to_node(source, 'fillcolor', '#c3e88d')
        
        self.write_png(f'.tests/graph_00.png', splines='false')
        
        self.set_color_to_all_edges('#08306b30')
        self.set_color_to_all_nodes('#8dd3c730')
        
        i = 0
        print('---------------------')
        print(f'Iteração: {i}')
        print(f'Last visited: {last_visited}')
        print(f'Queue: {queue}')
        while queue:
            i += 1
            path = queue.pop(0)
            node = path[-1]
            
            print('---------------------')
            print(f'Node: {node}')
            print(f'Iteração: {i}')
            print(f'Path: {path}')
            print(f'Last visited: {last_visited}')
            print(f'Queue: {queue}')
            
            self.set_color_to_path(path, '#f03b20')
            self.set_attr_to_node(node, 'fillcolor', '#e3cc16')
            if last_visited:
                self.set_color_to_node(last_visited, '#1a9641')
            
            self.write_png(f'.tests/graph_{i:02}.png', splines='false')
            
            if node is not last_visited:
                neighbors = self.nodes[node].neighbors
        
                for neighbor in neighbors:
                    if neighbor.name in path and neighbor.name != source:
                        continue
                    new_path = list(path)
                    new_path.append(neighbor.name)
                    queue.append(new_path)
                    
                    if neighbor.name == source and len(new_path) > 3:
                        print('---------------------')
                        print(f'Iteração: {i}')
                        print(f'Last visited: {last_visited}')
                        print(f'Queue: {queue}')
                        self.set_color_to_path(new_path, '#f03b20')
                        self.set_color_to_node(node, '#d7191c')
                        self.write_png(f'.tests/graph_{i}.png', splines='false')
                        self.set_color_to_path(new_path, None)
                        self.set_color_to_node(node, None)
                        
                        return new_path
                
                last_visited = node
                
            self.set_color_to_path(path, None)
            self.set_color_to_node(node, None)
            self.set_attr_to_node(node, 'fillcolor', None)
        
        return None
    
    def bfs(self, source: str):
        if source not in self.nodes:
            return None
        
        queue = [[source]]
        path = []
        
        while queue:
            path = queue.pop(0)
            node = path[-1]
            
            if node not in path[:-1]:
                neighbors = self.nodes[node].neighbors
        
                for neighbor in neighbors:
                    if neighbor.name in path:
                        continue
                    new_path = list(path)
                    new_path.append(neighbor.name)
                    queue.append(new_path)
        return path
    
    def lenght_search(self, source: str):
        if source not in self.nodes:
            return None
        
        queue = [[source]]
        path = []
        
        while queue:
            path = queue.pop(0)
            node = path[-1]
            
            if node not in path[:-1]:
                neighbors = self.nodes[node].neighbors
        
                for neighbor in neighbors:
                    if neighbor.name in path:
                        continue
                    new_path = list(path)
                    new_path.append(neighbor.name)
                    queue.append(new_path)
        return len(path)

    def longest_path(self):
        longest_path = []
        
        for node in self.nodes.values():
            path = self.bfs(node.name)
            
            if path and len(path) > len(longest_path):
                longest_path = path
        
        return longest_path
    
    def longest_path_export(self):
        longest_path = []
        
        self.write_png(f'.tests/graph_00.png', splines='false')
        
        self.set_color_to_all_edges('#08306b30')
        self.set_color_to_all_nodes('#8dd3c730')
        
        i = 0
        
        for node in self.nodes.values():
            i+=1
            path = self.bfs(node.name)
            
            if path:
                self.set_color_to_path(path, '#f03b20')
                self.write_png(f'.tests/graph_{i:02}.png', splines='false')
                self.set_color_to_path(path, None)
                
            if path and len(path) > len(longest_path):
                longest_path = path
        
        return longest_path
    
    def save_file_g4v(self, file):
        file.write(self.to_g4v())
    
    def to_g4v(self):
        return f'{self.to_g4v_nodes()}\n{self.to_g4v_edges()}'
    
    def to_g4v_nodes(self):
        nodes = []
        for node in self.nodes.values():
            data = f'Node:{node.name}['
            for key, value in node.data.items():
                data += f'{key}="{value}" '
            data = data.removesuffix(' ')
            data += '];'
            nodes.append(data)
        return '\n'.join(nodes)
    
    def to_g4v_edges(self):
        edges = []
        for edge in self.edges.values():
            data = f'Edge:{edge.source.name}->{edge.target.name}['
            for key, value in edge.data.items():
                data += f'{key}="{value}" '
            data = data.removesuffix(' ')
            data += '];'
            edges.append(data)
        return '\n'.join(edges)
    
    def __str__(self):
        return self.to_g4v()
    
    def from_file_g4v(self, file):
        lines = file.readlines()
        self.from_g4v(lines)
            
    def from_g4v(self, lines: list):
        nodes = []
        edges = []
        
        for line in lines:
            if line.startswith('Node:'):
                nodes.append(line[5:])
            elif line.startswith('Edge:'):
                edges.append(line[5:])
        
        self.from_g4v_nodes(nodes)
        self.from_g4v_edges(edges)
    
    def from_g4v_nodes(self, lines: list[str]):
        for line in lines:
            data = line.split('[')
            name = data[0]
            data = data[1][:-2].split(' ')
            node = Node(name)
            for d in data:
                if len(d.split('=')) == 1:
                    break
                key, value = d.split('=')
                value = value.strip('"')
                node.data[key] = value
            self.add_node(node)
    
    def from_g4v_edges(self, lines: list[str]):
        for line in lines:
            data = line.split('[')
            source, target = data[0].split('->')
            data = data[1][:-2].split(' ')
            edge = self.add_edge(source, target)
            for d in data:
                if len(d.split('=')) == 1:
                    break
                key, value = d.split('=')
                value = value.strip('"')
                self.edges[(source, target)].data[key] = value


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