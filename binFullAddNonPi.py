######################################################################
# Name: Dax Henson
# Date:
# Description: Finds the binary sum of two binary numbers
######################################################################
from random import randint  # allows us to generate random integers


# function that randomly generates an 8-bit binary number
def setNum():
    # create an empty list to represent the bits
    num = []
    # generate eight random bits
    for i in range(0, 8):
        # append a random bit (0 or 1) to the end of the list
        num.append(randint(0, 1))
    return num


# function that implements a full adder using two half adders
# inputs are Cin, A, and B; outputs are S and Cout
def fullAdder(Cin, A, B):
    # first half adder
    S0 = A ^ B
    C0 = A & B
    # second half adder
    S = Cin ^ S0
    C1 = Cin & S0
    # OR statement
    Cout = C0 | C1
    return S, Cout


# controls/drives the addition of each 8-bit number to produce a sum
def calculate(num1, num2):
    Cout = 0  # the initial Cout is 0
    sum = []  # initialize the sum
    n = len(num1) - 1  # the position of the right-most bit of num1
    # step through each bit, from right-to-left
    while (n >= 0):
        # isolate A and B (the current bits of num1 and num2)
        A = num1[n]
        B = num2[n]
        # set the Cin (as the previous half adder's Cout)
        Cin = Cout
        # call the fullAdder function that takes Cin, A, and B...
        # ...and returns S and Cout
        S, Cout = fullAdder(Cin, A, B)
        # insert the sum bit, S, at the beginning (index 0) of sum
        sum.insert(0, S)
        # go to the next bit position (to the left)
        n -= 1
    # insert the final carry out at the beginning of the sum
    sum.insert(0, Cout)
    return sum


# get a random num1 and display it to the console
num1 = setNum()
print "     ", num1
# get a random num2 and display it to the console
num2 = setNum()
print "+    ", num2
# calculate the sum of num1 + num2 and display it to the console
sum = calculate(num1, num2)
print "= ", sum
# wait for user input before exiting
raw_input("Press ENTER to terminate")
raise SystemExit
