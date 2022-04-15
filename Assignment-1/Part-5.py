#Keshon Primus
#Assignment 1 Part 4

class LinkedNode: #Class for the nodes of the linked list
    def __init__(self, data):
        self.data = data
        self.next_ = None
        
    
class LinkedList(object): #Class for the actual linking of the linked list
    
    def __init__(self):
        self.head = None
        self.n = 0
        
    def push(self, new_data): #Adds new node at end of linked list
        newNode = LinkedNode(new_data)
        
        if self.head is None: #if linked list is empty
            self.head = newNode #creates new node and assigns it to head
            self.n += 1 #increases counter of size of linked list
            return
        
        else:
            tail = self.head #adds to end if empty
            while (tail.next_):
                tail = tail.next_
                
            tail.next_ = newNode
        self.n += 1
        
    def insertAfter(self, new_data, prev_node): #Inserts new node in between 2 nodes in linked list
        
        if prev_node is None: #if linked list is empty
            print("Error: Not possible.")
            return
        
        newNode = LinkedNode(new_data) #creates new node
        newNode.next_ = prev_node.next_
        prev_node.next_ = newNode
        self.n += 1 #increase size of counter
    
    def size(self): #finds the size of the linked list
        return self.n
        
    def isEmpty(self): #is linked list empty?
        return (self.head is None)
        
    def printList(self): #prints the entire linked list
        last = self.head
        while (last): #iterates through linked list for printing
            print(last.data, end = "-->")
            last = last.next_
    
    def pop(self): #Removes last node in linked list
        if self.head is None: #if linked list is empty
            print("Error: Linked List is empty.")
            return
        
        else:
            tail = self.head
            while (tail.next_.next_): #iterates through linked list to find last node
                tail = tail.next_
                
            tail.next_ = None
        self.n -= 1 #decrement counter after deletion

        
    def remove(self, index_to_delete): #Removes node with a particular index value from linked list
        
        i = 0
         
        if self.head is None: #if linked list is empty
            return "Empty List." 
        
        elif i == index_to_delete: #if index is 0
            old = self.head.data
            self.head = self.head.next_
            return "Deleted " + str(old)
            
        elif index_to_delete > self.n: #if index is not in the linked list
            return "Error: Index out of Range for Deletion."
        
        else: #if iteration trhough linked list is needed to find the node with index value
            temp = self.head
            prev = self.head
            current = self.head
            while(current): #iterates through linked list to find node with index value to delete
                if i == index_to_delete:
                    old = current.data #singling out the node to be deleted
                    temp = current.next_
                    break
                prev = current
                current = current.next_
                i += 1
            prev.next_ = temp
            return "Deleted " + str(old)
        
                
                
    def elementAt(self, index): #Finds value of data in the node with a particular index
        
        temp = self.head
        i = 0
        
        while (temp): #iterate through linked list
            if self.head is None: #if linked list is empty
                return "\nError: Empty List."
                
            elif index > self.n: #if index is not in linked list
                return "\nError: Index out of range."
                
            elif (i == index): 
                return temp.data
            
            else:
                temp = temp.next_
                i += 1
        
        
            
llist = LinkedList() #Creates linked list
 
#Test Cases

# Insert 6.  So linked list becomes 6->None
llist.push(6)
 
    # Insert 7 at the beginning. So linked list becomes 7->6->None
llist.push(7);
 
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
llist.push(1);
 
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
llist.push(4)

llist.insertAfter(8, llist.head.next_)
llist.printList()
print()

llist.insertAfter(1, llist.head)
llist.printList()
print()

llist.insertAfter(3, llist.head.next_.next_.next_)

print(llist.size())
llist.printList()
print()
print()

llist.pop()
llist.printList()
print()
print()

print("Element at index is:", llist.elementAt(7))
print("Element at index is:", llist.elementAt(4))

print(llist.remove(17))
print(llist.remove(3))
llist.printList()
