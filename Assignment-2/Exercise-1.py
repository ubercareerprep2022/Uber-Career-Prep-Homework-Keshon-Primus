class TreeNode: #Object class for each node
    def __init__(self, key):
        self.left = None #left subtree
        self.right = None #right subtree
        self.val = key
        
    
def preorderPrint(root):
    
    if root: #if root node exists
        print(root.val, end = "--->")
    else:
        print("No nodes!")
    if root.left: #if left child node exists
        preorderPrint(root.left)
    if root.right: #if right child node exists
        preorderPrint(root.right)

def inorderPrint(root):
    
    if root: #if root node exists
        if root.left: #if left child node exists
            inorderPrint(root.left)
        print(root.val, end = "--->")
        if root.right: #if right child node exists
            inorderPrint(root.right)
    else:
        print("No Nodes!")
        
def postorderPrint(root):
    
    if root: #if root node exists
        if root.left: #if left child node exists
            postorderPrint(root.left)
        if root.right: #if right child node exists
            postorderPrint(root.right)
        print(root.val, end = "--->")
    else:
        print("No Nodes!")

				
#Test cases to create a tree
root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(17)
root.right.left = TreeNode(6)
root.right.right = TreeNode(3)

print("\nPreorder: ", end = "")
preorderPrint(root)

print("\nInorder: ", end = "")
inorderPrint(root)

print("\nPostorder: ", end = "")
postorderPrint(root)
