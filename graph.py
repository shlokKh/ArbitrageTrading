class graph:
    def __init__(self, size):
        self.graph = []
        self.numEdges = 0
        for i in range(size): 
            row=[] 
            for j in range(size): 
                row.append(0) 
            self.graph.append(row) 

    def find_edge(self, u, v):
        if self.graph[u][v] == 1:
            return graph[u][v]
        else:
            return None
    
    def add_edge(self, u, v, weight):
        if find_edge is None:
            self.numEdges += 1
            self.graph[u][v] = weight
            return True
        else:
            return False
    
    def print_matrix(self):
        for i in range(len(self.graph)):
            string = ""
            for j in range(len(self.graph)):
                string += str(self.graph[i][j]) + " "
            print(string)
            
