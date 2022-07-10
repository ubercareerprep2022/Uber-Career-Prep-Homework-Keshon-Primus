class Graph: #Graph Class
    def __init__(self, vertices):
        self.graph = {}
        
        
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
