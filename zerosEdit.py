###############################################################################
# Name: Dax Henson
# Date: 2016/01/11
# Description: Calculates the number of zeros written from 1 to 1000000.
###############################################################################
n = 0
count = 0                           # initializes variables


def numZeros():                     # counts number of zeros in current number
    n1 = n                         # duplicates number to avoid dividing n
    zeros = 0                       # resets zeros before counting each number
    while (n1 != 0):
        if (n1 % 10 == 0):         # checks if divisible by 10
            zeros += 1
        n1 /= 10                   # moves one decimal place to the left
    return zeros


while (n < 1000000):                # defines upper bound
    n += 1
    count = count + numZeros()
else:
    print "The number of zeros written from 1 to " \
          "1 million is {}.".format(count)
