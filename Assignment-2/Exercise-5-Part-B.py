class Node:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.left = None
        self.right = None
        
        
    
    def addNode(self, name, number):
        if self:
            if name < self.name:
                if self.left:
                    return self.left.addNode(name, number)
                else:
                    self.left = Node(name, number)
            elif name > self.name:
                if self.right:
                    return self.right.addNode(name, number)
                else:
                    self.right = Node(name, number)
        else:
            return "Error. no Phonebook available."
            
    
    def findName(self, name):
        if self.name == name:
            return "Found Name! Number is " + str(self.number)
        elif name < self.name:
            if self.left:
                return self.left.findName(name)
        elif name > self.right:
            if self.right:
                return self.right.findName(name)
        else:
            return "Name not found."
                
    def findNumber(self, number):
        if self.number == number:
            return "Found number! Name is " + str(self.name)
        elif number < self.number:
            if self.left:
                return self.left.findNumber(number)
        elif number > self.number:
            if self.right:
                return self.right.findNumber(number)
        else:
            return "Number not found."
            
    
    def preorder(self):
        if self:
            print("Name: ", self.name, end = ", ")
            print("Number: ", self.number)
            
        if self.left:
            return self.left.preorder()
        if self.right:
            return self.right.preorder()
    
            
            
class Phonebook:
    def __init__(self):
        self.root = None
        
        
    def newContact(self, name, number):
        if self.root:
            return self.root.addNode(name, number)
        else:
            self.root = Node(name, number)
        
            
    def findContactbyName(self, name):
        if self.root:
            return self.root.findName(name)
        else:
            return "Error. Empty Phonebook."
        
            
    def findContactbyNumber(self, number):
        if self.root:
            return self.root.findNumber(number)
        else:
            return "Error. Empty Phonebook."
            
    
    def preorderprint(self):
        print("*******************PHONEBOOKLIST*******************")
        
        if self.root:
            return self.root.preorder()
        else:
            print("Error. Empty Phonebook.")
            
            
Phonebook1 = Phonebook()

Phonebook1.newContact("Maysam", 4077413377)
Phonebook1.newContact("Paul", 4324123423)
Phonebook1.newContact("Zack", 421234564)
print(Phonebook1.findContactbyName("Maysam"))
print()
print()
Phonebook1.preorderprint()
