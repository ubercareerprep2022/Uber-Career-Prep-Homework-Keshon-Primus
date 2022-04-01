'''Assignment-2 : Part 4
A queue was created using lists in python. They are easily mutable. They also are capable of storing any datatype. No assumptions were required for this program
Test cases were created and used below. '''

class Queue:
    def __init__(self):
        self.data = []
        self.n = 0;
    
    def isEmpty(self):
        return self.n == 0
        
    def size(self):
        return ("Size is now " + str(self.n))
        
    def enqueue(self, value):
        self.value = value
        self.data.append(self.value)
        self.n += 1
        print("You just added " + str(self.value))
        print(Queue.size(self))
    
    def front(self):
        if (Queue.isEmpty(self)):
            print("You want the front of the queue? front of what queue? It's *empty* :') ")
            return
        print("Front of Queue = " + str(self.data[0]))
        
    def rear(self):
        if (Queue.isEmpty(self)):
            print("You want the last value of the queue? front of what queue? It's *empty* :') ")
            return
        print("Last value of Queue is now " + str(self.data[-1]))
    
    def dequeue(self):
        if (Queue.isEmpty(self)):
            print("Error: You're asking me to remove something from an already empty list? Don't make me end it all rn.\n")
            return 
        self.n -= 1
        t = self.data.pop(0)
        print("Not sure why but for some reason you removed " + str(t))
        print(Queue.size(self))

        
'''Test Cases'''    

print("\n\nProcessing for the Queue \n")
queueList1 = Queue()
queueList1.enqueue(2)
queueList1.enqueue('Julia')
queueList1.front()
print("Current Queue = ", end = "")
print(queueList1.data)
queueList1.enqueue(5)
queueList1.enqueue(7)
queueList1.front()
queueList1.enqueue('Jackie')
print("Current Queue = ", end = "")
print(queueList1.data)

print("\nNow to dequeue!")
queueList1.dequeue()
queueList1.dequeue()
queueList1.dequeue()
queueList1.front()
print("Current Queue = ", end = "")
print(queueList1.data)
queueList1.dequeue()
queueList1.dequeue()
queueList1.front()
print("Current Queue = ", end = "")
print(queueList1.data)

print("\nTime to mix things up a bit.")
queueList2 = Queue()
queueList2.enqueue(4)
queueList2.enqueue('Hannah')
queueList2.dequeue()
queueList2.front()
queueList2.enqueue('Montana')
queueList2.front()
queueList2.dequeue()
queueList2.dequeue()
queueList2.front()
print("Current Queue = ", end = "")
print(queueList2.data)
queueList2.dequeue()
queueList2.enqueue(213)
queueList2.front()
queueList2.enqueue("Cody")
print("Current Queue = ", end = "")
print(queueList2.data)
queueList2.enqueue('Naomi')
queueList2.front()
queueList2.dequeue()
queueList2.front()
print("Current Queue = ", end = "")
print(queueList2.data)