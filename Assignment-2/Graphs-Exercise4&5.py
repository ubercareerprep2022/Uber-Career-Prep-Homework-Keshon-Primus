class Graph: #Graph Class
    def __init__(self, vertices):
        self.graph = {}
        self.v = vertices
        
        
    def addEdge(self, node1, node2): #Adds edge to graph structure
        self.graph[node1] = []
        self.graph[node1].append(node2)
        
    def BFS_Shortest_Path(self, graph, start, goal): #Shortest Path via BFS search
        explored = []
        
        q = [[start]]
        
        if start == goal:
            print("Same Node lol")
            return
        
        while q:
            path = q.pop(0)
            node = path[-1]
            
            if node not in explored:
                negihbours = self.graph[node]
                
                for negihbour in negihbours:
                    new_path = list(path)
                    new_path.append(negihbour)
                    q.append(new_path)
                    
                    if negihbour == goal:
                        print("Shortest path = ", new_path)
                        return
                explored.append(node)
                
        print("So sorry, but a connecting path doesn't exist :(")
        return
    
    
    def isCycleHelper(self, v, visited, rackstack):
        visited[v] = 1
        rackstack[v] = 1
        
        for neighbour in self.graph[v]:
            if visited[neighbour] == 0:
                if self.isCycleHelper(neighbour, visited, rackstack) == 1:
                    return True
            elif rackstack[neighbour] == True:
                return True
                
        rackstack[v] = 0
        return False
        
    
    def isCycle(self):
        visited = [0]*((self.v)+1)
        rackstack = [0]*((self.v)+1)
        
        for node in range(self.v):
            if visited[node] == 0:
                if self.isCycleHelper(node, visited, rackstack) == 1:
                    return "Graph has a Cycle!"
        return "Graph has no Cycle."
    
#Test Cases   
g = Graph(1)
g.addEdge(1, 5)
g.addEdge(0, 5)
g.addEdge(5, 2)
g.addEdge(1, 4)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.BFS_Shortest_Path(g, 0, 2)
print(g.isCycle())
