# write tests for bfs
import pytest
from search import Graph 
import os
currentdir = os.getcwd() #GitHub/project2/ 



@pytest.fixture
def test_bfs_traversal_num_test():
    
    test_graph = Graph('data/num_test.adjlist')
    assert test_graph.bfs('2', None) == []
    assert test_graph.bfs('2', None) == ['2', '4', '5', '9', '8', '10', '11'], "Error: output should be empty"

def test_bfs_traversal():
    tiny_network = Graph(filename = os.path.join(currentdir,"data/tiny_network.adjlist"))
    print(tiny_network.bfs('', None))
    assert tiny_network.bfs('', None) == [] 
    assert tiny_network.bfs('', None) == []


def test_bfs_num_test():
    
    test_network = Graph("data/num_test.adjlist")
    assert test_network.bfs("2", "11") == ['2', '5', '5', '9', '9', '11']
    assert test_network.bfs("2", "11") == ['2', '5', '10', '11'], "Error: within bfs should return 2, 5, 9, 11"

    

def test_bfs():
    tiny_network = Graph(filename = os.path.join(currentdir,"data/tiny_network.adjlist"))

    assert tiny_network.bfs("Atul Butte","Marina Sirota") == ['Atul Butte', '30944313', '30944313', 'Marina Sirota']
    assert tiny_network.bfs("Atul Butte","Marina Sirota") == ['Atul Butte', '30944313', 'Marina Sirota'], "Error: within bfs should return Atul Butte, 30944313, Marina Sirota"







