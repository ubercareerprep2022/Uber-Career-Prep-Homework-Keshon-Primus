'''Assignment 1 - Part 2 - B

Assumptions - Only numerical values entered.
            - A number can be used twice (eg. (3, 3)) if targetsum - number = number (eg. 6 - 3 = 3)'''

def pairsthatEqualTargetSum(targetsum, inputArray = []):

    'declaration of lists that we will need later'
    returnlist = []
    'sorts array numerically'
    inputArray.sort() 
    differencelist = []
    
    'adding the difference from the target sum and the numbers of the array into a new list'
    for i in inputArray:
        differencelist.append(targetsum-i)
    
    for j in differencelist:
        if (j in inputArray):
            'to ensure no repetition of the same numbers as a sublist'
            if (((j, (targetsum-j)) not in returnlist) and ((targetsum-j, j) not in returnlist)):
                returnlist.append(((targetsum - j), j))
    return returnlist

    
inputArray = []
'prompt for input from user'
n = int(input("Enter the number of elements in the array: "))
print("Enter the numbers in the array: ", end = "")

'input data into array'
for i in range (0, n, 1):
    num = int(input())
    inputArray.append(num)
targetsum = int(input("Enter targetsum: "))
print("\nPairs that add to the target4 s5um of " + str(targetsum) + ": ", end = "")
print(pairsthatEqualTargetSum(targetsum, inputArray))

'Test Cases'
print(pairsthatEqualTargetSum(5, [1, 2, 3, 4, 5]))
print(pairsthatEqualTargetSum(1, [1, 2, 3, 4, 5]))
print(pairsthatEqualTargetSum(7, [1, 2, 3, 4, 5]))
print(pairsthatEqualTargetSum(13, [1, 6, 3, 8, 7]))