import math

operatorChoice = input("Please input the operator (add/subtract/multiply/divide):\n").upper()

if operatorChoice == "ADD" or operatorChoice == "SUBTRACT" or operatorChoice == "MULTIPLY" or operatorChoice == "DIVIDE": #check if it is valid
    operatorCheck = True
else: 
    operatorCheck = False

numberOne = input("Input the first number:\n")
numberTwo = input("Input the second number:\n")
numberCheck = None

if (numberOne.isnumeric() == True or numberOne.isdecimal() == True) and (numberTwo.isnumeric() == True or numberTwo.isdecimal() == True):
    numberCheck == True
else:
    numberCheck == False


while operatorCheck == False:
    print("Please re-input your operator.")
    operatorChoice = input("Please input the operator (add/subtract/multiply/divide):\n").upper()
    
    if operatorChoice == "ADD" or operatorChoice == "SUBTRACT" or operatorChoice == "MULTIPLY" or operatorChoice == "DIVIDE": #recheck so loop isn't infinite
        operatorCheck = True
    else: 
        operatorCheck = False


while numberCheck == False:
    print("Please re-input your numbers.")
    numberOne = input("Input the first number:\n")
    numberTwo = input("Input the second number:\n")

    if (numberOne.isnumeric() == True or numberOne.isdecimal() == True) and (numberTwo.isnumeric() == True or numberTwo.isdecimal() == True): #recheck for loop
        numberCheck == True
    else:
        numberCheck == False


#THE MAGIC

if operatorChoice == "ADD" :                        
    solution = float(numberOne) + float(numberTwo)
    print(numberOne, "+", numberTwo, "=", solution)

elif operatorChoice == "SUBTRACT" :
    solution = float(numberOne) - float(numberTwo)
    print(numberOne, "-", numberTwo, "=", solution)

elif operatorChoice == "MULTIPLY" :
    solution = float(numberOne) * float(numberTwo)
    print(numberOne, "*", numberTwo, "=", solution)

elif operatorChoice == "DIVIDE" :
    solution = float(numberOne) / float(numberTwo)
    print(numberOne, "/", numberTwo, "=", solution)

