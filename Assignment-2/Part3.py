'''Assignment-2 : Part 3
A stack was created using lists in python. They are easily mutable. They also are capable of storing any datatype. No assumptions were required for this program
Test cases were created and used below. '''

class Stack:
    def __init__(self):
        self.data = []
        self.n = 0;
    
    def isEmpty(self):
        return self.n == 0
        
    def size(self):
        return ("Size is now " + str(self.n))
        
    def push(self, value):
        self.value = value
        self.data.append(self.value)
        self.n += 1
        print("You just added " + str(self.value))
        print(Stack.size(self))
    
    def top(self):
        if (Stack.isEmpty(self)):
            print("You want the top of the stack? Top of what stack? It's *empty* :') ")
            return
        print ("Top of Stack is now " + str(self.data[-1]))
    
    def pop(self):
        if (Stack.isEmpty(self)):
            print("Error: You're asking me to remove something from an already empty list? Don't make me end it all rn.\n")
            return 
        self.n -= 1
        t = self.data.pop()
        print("Not sure why but for some reason you removed " + str(t))
        print(Stack.size(self))

        
'''Test Cases'''    

print("\n\n Now for the Stack")        
stackList = Stack()
stackList.push(2)
stackList.push('Julia')
stackList.top()
stackList.push(5)
print("Current Stack = ", end = "")
print(stackList.data)
stackList.push(7)
stackList.top()
stackList.push('Jackie')
print("Current Stack = ", end = "")
print(stackList.data)

print("\nNow to pop!")
stackList.pop()
stackList.pop()
stackList.pop()
stackList.top()
print("Current Stack = ", end = "")
print(stackList.data)
stackList.pop()
stackList.pop()
print("Current Stack = ", end = "")
print(stackList.data)
stackList.top()

print("\nTime to mix things up a bit.")
stackList2 = Stack()
stackList2.push(4)
stackList2.push('Hannah')
stackList2.pop()
stackList2.top()
print("Current Stack = ", end = "")
print(stackList2.data)
stackList2.push('Montana')
stackList2.top()
stackList2.pop()
stackList2.pop()
print("Current Stack = ", end = "")
print(stackList2.data)
stackList2.top()
stackList2.pop()
stackList2.push(213)
stackList2.top()
print("Current Stack = ", end = "")
print(stackList2.data)
stackList2.push("Cody")
stackList2.push('Naomi')
stackList2.top()
print("Current Stack = ", end = "")
print(stackList2.data)
stackList2.pop()
stackList2.top()
print("Current Stack = ", end = "")
print(stackList2.data)

