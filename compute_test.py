import compute

def test_n_of_vertices_of_adjacency_list():
    assert compute.n_of_vertices_of_adjacency_list(
        {
            0: [1, 2],
            1: [0, 3],
            2: [0, 3],
            3: [1, 2]
        }
    ) == 4
    
def test_n_of_edges_of_adjacency_list():
    assert compute.n_of_edges_of_adjacency_list(
        {
            0: [1, 2],
            1: [0, 3],
            2: [0, 3],
            3: [1, 2]
        }
    ) == 4
    
def test_n_of_vertices_of_adjacency_matrix():
    assert compute.n_of_vertices_of_adjacency_matrix(
        [
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 0]
        ]
    ) == 4
    
def test_n_of_edges_of_adjacency_matrix():
    assert compute.n_of_edges_of_adjacency_matrix(
        [   #0  1  2  3
            [0, 1, 1, 0],   #0
            [1, 0, 1, 1],   #1
            [1, 1, 0, 1],   #2
            [0, 1, 1, 0]    #3
        ]
    ) == 5
    
def test_n_of_vertices_of_incidence_matrix():
    assert compute.n_of_vertices_of_incidence_matrix(
        [
            [0, 1],
            [1, 0],
            [1, 1]
        ]
    ) == 3
    
def test_n_of_edges_of_incidence_matrix():
    assert compute.n_of_edges_of_incidence_matrix(
        [
            [0, 1],
            [1, 0],
            [1, 1]
        ]
    ) == 2
    assert compute.n_of_edges_of_incidence_matrix(
        [
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
            [0, 1, 0]
        ]
    ) == 3
    
def test_adjacent_vertices_of_adjacency_list():
    assert compute.adjacent_vertices_of_adjacency_list(
        {
            0: [1, 2],
            1: [0, 3],
            2: [0, 3],
            3: [1, 2]
        },
        0
    ) == [1, 2]
    assert compute.adjacent_vertices_of_adjacency_list(
        {
            0: [1, 2],
            1: [0, 3],
            2: [0, 3],
            3: [1, 2]
        },
        1
    ) == [0, 3]
    assert compute.adjacent_vertices_of_adjacency_list(
        {
            0: [1, 2],
            1: [0, 3],
            2: [0, 3],
            3: [1, 2]
        },
        2
    ) == [0, 3]
    
def test_adjacent_vertices_of_adjacency_matrix():
    assert compute.adjacent_vertices_of_adjacency_matrix(
        [
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 0]
        ],
        0
    ) == [1, 2]
    assert compute.adjacent_vertices_of_adjacency_matrix(
        [
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 0]
        ],
        1
    ) == [0, 2, 3]
    assert compute.adjacent_vertices_of_adjacency_matrix(
        [
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 0]
        ],
        2
    ) == [0, 1, 3]
    
def test_adjacent_vertices_of_incidence_matrix():
    assert compute.adjacent_vertices_of_incidence_matrix(
        [
            [0, 1],
            [1, 0],
            [1, 1]
        ],
        0
    ) == [2]
    assert compute.adjacent_vertices_of_incidence_matrix(
        [
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
            [0, 1, 0]
        ],
        1
    ) == [2]
    assert compute.adjacent_vertices_of_incidence_matrix(
        [
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
            [0, 1, 0]
        ],
        2
    ) == [0, 1]
    
def test_has_edge_between_vertices_of_adjacency_list():
    assert compute.has_edge_between_vertices_of_adjacency_list(
        {
            0: [1, 2],
            1: [0, 3],
            2: [0, 3],
            3: [1, 2]
        },
        0,
        1
    ) == True
    assert compute.has_edge_between_vertices_of_adjacency_list(
        {
            0: [1, 2],
            1: [0, 3],
            2: [0, 3],
            3: [1, 2]
        },
        0,
        2
    ) == True
    assert compute.has_edge_between_vertices_of_adjacency_list(
        {
            0: [1, 2],
            1: [0, 3],
            2: [0, 3],
            3: [1, 2]
        },
        0,
        3
    ) == False
    
def test_has_edge_between_vertices_of_adjacency_matrix():
    assert compute.has_edge_between_vertices_of_adjacency_matrix(
        [
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 0]
        ],
        0,
        1
    ) == True
    assert compute.has_edge_between_vertices_of_adjacency_matrix(
        [
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 0]
        ],
        0,
        2
    ) == True
    assert compute.has_edge_between_vertices_of_adjacency_matrix(
        [
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 0]
        ],
        0,
        3
    ) == False
    
def test_has_edge_between_vertices_of_incidence_matrix():
    assert compute.has_edge_between_vertices_of_incidence_matrix(
        [
            [0, 1],
            [1, 0],
            [1, 1]
        ],
        0,
        2
    ) == True
    assert compute.has_edge_between_vertices_of_incidence_matrix(
        [
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
            [0, 1, 0]
        ],
        1,
        2
    ) == True
    assert compute.has_edge_between_vertices_of_incidence_matrix(
        [
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
            [0, 1, 0]
        ],
        2,
        3
    ) == False
    
def test_degree_of_adjacency_list():
    assert compute.degree_of_adjacency_list(
        {
            0: [1, 2],
            1: [0, 3],
            2: [0, 3],
            3: [1, 2]
        },
        0
    ) == 2
    assert compute.degree_of_adjacency_list(
        {
            0: [1, 2],
            1: [0, 3],
            2: [0, 3],
            3: [1, 2]
        },
        1
    ) == 2
    assert compute.degree_of_adjacency_list(
        {
            0: [1, 2],
            1: [0, 3],
            2: [0, 3],
            3: [1, 2]
        },
        2
    ) == 2
    assert compute.degree_of_adjacency_list(
        {
            0: [1, 2],
            1: [0, 3],
            2: [0],
            3: [1]
        },
        3
    ) == 1
    
def test_degree_of_adjacency_matrix():
    assert compute.degree_of_adjacency_matrix(
        [
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 0]
        ],
        0
    ) == 2
    assert compute.degree_of_adjacency_matrix(
        [
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 0]
        ],
        1
    ) == 3
    assert compute.degree_of_adjacency_matrix(
        [
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 0]
        ],
        2
    ) == 3
    assert compute.degree_of_adjacency_matrix(
        [
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 0]
        ],
        3
    ) == 2
    
def test_degree_of_incidence_matrix():
    assert compute.degree_of_incidence_matrix(
        [
            [0, 1],
            [1, 0],
            [1, 1]
        ],
        0
    ) == 1
    assert compute.degree_of_incidence_matrix(
        [
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
            [0, 1, 0]
        ],
        1
    ) == 1
    assert compute.degree_of_incidence_matrix(
        [
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
            [0, 1, 0]
        ],
        2
    ) == 2
    assert compute.degree_of_incidence_matrix(
        [
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
            [0, 1, 0]
        ],
        3
    ) == 1
    
def test_degree_of_vertices_of_adjacency_list():
    assert compute.degree_of_adjacency_list(
        {
            0: [1, 2],
            1: [0, 3],
            2: [0],
            3: [1]
        }
    ) == [2, 2, 1, 1]
    
def test_degree_of_vertices_of_adjacency_matrix():
    assert compute.degree_of_adjacency_matrix(
        [
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 0]
        ]
    ) == [2, 3, 3, 2]
    
def test_degree_of_vertices_of_incidence_matrix():
    assert compute.degree_of_incidence_matrix(
        [
            [0, 1],
            [1, 0],
            [1, 1]
        ]
    ) == [1, 1, 2]
    
def test_simple_path_of_adjacency_list():
    assert compute.simple_path_of_adjacency_list(
        {
            0: [1, 2],
            1: [0, 3],
            2: [0],
            3: [1]
        },
        0,
        1
    ) == [0, 1]
    assert compute.simple_path_of_adjacency_list(
        {
            0: [1, 2],
            1: [0, 3],
            2: [0],
            3: [1]
        },
        0,
        2
    ) == [0, 2]
    assert compute.simple_path_of_adjacency_list(
        {
            0: [1, 2],
            1: [0, 3],
            2: [0],
            3: [1]
        },
        0,
        3
    ) == [0, 1, 3]
    assert compute.simple_path_of_adjacency_list(
        {
            0: [1, 2],
            1: [0, 3],
            2: [0],
            3: [1]
        },
        1,
        2
    ) == [1, 0, 2]
    
def test_simple_path_of_adjacency_matrix():
    assert compute.simple_path_of_adjacency_matrix(
        [
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 0]
        ],
        0,
        1
    ) == [0, 1]
    assert compute.simple_path_of_adjacency_matrix(
        [
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 0]
        ],
        0,
        2
    ) == [0, 2]
    assert compute.simple_path_of_adjacency_matrix(
        [
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 0]
        ],
        0,
        3
    ) == [0, 1, 3]
    
def test_simple_path_of_incidence_matrix():
    assert compute.simple_path_of_incidence_matrix(
        [
            [0, 1],
            [1, 0],
            [1, 1]
        ],
        0,
        1
    ) == [0, 2, 1]
    assert compute.simple_path_of_incidence_matrix(
        [
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
            [0, 1, 0]
        ],
        0,
        2
    ) == [0, 2]
    assert compute.simple_path_of_incidence_matrix(
        [
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
            [0, 1, 0]
        ],
        0,
        3
    ) == [0, 3]
    
def test_is_subgraph(): 
    assert compute.is_subgraph(
        [
            [0, 1],
            [1, 0],
            [1, 1]
        ],
        [
            [1],
            [1]
        ]) == True
    assert compute.is_subgraph(
        [
            [0, 1],
            [1, 0],
            [1, 1]
        ],
        [
            [0],
            [0]
        ]) == True
    assert compute.is_subgraph(
        [
            [0, 0, 1],
            [0, 0, 1],
            [1, 1, 0],
            [0, 1, 0],
            [1, 0, 0]
        ],
        [
            [1, 1],
            [1, 0],
            [0, 1]
        ]) == True