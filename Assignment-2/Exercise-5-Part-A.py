class Person:
    def __init__(self, name, phonenumber):
        self.name = name
        self.phonenumber = phonenumber
        

phonebookList = []


def size():
    n = len(phonebookList)
    return "This phonebook contains " + (str(n) + " contacts." if n != 1 else str(n) + " contact.") 


def addContact(newname, newnumber):
    for i in range(0, len(phonebookList), 1):
        if phonebookList[i].phonenumber == newnumber:
            return "\nError. number already exists in Phonebook"
    phonebookList.append(Person(newname, newnumber))
    


def findContact(nametoFind, numbertoFind):
    for i in range(0, len(phonebookList), 1):
        if phonebookList[i].phonenumber == numbertoFind and phonebookList[i].name == nametoFind:
            print("\nPerson found! ---> Name:", str(phonebookList[i].name), end = ", ") 
            print("Number:" + str(phonebookList[i].phonenumber))
            return True
        elif phonebookList[i].phonenumber == numbertoFind:
            print("\nPhone number found, but Phoneholder does not match.")
            return False
        elif phonebookList[i].name == nametoFind:
            print("\nName found, but phone number attached does not match.")
            return False
        else:
            print("\nError. Person not found.")
            return False


def findName(numberusedtoFind):
    for i in range(0, len(phonebookList), 1):
        if phonebookList[i].phonenumber == numberusedtoFind:
            print("Name attached to", phonebookList[i].phonenumber, end = ": ")
            print(phonebookList[i].name)
            return
        
    print("No name found for that number.")
 

             
def findNumber(nameusedtoFind):
    for i in range(0, len(phonebookList), 1):
        if phonebookList[i].name == nameusedtoFind:
            print("Number attached to", phonebookList[i].name, end = ": ")
            print(phonebookList[i].phonenumber)
            return
    
    print("No number found for that name.")
         

def removeContact(nametoRemove, numbertoRemove):
    if findContact(nametoRemove, numbertoRemove):
        for i in range(0, len(phonebookList)):
            if phonebookList[i].name == nametoRemove:
                phonebookList.pop(i)
        return "\nRemoved an item."
    else:
        for i in range(0, len(phonebookList)):
            if (phonebookList[i].name == nametoRemove and phonebookList[i].phonenumber != numbertoRemove) or (phonebookList[i].name != nametoRemove and phonebookList[i].phonenumber == numbertoRemove):
                print("\nWARNING: Potential Name and Number found that matches 1 of the descriptions: ", phonebookList[i].name, phonebookList[i].phonenumber)
                delete = str(input("Do you wish to delete this contact? (Y/N)"))
                while delete != "N" and delete != "n" and delete != "Y" and delete != "y":
                    delete = str(input("Error: Invalid Key. Do you wish to delete this contact? (Y/N)"))
                if delete == "N" or delete == "n":
                    print("No item deleted.")
                    continue
                else:
                    phonebookList.pop(i)
                    print("item deleted.")
                    continue
    
                    
def printphoneBook():
    print("\n***************PHONEBOOK LIST****************")
    for i in range(0, len(phonebookList), 1):
        print(i+1, end = ". ")
        print("Name:", phonebookList[i].name, end = ", ")
        print("Number:", phonebookList[i].phonenumber)
        
        
        
addContact("Kevin", 3498172)
findContact("Kevin", 3498172)
addContact("Paul Rosen", 40533617)
printphoneBook()
addContact("Kevin", 8139975307)
print(removeContact("Kevin", 3498162))
printphoneBook()
print(size())
findNumber("Kevin")
findName(3498162)
findName(40533617)
printphoneBook()
