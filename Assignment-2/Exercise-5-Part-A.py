class Person: #creates each contact object for the phonebook
    def __init__(self, name, phonenumber):
        self.name = name
        self.phonenumber = phonenumber
        

phonebookList = [] #phonebook list structure (initially empty


def size():
    n = len(phonebookList)
    return "This phonebook contains " + (str(n) + " contacts." if n != 1 else str(n) + " contact.") 


def addContact(newname, newnumber):
    for i in range(0, len(phonebookList), 1):
        if phonebookList[i].phonenumber == newnumber: #checks to see if contact already exists. We assume that each phone number is unique
            return "\nError. number already exists in Phonebook"
    phonebookList.append(Person(newname, newnumber)) #adds contact object to the phonebook list
    


def findContact(nametoFind, numbertoFind):
    for i in range(0, len(phonebookList), 1):
        if phonebookList[i].phonenumber == numbertoFind and phonebookList[i].name == nametoFind: #if name and number match with a contact in phonebook
            print("\nPerson found! ---> Name:", str(phonebookList[i].name), end = ", ") 
            print("Number:" + str(phonebookList[i].phonenumber))
            return True
        elif phonebookList[i].phonenumber == numbertoFind: #if only number matches
            print("\nPhone number found, but Phoneholder does not match.")
            return False
        elif phonebookList[i].name == nametoFind: #if only name matches
            print("\nName found, but phone number attached does not match.")
            return False
        else: #if nothing matches 
            print("\nError. Person not found.") 
            return False


def findName(numberusedtoFind):
    for i in range(0, len(phonebookList), 1):
        if phonebookList[i].phonenumber == numberusedtoFind: #if number mathces a contact in phonebook
            print("Name attached to", phonebookList[i].phonenumber, end = ": ")
            print(phonebookList[i].name) #prints corresponding name
            return
        
    print("No name found for that number.") #if no name matches
 

             
def findNumber(nameusedtoFind):
    for i in range(0, len(phonebookList), 1):
        if phonebookList[i].name == nameusedtoFind: #if name matches a contact in phonebook
            print("Number attached to", phonebookList[i].name, end = ": ")
            print(phonebookList[i].phonenumber) #prints corresponding number
            return
    
    print("No number found for that name.") #if no number matches
         

def removeContact(nametoRemove, numbertoRemove):
    if findContact(nametoRemove, numbertoRemove): #if the contact name and number both match an existing contact in phonebook
        for i in range(0, len(phonebookList)):
            if phonebookList[i].number == numbertoRemove: #looks for contact by number. We assume number is unique
                phonebookList.pop(i) #delete contact from phonebook
        return "\nRemoved an item."
    else:
        for i in range(0, len(phonebookList)): #if name or number matches, but not both
            if (phonebookList[i].name == nametoRemove and phonebookList[i].phonenumber != numbertoRemove) or (phonebookList[i].name != nametoRemove and phonebookList[i].phonenumber == numbertoRemove):
                print("\nWARNING: Potential Name and Number found that matches 1 of the descriptions: ", phonebookList[i].name, phonebookList[i].phonenumber) #prompts to ask for a user suggestion before deleting
                delete = str(input("Do you wish to delete this contact? (Y/N)")) #prompts user to confirm deletion
                while delete != "N" and delete != "n" and delete != "Y" and delete != "y": #input validation
                    delete = str(input("Error: Invalid Key. Do you wish to delete this contact? (Y/N)"))
                if delete == "N" or delete == "n": #if user does not wish to delte
                    return "No item deleted."
                else:
                    phonebookList.pop(i) #if user wishes to delete
                    return "item deleted."
                    
    
                    
def printphoneBook(): #print entire phonebook
    print("\n***************PHONEBOOK LIST****************")
    for i in range(0, len(phonebookList), 1):
        print(i+1, end = ". ") #numbers each contact listed
        print("Name:", phonebookList[i].name, end = ", ")
        print("Number:", phonebookList[i].phonenumber)
        
        
 #Test Cases  
addContact("Keshon", 3498172)
findContact("Keshon", 3498172)
addContact("Paul Rosen", 40533617)
printphoneBook()
print(removeContact("Keshon", 3498162))
printphoneBook()
print(size())
findNumber("Keshon")
findName(3498162)
findName(40533617)
