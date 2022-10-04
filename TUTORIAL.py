#List of all the variables ranging from Integers to Strings
title = "Welcome to the Pointers & References in C++ Tutorial!!"
explanation1 = "-Explanation-"
explanation2 = "-Explanation-"
pagenumber = 1
pagenumber2 = 2
pagenumber3 = 3
grade1 = 50
grade2 = 100
#The values for the if statements on whether the user got the answer right or wrong
reference_answer = "int& newNumber = myNumber"
pointer_answer_1 = "int* pHandle;"
pointer_answer_2 = "pHandle = &myName;"

import time

#List and Dictionary setup below 
list = ["Reference Code", "Pointers Code", "cout <<", "*", "&", "p()", "&()", ]

#Dictionary - need to separate keys and values by key: value then "," between each set
refpointdict = {
    "Declare": "variable* p(name of pointer)",
    "Assign": "p(pointer name) = &(variable name)",
    "cout": "prints to screen",
    "cin": "takes user input",
    "Answer1": "int& newNumber = myNumber",
    "Answer2": "int* pHandle;",
    "Answer3": "pHandle = &myName;"
}


#Prints mostly words and sentences 
#Prints the string variable for Title 
print(title)
print("Today you will learn about Pointers and References in C++")
print("Both of them are relatively similar but work differently or coded differently")
print("They basically reference or point to a variable that has been declared")
print("You can then use this pointer/reference in place of the variable throughout the code.")
print("Below, you will see how each is coded and how they work...")

#Prints a blank line. Almost like hitting enter in a word document to organize lines better and create spaces
print()
print(list[0])
print("int myAge = 26; //Int variable for an age or number")
print("int& tylerAge = myAge; //This is the reference line")
print("cout << tylerAge;")
print("The program will output 26")
print()
print(explanation1)
print("You have to use & after the variable type to initialize the reference")
print("Then create a name for the reference following that")
print("Then = the variable you want it to reference")
print("Now, going forward, you can use tylerAge in place of myAge")
print()

#This starts the input process of letting the user know what they need to input and giving them a space to input what they want
print("Your Turn: Create a reference for the int variable given below...")
print("int myNumber = 73 with reference name newNumber")
user_answer = input()
if user_answer == reference_answer:
    print("GREAT, YOU GOT IT!!")
    #Prints a piece of the dictionary to show the user what they got right exactly
    print(refpointdict["Answer1"])
    #Creates a pause for 3 seconds to show the player the answer to confirm what they did is right
    time.sleep(3) 
else:
    print("That's Not It, Sorry.")
    
print()
print(list[1])
print("int* pYear; //Declare the Pointer")
print("int year = 1996; //Create the variable for the pointer")
print("pYear = &year; //Assign Pointer")
print("cout << pYear;")
print("The program will output 1996")
print()
print(explanation2)
print("When you declare the pointer, you need to put an * after the variable type")
print("Create the variable you want to point to")
print("When you assign the variable to the pointer, you have to put a P before the pointer name, hence, Pointer")
print("You have to put & before the variable name to assign it to the pointer")
print("Pointer's require a little more action to assign a variable to it")
print("There are also something called addresses but we can tackle that in another tutorial")
print()
print("Your Turn: Create a Pointer for the string variable given below...")
print("string myName = 'Tyler' with pointer name handle")
print("First, Declare the pointer: ")
user_answer = input()

#If statement to determine if the user is right or wrong
#Added the dictionary lookups to show the user what they got right exactly 
if user_answer == pointer_answer_1:
    print("GREAT, YOU GOT IT!!")
    print(refpointdict["Answer2"])
    time.sleep(3)
else:
    print("So Close!! Try Aain.")
print("Second, Assign the Pointer: ")
user_answer = input()
if user_answer == pointer_answer_2:
    print("GREAT, YOU GOT IT!")
    print(refpointdict["Answer3"])
    time.sleep(3)
else:
    print("That's Not It, Sorry.")


#More input for the user to tell the system what their grade was and how they did and then getting some feedback
print("How did you do with the two questions?")
print("What was your grade?", grade1, "or", grade2)
input()
print("EXCELLENT!!")
print("Hope you enjoyed this short tutorial on References and Pointers in C++")
print("We'll See You Next Time!!")
print()
print("Go Again?")

#This prints the Page as well as all the page numbers from the integer variables 
print("Page:", pagenumber, pagenumber2, pagenumber3)
