
class Node: #Node Class
    def __init__(self, data):
        self.data = data
        
class Edge: #Edge Class
    def __init__(self, key1,key2):
        self.keys = (key1,key2)
        
        
class Graph: #Graph Class which consist of list of Nodes and List of Edges
    def __init__(self):
        self.graph = []
        self.nodes = []
        self.edges = []
        
    
    def addNode(self, value):
        if value not in self.nodes:
            newNode = Node(value)
            self.nodes.append(newNode)
        else:
            print("\nError. Already exists.")
    
    
    def addEdge(self, key1,key2):
        for i in self.nodes:
            if key1 == i.data:
                for j in self.nodes:
                    if key2 == j.data:
                        newEdge = Edge(key1, key2)
                        self.edges.append(newEdge)
                        print("\nAdded new edge")
                        
    
    def removeNode(self, value):
        for i in self.nodes:
            if value == i.data:
                self.nodes.pop(self.nodes.index(i))
        for j in self.edges:
            if value in j.keys:
                self.edges.pop(self.edges.index(j))
                print("\nSuccessfully removed Node")
        
            
    def removeEdge(self, key1,key2):
        for i in self.edges:
            if key1 in i.keys and key2 in i.keys:
                self.edges.pop(self.edges.index(i))
                print("\nSuccessfully removed edge")
                return
        print("\nError. Edge cannot be found")
            
    
    def getAdjNodes(self, node):
        adjlist = []
        for i in self.edges:
            if node in i.keys:
                adjlist.append(i.keys)
        print("\nAdjacency listing for", node, end = ": ")
        for j in adjlist:
            print(j, end = ", ")
        
    def printGraph(self):
        print("\nNodes: ", end = "")
        for k in self.nodes:
            print(k.data, end = ", ")
        
        print("\nEdges: ", end = "")
        for l in self.edges:
            print(l.keys, end = ", ") 
                
        
           
#Test Cases                     
g1 = Graph()
g1.addNode(1)
g1.addNode(2)
g1.addNode(3)
g1.addNode(4)
g1.addNode(5)
g1.printGraph()
g1.addEdge(1,2)
g1.addEdge(1,4)
g1.addEdge(2,4)
g1.addEdge(1,3)
g1.addEdge(3,1)
g1.addEdge(3,4)
g1.addEdge(2,3)
g1.printGraph()
#g1.removeNode(4)    
#g1.removeEdge(1,4)
g1.printGraph()
g1.getAdjNodes(1)
g1.getAdjNodes(3)
