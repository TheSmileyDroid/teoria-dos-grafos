
# Adjacency list: 
#   - Each vertex is a key in the dictionary
#   - Each value is a list of adjacent vertices

# Adjacency matrix:
#   - Each row is a vertex
#   - Each column is an adjacent vertex

# Incidence matrix:
#   - Each row is an node
#   - Each column is an edge
import graph

def is_isomorphic(graph1, graph2):
    if len(graph1) != len(graph2):
        return False
    if len(graph1[0]) != len(graph2[0]):
        return False
    edges_g1: list[int] = list(map(sum, graph1))
    edges_g2: list[int] = list(map(sum, graph2))
    sorted_edges_g1 = sorted(edges_g1)
    sorted_edges_g2 = sorted(edges_g2)
    if sorted_edges_g1 == sorted_edges_g2:
        return True
    return False

def remove_node(graph, node) -> list[list[int]]:
    new_graph = []
    edges = []
    for i in range(len(graph[0])):
        if graph[node][i] == 1:
            edges.append(i)
    for i in range(len(graph)):
        if i == node:
            continue
        new_node = []
        for j in range(len(graph[i])):
            if j not in edges:
                new_node.append(graph[i][j])
            else:
                new_node.append(0)
        new_graph.append(new_node)
    return new_graph

def remove_edge(graph, edge) -> list[list[int]]:
    new_graph = []
    for i in range(len(graph)):
        new_node = []
        for j in range(len(graph[i])):
            if j == edge:
                continue
            new_node.append(graph[i][j])
        new_graph.append(new_node)
    return new_graph

def is_subgraph(graph, subgraph) -> bool:
    if is_isomorphic(graph, subgraph):
        return True
    if len(graph) < len(subgraph):
        return False
    if len(graph[0]) < len(subgraph[0]):
        return False
    for i in range(len(graph)):
        new_graph = remove_node(graph, i)
        if is_subgraph(new_graph, subgraph):
            return True
        for j in range(len(graph[i])):
            new_graph = remove_edge(graph, j)
            if is_subgraph(new_graph, subgraph):
                return True
    return False


def n_of_vertices_of_adjacency_list(adj_list: dict[list[str]]) -> int:
    return len(adj_list)

def n_of_edges_of_adjacency_list(adj_list: dict[list[str]]) -> int:
    return sum(len(adj_list[vertex]) for vertex in adj_list) // 2

def n_of_vertices_of_adjacency_matrix(adj_matrix: list[list[int]]) -> int:
    return len(adj_matrix)

def n_of_edges_of_adjacency_matrix(adj_matrix: list[list[int]]) -> int:
    return sum(sum(row) for row in adj_matrix) // 2

def n_of_vertices_of_incidence_matrix(inc_matrix: list[list[int]]) -> int:
    return len(inc_matrix)

def n_of_edges_of_incidence_matrix(inc_matrix: list[list[int]]) -> int:
    return len(inc_matrix[0])

def adjacent_vertices_of_adjacency_list(adj_list: dict[list[str]], vertex: str) -> list[str]:
    return adj_list[vertex]

def adjacent_vertices_of_adjacency_matrix(adj_matrix: list[list[int]], vertex: int) -> list[int]:
    return [i for i, row in enumerate(adj_matrix[vertex]) if row]

def adjacent_vertices_of_incidence_matrix(inc_matrix: list[list[int]], vertex: int) -> list[int]:
    adj_vertices = []
    for i in range(len(inc_matrix)):
        if inc_matrix[i][vertex] == 1:
            for j in range(len(inc_matrix[i])):
                if j != vertex and inc_matrix[i][j] == 1:
                    adj_vertices.append(j)
    return adj_vertices

def has_edge_between_vertices_of_adjacency_list(adj_list: dict[list[str]], vertex1: str, vertex2: str) -> bool:
    return vertex2 in adj_list[vertex1]

def has_edge_between_vertices_of_adjacency_matrix(adj_matrix: list[list[int]], vertex1: int, vertex2: int) -> bool:
    return adj_matrix[vertex1][vertex2]

def has_edge_between_vertices_of_incidence_matrix(inc_matrix: list[list[int]], vertex1: int, vertex2: int) -> bool:
    for edge in range(len(inc_matrix[vertex1])):
        if inc_matrix[vertex1][edge] == 1 and inc_matrix[vertex2][edge] == 1:
            return True
    return False

def degree_of_adjacency_list(adj_list: dict[list[str]], vertex: str = None) -> int:
    if vertex is None:
        return [len(adj_list[vertex]) for vertex in adj_list]
    return len(adj_list[vertex])

def degree_of_adjacency_matrix(adj_matrix: list[list[int]], vertex: int = None) -> int:
    if vertex is None:
        return [sum(row) for row in adj_matrix]
    return sum(row[vertex] for row in adj_matrix)

def degree_of_incidence_matrix(inc_matrix: list[list[int]], vertex: int = None) -> int:
    if vertex is None:
        return [sum(row) for row in inc_matrix]
    return sum(row for row in inc_matrix[vertex])

def simple_path_of_adjacency_list(adj_list: dict[list[str]], vertex1: str, vertex2: str) -> list[str]:
    visited = []
    queue = [[vertex1]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in visited:
            neighbors = adjacent_vertices_of_adjacency_list(adj_list, node)
            
            for neighbor in neighbors:
                if neighbor in  visited:
                    continue
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path) 
                
                if neighbor == vertex2:
                    return new_path
            
            visited.append(node)
    return []

def simple_path_of_adjacency_matrix(adj_matrix: list[list[int]], vertex1: int, vertex2: int) -> list[int]:
    visited = []
    queue = [[vertex1]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in visited:
            neighbors = adjacent_vertices_of_adjacency_matrix(adj_matrix, node)
            
            for neighbor in neighbors:
                if neighbor in  visited:
                    continue
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path) 
                
                if neighbor == vertex2:
                    return new_path
            
            visited.append(node)
    return []

def simple_path_of_incidence_matrix(inc_matrix: list[list[int]], vertex1: int, vertex2: int) -> list[int]:
    visited = []
    queue = [[vertex1]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in visited:
            neighbors = adjacent_vertices_of_incidence_matrix(inc_matrix, node)
            
            for neighbor in neighbors:
                if neighbor in  visited:
                    continue
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path) 
                
                if neighbor == vertex2:
                    return new_path
            
            visited.append(node)
    return []

def cycle_of_adjacency_list(adj_list: dict[list[str]], vertex: str = None) -> list[str]:
    last_visited = None
    queue = [[vertex]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node is not last_visited:
            neighbors = adjacent_vertices_of_adjacency_list(adj_list, node)
            
            for neighbor in neighbors:
                if neighbor in path and neighbor != path[0]:
                    continue
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path) 
                
                if neighbor == path[0] and len(new_path) > 3:
                    return new_path
            
            last_visited = node
    return []

def cycle_of_adjacency_matrix(adj_matrix: list[list[int]], vertex: int = None) -> list[int]:
    last_visited = None
    queue = [[vertex]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node is not last_visited:
            neighbors = adjacent_vertices_of_adjacency_matrix(adj_matrix, node)
            
            for neighbor in neighbors:
                if neighbor in path and neighbor != path[0]:
                    continue
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path) 
                
                if neighbor == path[0] and len(new_path) > 3:
                    return new_path
            
            last_visited = node
    return []

def cycle_of_incidence_matrix(inc_matrix: list[list[int]], vertex: int = None) -> list[int]:
    last_visited = None
    queue = [[vertex]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node is not last_visited:
            neighbors = adjacent_vertices_of_incidence_matrix(inc_matrix, node)
            
            for neighbor in neighbors:
                if neighbor in path and neighbor != path[0]:
                    continue
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path) 
                
                if neighbor == path[0] and len(new_path) > 3:
                    return new_path
            
            last_visited = node
    return []
