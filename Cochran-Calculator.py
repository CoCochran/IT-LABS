#Connor Cochran
#11/6/2022
#Cochran-Calculator.py

operatorChoice = input("Please input the operator (add/subtract/multiply/divide):\n").upper()

if operatorChoice == "ADD" or operatorChoice == "SUBTRACT" or operatorChoice == "MULTIPLY" or operatorChoice == "DIVIDE": #check if it is valid
    operatorCheck = True
else: 
    operatorCheck = False

numberOne = input("Input the first number:\n")
numberTwo = input("Input the second number:\n")



while operatorCheck == False:
    print("Please re-input your operator.")
    operatorChoice = input("Please input the operator (add/subtract/multiply/divide):\n").upper()
    
    if operatorChoice == "ADD" or operatorChoice == "SUBTRACT" or operatorChoice == "MULTIPLY" or operatorChoice == "DIVIDE": #recheck so loop isn't infinite
        operatorCheck = True
    else: 
        operatorCheck = False


def checkNumber(One, Two): # This guy is a genius, smartest human being to ever live >>> https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-represents-a-number-float-or-int
    try:
        float(One)
        float(Two)
        return True
    except ValueError:
        return False

checkNumber(numberOne, numberTwo)
while checkNumber(numberOne, numberTwo) == False:
    print("Please re-input your numbers.\n")
    numberOne = input("Input the first number:\n")
    numberTwo = input("Input the second number:\n")
    checkNumber(numberOne, numberTwo)



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


