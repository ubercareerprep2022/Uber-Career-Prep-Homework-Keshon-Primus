'''Manually written code for Part 1 of Assignment 1
Assumptions - No whitespace entered '''

def isPermutation(string1, string2):
    
    list1 = []
    list2 = []
    string1 = string1.upper()
    string2 = string2.upper()

    'checks if both string are of equal length to continue validation, otherwise: False'
    if (len(string1) == len(string2)): 
        for i in range(0, len(string1), 1):
            'input each string into a list for easy verification'
            list1.append(string1[i])
            list2.append(string2[i])
            
            'sorts both lists for easier verification'
            list1.sort()
            list2.sort()
        return (list1 == list2)
    return False
    
inputA = input("\nEnter first string: ")
inputB = input("Enter second string: ")

if (isPermutation(inputA, inputB)):
    print ("This is a Permutation!")
else:
    print("This is not a Permutation.")

'Test cases' 
print(isPermutation("asdf", "fsda"))
print(isPermutation("asdf", "fsa")) 
print(isPermutation("asdf", "fsax"))
print(isPermutation("HaNnah", "Ahnnah"))
    