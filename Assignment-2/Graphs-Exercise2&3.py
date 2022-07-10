class Graph: #Graph Class
    def __init__(self):
        self.graph = {}
        
        
    def addEdge(self, node1, node2): #Adds edge to graph structure
        self.graph[node1] = []
        self.graph[node1].append(node2)
        
    def DFSHelper(self, curr, visited):
        
        visited.append(curr)
        print(curr, end="-->") #Add current node to visited list and print it
        
        for adjnode in self.graph[curr]:#Go through list of values in dictionary for that key
            if adjnode not in visited:  #and check if visited
                self.DFSHelper(adjnode, visited)
                
                
    def DFS(self):
         
        visited = []#list with all visited vertices
        
        for vertex in self.graph:
            if vertex not in visited:
                self.DFSHelper(vertex, visited) #call recursive helper function to print DFS traversal
                
    
    def BFS(self, s):
 
        
        visited = [0] * (max(self.graph) + 1) #Mark all the vertices as not visited
 
        
        queue = [] #Create a queue
 
        
        queue.append(s) #Mark the source node as visited
        visited[s] = 1
 
        while queue:
 
            
            s = queue.pop(0)#Dequeue a node from queue
            print (s, end = "-->")
 
            # Get all adjacent vertices of s. If an adjacent node has not been visited, then enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


                    
#Test Cases
print("Following is Depth First Traversal \n")
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.DFS()

print ("\n The following is Breadth First Traversal (starting from vertex 1)")
g.BFS(1)
                
