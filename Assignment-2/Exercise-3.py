class TreeNode:
    def __init__(self, data):
        self.employees = []
        for i in data: #accepts an array of input for name and title of employees
            self.employees.append(i)
        self.left = self.right = None
    

def NumberOfLevels(root):
    if not root: #if the tree's root does not exist
        print("Error. Empty Tree.")
        return
    else: #breadth first search using queue. 
        levelqueue = []
        levelqueue.append(root) #append the root node to the queue to start breadth first search
        levelcounter = 0
        
        while levelqueue: #ensures that the entire tree is traversed through by ensuring that the queue is not empty until all nodes are appended
        
            queuecount = len(levelqueue) 
            levelcounter += 1 #increases the count of levels
            
            while queuecount > 0: #enusres that all nodes for a particular level are input into the queue before moving onto the next level
                
                nodetoprint = levelqueue.pop(0) #remove the node that is to be used from the queue. This is the first node added to the queue
                
                if nodetoprint.left: #if a left subtree exists
                    levelqueue.append(nodetoprint.left)
                if nodetoprint.right: #if a right subtree exists
                    levelqueue.append(nodetoprint.right)
                    
                queuecount -= 1 #used to check whether the queue for that particular level is empty. If empty, it cycles to the next level of the tree
               
            
        return "\nNumber of levels: " + str(levelcounter)
        
        
 #test cases. A tree is created and tested with the values below.       
root = TreeNode([["Sarah", "CEO"], ["Jim", "Sales Rep"]])
root.left = TreeNode([["Pam", "Receptionist"], ["Selena", "Accounting"]])
root.right = TreeNode([["Creed", "I don't know"], ["Taylor", "Assistant"]])
root.left.left = TreeNode([["Michael", "Regional Managaer"], ["Adam", "IT"]])
root.left.right = TreeNode(["John", "Security"])
print(NumberOfLevels(root))
