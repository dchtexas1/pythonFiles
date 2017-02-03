###############################################################################
# Name: Dax Henson
# Date: 2017/02/3
# Description: Solves problems 3 and 4 of Project Euler
###############################################################################
'''
I ended up using essentially the same math to determine the largest prime
factor, but in the commented function, the control flow is such that I
usually increment the divisor and /then/ check for primality instead of
only incrementing when I cannot divide any more.

The commented function is less efficient because it has to check the primality
of every number while the uncommented function only has to divide until it
can't divide anymore.

I used http://www.pythontutor.com/visualize.html#mode=edit to show how many
steps each script goes through. It cannot exceed 1000 steps, but with smaller
numbers, like 5451000, the commented function took 272 steps, but the
uncommented function took a mere 93 steps.
'''

# solves problem 3
'''
from math import sqrt


def isPrime(n):               # checks if n is prime
    if n % 2 == 0 and n > 2:  # pre-empts even numbers greater than two
        return False          # checks if n is evenly divisible by any number
    return all(n % i for i in xrange(3, int(sqrt(n)) + 1))


def problem3(n):
    factor = 0
    i = 2
    while (i < n):
        if (isPrime(i) is True and n % i == 0 and i >= factor):
            factor = i
            n /= i
        elif(i == 2):             # math is the same as the function below
            i += 1                # the only difference is that this function
        else:                     # calls isPrime() and uses an if statement
            i += 2                # instead of a while statement, which is
        if (i * i > n and n > 1): # slightly fewer steps if calling isPrime()
            factor = n
            break
    return factor


'''
# '''


def problem3(n):
    factor = 0
    i = 2
    while (n > 1):
        while (n % i == 0):        # continuously divides n and adds the
            factor = i             # divisor to the factor list
            n /= i                 # until n is no longer evenly divisible
        if (i == 2):
            i += 1                 # in which case it will increment i to the
        else:                      # next prime
            i += 2
        if (i * i > n and n > 1):  # prevents the loops from passing sqrt(n)
            factor = n             # and sets factor equal to n, which is
            break                  # necessarily larger than any prior factor
    return factor


# '''
# solves problem 4
def canFlip(n):
    if (str(n) == str(n)[::-1]):  # determines if n matches its mirror image
        return True               # (reversed() works too, but is more verbose)


def problem4():
    pal = 0
    for i in xrange(100, 1000):
        for j in xrange(100, 1000):
            p = i * j
            if (canFlip(p) is True and pal < p):  # pal is only altered if the
                pal = p                           # product exceeds current pal
            if (i == 999 and j == 999):
                return pal                        # ends the sequence


# the main part of the program
sol3 = problem3(600851475143)
print "The largest prime factor of the number 600851475143 is {}".format(sol3)
sol4 = problem4()
print "The largest palindrome made from the product of two 3-digit numbers is"\
    " {}".format(sol4)
