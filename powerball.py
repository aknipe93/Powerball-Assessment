#----------------------------------------------------------
# Powerball story
# Alexander Knipe
#
# As a Greenphire employee I would like to add my favorite 6
# numbers to consider for a Powerball entry ticket so that I
# can win 1 billion dollars.
#
# How it works
# 1) Run the program
# 2) Follow the prompts to fill in you info
# 3) If you want to add another employee type "y"
#    If not type anything eles
# 4) Review the employees and their picks
# 5) View the winning number
#
#-----------------------------------------------------------

from collections import Counter
from random import randint

# Global lists
employeeList = [] # keeps track of employees and their picks
numbersList = []  # keeps track of all the numbers chosen

# Filters out the unique numbers and stores them as a key
# in a dictionary with its value the amount of occurrences
def occurrences():
    return Counter(numbersList)

# Prints the winning number.
# If only 5 unique number are used
# (powerball number is same as one of the first 5)
# add a random number between 1 and 69 to the end
def printWinningList(list):
    print "Powerball winning number:"
    if len(list) < 6:
        x = str(randint(1,69))
        list.insert(0,x)
    print list[4] + " " +  list[3] + " " +  list[2] + " " +  list[1] + " " +  list[0] + " Powerball: " + list[5]

# Determins the winning number by sorting the unique numbers by how many
# occurrences and chooses the top 6 most used numbers.
# The most used number is the powerball and the other 5 numbers are in order
# in descending order of occurrence
def powerBallWinning():
    finalList = []
    numberOccur = occurrences();
    sorted_x = sorted(numberOccur, key=numberOccur.get)
    for key in sorted_x:
        finalList.append(key)
    printWinningList(finalList[-6:])

# User input for the powerball number
# checks to make sure user input is within the range
def powerBallNumber():
     y = int(raw_input("select Power Ball # (1 thru 26):"))
     min=1
     max=26
     if y >= 0 and y <= 26:
         return str(y)
     else:
         print "Sorry you entered a number out of thr range"
         return powerBallNumber()



# User input for the first five numbers
# Checks to make sure that the numbers are within range and not duplicates
def firstFive(text, numbers):
    if len(numbers) > 0:
        num = "excluding "
    else:
        num = ""
    numInList = len(numbers);
    k = 0;
    for i in numbers:
        k = k + 1
        if k >= numInList and k<>1:
            num = num + ' and ' + str(i)
        else:
            num = num + str(i) + ","

    text2 = text + " " + num +")"
    x = int(raw_input(text2))
    min = 0
    max = 69
    if (str(x) in numbers):
        print "Sorry you entered a number you already used"
        return firstFive(text ,numbers)
    elif x >= min and x <= max:
        return str(x);
    else:
        print "Sorry you entered a number out of bounds"
        return firstFive(text, numbers)

# Prints the employee's name and their chosen number
def printEmployees():
    for i in employeeList:
        numStr = ''
        for num in i['number']:
            numStr = numStr + ' ' +num
        print i['name'] + " " + numStr + " Powerball: " + i['powerball']

# Main function prompting the user inputs, saving the user data,
# saving the numbers chosen, giving the option to add another employee,
# and starting the function to pick the winning number
def enterEmployee():
    firstName   = raw_input("Enter your first name: ")
    lastName    = raw_input("Enter your last name: ")
    numbers = []
    firstNumber = firstFive("select 1st # (1 thru 69 ", numbers)
    numbersList.append(firstNumber)
    numbers.append(firstNumber)

    secondNumber = firstFive("select 2nd # (1 thru 69 ", numbers)
    numbersList.append(secondNumber);
    numbers.append(secondNumber);

    thirdNumber = firstFive("select 3rd # (1 thru 69 ", numbers)
    numbersList.append(thirdNumber);
    numbers.append(thirdNumber);

    fourthNumber = firstFive("select 4th # (1 thru 69 ", numbers)
    numbersList.append(fourthNumber);
    numbers.append(fourthNumber);

    fifthNumber = firstFive("select 5th # (1 thru 69 ", numbers)
    numbersList.append(fifthNumber);
    numbers.append(fifthNumber);

    powerball = powerBallNumber();
    numbersList.append(powerball);

    name = firstName + " " + lastName
    employeeList.append({'name': name, 'number':numbers, 'powerball': powerball})
    nextEmployee = raw_input("Enter another employee? (Y/n)")
    if nextEmployee == "y" or nextEmployee == "Y":
        enterEmployee()
    else:
        printEmployees()
        powerBallWinning()



# calling the starting function
enterEmployee()