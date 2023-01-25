import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """


    def __init__(self, filename) -> None:

        """
        Initialization of graph object 
        """

        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")
        #print(self.graph)

    def next_node(self, node, end=None):
        """
        Find the next node in the graph
        """
        if node == end:
            return print(end)
        else:
            return self.graph.neighbors(node)


    def bfs(self, start, end=None):
        """
        A recursive function that performs a breadth first traversal and pathfinding on graph G
        
        ArithmeticError:

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None
        """

        # ArithmeticError:
        if start not in self.graph.nodes():            # if start node is not in graph
            raise ValueError(f"Start node {start} not found in graph")
        
        elif end not in self.graph.nodes():            # if end node is not in graph
            raise ValueError(f"End node {end} not found in graph")

        elif start == end and self.graph.nodes():      # if start node is the same as end node
            raise ValueError(f"Start node {start} is the same as end node {end}")

        
        """
        Breath First Search - BFS Algorithm

        Obectives: 
            To find the shortest path between two nodes in a graph. 
            To traverse a graph in a breadth first manner.

        Algorithm:
            1. Start at the root node (start node)
            2. Explore all the neighbor nodes at the present depth
            3. Move on to the nodes at the next depth level (next neighbor)
            4. Repeat until the goal node is found or all nodes have been explored
            5. If the goal node is never found, return failure (no path exists)
        """
    
        queue = [start]                                    # initialize queue with start node
        visited = []                                       # initialize visited list
        path={}                                            # initialize path dictionary     
        path[start] = []                                   # add start node to path dictionary                

        for neighbor in self.next_node(start, end):         # for each neighbor of node
                    path[neighbor] = path[start] + [neighbor]   # add node to path list
        
        found = False

        while queue:
            node = queue.pop()                             # pop the first node in queue
            if node not in visited:                         # if node is not visited
                if node == end:
                    found = True                                # if node is end node
                    return path[node]                           # return path list

                if node not in visited:                         # if node is not visited
                    visited.append(node)       
                                    # add node to visited list
                    neighbors = self.next_node(node, end)
                    for neighbor in neighbors:                  # for each neighbor of node
                        path[neighbor] = path[node] + [node] + [neighbor] # add node to path list 
                        queue.append(neighbor)                  # add neighbors to queue

        # Traverse the graph in a breadth first manner
        if end == None:
            return visited                      # if no end node, return visited list

        if not found:
            return None                     # if no path exists, return None



