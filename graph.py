# DFS
def dfs_iter(adj, s): 
    """
    Iterative DFS: implement using a stack. 

    Stack is a FIFO data structure, which helps with DFS depth-first exploration. 
    The nodes we most recently pushed onto the stack are popped off for continued 
    exploration. 

    Time complexity: O(|V| + |E|) - at worst we traverse all nodes and edges
    Space complexity: O(|V|) - we store all nodes in order to be returned. 
    We also maintain the stack to store the nodes. 

    Assume order = order for which nodes are popped off the stack. 
    """
    
    # Initialize stack, parents dict, order 
    stack = [] 
    parents = {key: None for key in adj.keys()}
    order = [] 

    # Push s onto stack, add to parents
    stack.append(s) 
    parents[s] = s  

    while stack: 
        node = stack.pop() # Pop from most recently added (LIFO) 
        order.append(node) # Append node from the order of visitation
        for neighbor in adj[node]: 
            if parents[neighbor] is None: # If neighbor hasn't been visited
                stack.append(neighbor) 
                parents[neighbor] = node 
    
    return order 


def dfs_recurse(adj, s, parents=None, order=None): 

    # If this is the first instance of recursion, initialize parents and order 
    if not parents and not order: 
        parents = {key: None for key in adj.keys()}
        parents[s] = s 
        order = [] 
    
    for neighbor in adj[s]: 
        if parents[neighbor] is None: 
            parents[neighbor] = s
            # Recursively call DFS from each neighbor 
            dfs_recurse(adj, neighbor, parents, order) 

    # Add s to the order of exploration 
    # If you think about the recursion call stack, order.append(s) happens when s's neighbors have all been explored (and hence the graph starting from s has been fully explored, so we append s to the order to signify its completed exploration) 
    order.append(s) 
    return order 
    

# BFS
def bfs(adj, s): 
    """
    Time: O(|V| + |E|)
    Space: O(|V|) - mustkeep track of queue, parents, and order 
    """  
    parents = {node: None for node in adj.keys()}
    queue = [] 
    parents[s] = s
    queue.append(s) 
    order = [] 

    while queue: 
        node = queue.pop(0) # Pop from the front of the queue (FIFO) 
        order.append(node) 
        for neighbor in adj[node]: 
            if parents[neighbor] is None: # Add new nodes to the back of the queue 
                parents[neighbor] = node 
                queue.append(neighbor) 
    
    return order 


# DIJKSTRA
import heapq 
def dijkstra(adj, s): 
    """
    A BFS-like greedy algorithm for finding the shortest path in a weighted, non-negative graph. 
    """
    # Create parents dictionary, heap to keep track of the nodes,
    parents = {node: None for node in adj.keys()}
    weight_sums = {node: float('inf') for node in adj.keys()} # A mapping of nodes to the (eventual) sum of the shortest path from the starting node to that node 
    minheap = [] 

    # Add source node to the data structures 
    parents[s] = s 
    weight_sums[s] = 0 
    heapq.heappush(minheap, (0, s)) # Push the (distance from source, source node) tuple onto the heap 

    while minheap: 
        weight_source_to_node, node = heapq.heappop(minheap) # Pop the smallest item from the heap 
        # Iterate over the neighbors
        for edge_weight, neighbor in adj[node]: 
            new_weight_source_to_neighbor = weight_source_to_node + edge_weight 
            # If the new_weight_sum to the neighbor is smaller than the one stored in weight_sums, update the data structures
            if new_weight_source_to_neighbor < weight_sums[neighbor]: 
                weight_sums[neighbor] = new_weight_source_to_neighbor 
                parents[neighbor] = node 
                heapq.heappush(minheap, (new_weight_source_to_neighbor, neighbor))
    
    # At the end of the algorithm, parents and weight_sums will be populated 
    return parents, weight_sums 
    

# BELLMAN-FORD
def bellman_ford(adj, s):
    """
    An algorithm for finding the shortest path in a weighted graph 
    that also could have negative edges. 
    """ 
    pass 

import unittest 

class TestGraphTraversalMethods(unittest.TestCase): 
    def test_dfs_iter(self): 
        adj = {0: {1, 3, 4}, 
              1: {0}, 
              2: {3}, 
              3: {0, 2}, 
              4: {0}}
        expected_order = [0, 4, 3, 2, 1]
        self.assertEqual(expected_order, dfs_iter(adj, 0)) 
    
    def test_dfs_recurse(self): 
        adj = {0: {1, 3, 4}, 
              1: {0}, 
              2: {3}, 
              3: {0, 2}, 
              4: {0}}
        expected_order = [1, 2, 3, 4, 0]
        self.assertEqual(expected_order, dfs_recurse(adj, 0))
    
    def test_bfs(self): 
        adj = {0: {1, 3, 4}, 
              1: {0}, 
              2: {3}, 
              3: {0, 2}, 
              4: {0}}
        expected_order = [0, 1, 3, 4, 2]
        self.assertEqual(expected_order, bfs(adj, 0))
    
    def test_dijkstra(self):  
        adj = {0: {(100, 1)}, 1: {(100, 2), (600, 3)}, 2: {(100, 0), (200, 3)}, 3: {}}
        parents = {0:0, 1:0, 2:1, 3:2}
        weight_sums = {0:0 ,1:100, 2:200, 3:400}
        self.assertEqual((parents, weight_sums), dijkstra(adj, 0))
        


if __name__ == '__main__':
    unittest.main()
