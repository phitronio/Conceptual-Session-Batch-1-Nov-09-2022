from queue import Queue
class Graph:
    def __init__(self, num_of_nodes, directed = False):
        self.num_of_nodes = num_of_nodes
        self.directed = directed
        self.adj_matrix = [[0 for col in range(self.num_of_nodes)] for row in range(self.num_of_nodes)]
        self.adj_list = {node:set() for node in range(self.num_of_nodes)}
        # self.adj_list = [[] for _ in range(self.num_of_nodes)] # [[],[]]
        # print(self.adj_list)
        # print(self.adj_matrix)
    def add_nodes_to_adj_list(self, node1, node2):
        self.adj_list[node1].add(node2)
        if not self.directed: # bidirectinal graph
            self.adj_list[node2].add(node1)
            
    def add_nodes_to_adj_matrix(self, node1, node2):
        self.adj_matrix[node1][node2] = 1
        if not self.directed: # bidirectinal graph
            self.adj_matrix[node2][node1] = 1
    
    def bfs_traversal(self, start_node): # O(V+E)
        visited = set() # {}
        queue = Queue() #[]
        queue.put(start_node)
        visited.add(start_node)
        while not queue.empty(): # queue is not empty
            curr_node = queue.get() # curr_node ta beriye gelo 0
            print(curr_node, end = " ") # 0
            for child in self.adj_list[curr_node]: # 1--> 0,2,3
                if child not in visited:
                    queue.put(child)
                    visited.add(child)
    visited = set()
    def dfs_traversal(self,start_node): # start_node = 0
        if start_node not in self.visited:
            print(start_node, end = " ") # 0 printed
            self.visited.add(start_node)
            for child in self.adj_list[start_node]: # 0--> 1,2
                self.dfs_traversal(child)
        
            
            

g = Graph(5, False)
g.add_nodes_to_adj_list(0,1)
g.add_nodes_to_adj_list(0,2)
g.add_nodes_to_adj_list(1,2)
g.add_nodes_to_adj_list(1,4)
g.add_nodes_to_adj_list(2,3)
g.add_nodes_to_adj_list(3,4)

g.add_nodes_to_adj_matrix(0,1)
g.add_nodes_to_adj_matrix(0,2)
g.add_nodes_to_adj_matrix(1,2)
g.add_nodes_to_adj_matrix(1,4)
g.add_nodes_to_adj_matrix(2,3)
g.add_nodes_to_adj_matrix(3,4)

print(f"Adjacency List {g.adj_list}")
print(f"Adjacency Matrix {g.adj_matrix}")
print(f"Run Bfs {g.bfs_traversal(0)}")
print(f"Run Dfs {g.dfs_traversal(0)}")



# 1. Make a graph
# 2. Print Adjacency List
# 3. Print Adjacency Matrix
# 4. Run Bfs
# 5. Run Dfs
# 6. Exit





# num_of_nodes = 3
# [[0,1,2],[3,4],[5,6,7]] = adj_matrix
# adj  list = {1 : {}, 2 : {}, 3 : {}}
#  node,  
