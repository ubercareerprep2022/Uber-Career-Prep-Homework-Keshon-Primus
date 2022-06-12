class Node:
    def __init__(self, data): #Node class for each node in tree
        self.data = data
        self.left = None
        self.right = None
        
    
    def insertNode(self, number): #adds new node to tree
        if number == self.data:
            return "Error. Number " + str(number)+ " is a Duplicate value." #prevents duplicate values from being added
            
        if number < self.data:
            if self.left: #if left child exists
                return self.left.insertNode(number)
            else:
                self.left = Node(number) #new left child
                
        elif number > self.data:
            if self.right: #if right child exists
                return self.right.insertNode(number)
            else:
                self.right = Node(number) #new right child
        
        
    def findNode(self, number): 
        if not self: #if tree is empty
            return "Error. Empty tree."
            
        if self.data == number: #if number is found
            return "Found! Number " + str(number)+ " exists in tree."
        
        elif number < self.data: #search left subtree if exists
            if self.left: 
                return self.left.findNode(number) #recursive left subtree search
            else:
                return "Number " + str(number)+ " Not found :("
        elif number > self.data: #search right subtree if exists
            if self.right:
                return self.right.findNode(number)  #recursive right subtree search
            else:
                return "Number "  + str(number)+ " Not found :("
        else:
            return "Number "  + str(number)+ " Not found :("
            
    
    def preorder(self): 
        if self:
            print(self.data, end = "-->")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
            
    def inorder(self):
        if self.left:
            self.left.inorder()
        if self:
            print(self.data, end = "-->")
        if self.right:
            self.right.inorder()
            
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        if self:
            print(self.data, end = "-->")
            

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    
    def push(self, number): #add to Binary Search Tree ADT
        if self.root:
            return self.root.insertNode(number)
        else:
            self.root = Node(number)
            return "New Root Node Created!"
            
    
    def find(self, number): #Find numbe rin Binary Search Tree ADT
        if not self.root:
            return "Error. Empty Binary Search Tree."
        else:
            return self.root.findNode(number)
            
    def postorderPrint(self):
        print("\nPostorder:" , end = "")
        self.root.postorder()
            
    def inorderPrint(self):
        print("\nInorder: ", end = "")
        self.root.inorder()
     
    def preorderPrint(self):
        print("\nPreorder: ", end = "")
        self.root.preorder()

            
Tree1 = BinarySearchTree()
print(Tree1.push(10))
Tree1.push(17)
Tree1.push(13)
print(Tree1.find(19))
Tree1.postorderPrint()
Tree1.preorderPrint()
Tree1.inorderPrint()
print()
print(Tree1.find(10))
print(Tree1.find(72))
print(Tree1.push(10))
