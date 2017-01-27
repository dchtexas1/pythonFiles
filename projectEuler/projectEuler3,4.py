###############################################################################
# Name: Dax Henson
# Date: 2017/01/2x
# Description: Solves problems 3 and 4 of Project Euler
###############################################################################
from math import sqrt
# it may help to make use of some math functions (which you can import)
# it may also help to define other "helper" functions (i.e., delegate tasks!)


def isPrime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in xrange(3, int(sqrt(n)) + 1))


def canFlip(n):
    if (str(n) == str(n)[::-1]):  # determines if the number equals its mirror
        return True               # (reversed() works too, but is more verbose)


# solves problem 3
def problem3(num):
    factors = []
    n = 2
    while (num > 1):
        while (num % n == 0):
            factors.append(n)
            num /= n
        if (n == 2):
            n += 1
        else:
            n += 2
        if (n * n > num):
            if (num > 1):
                factors.append(num)
            break
    if (isPrime(max(factors)) is True):
        return max(factors)
    else:
        return "something, right? What did you do?? You broke it!"


# solves problem 4
def problem4():
    pal = 0
    for i in xrange(100, 1000):
        for j in xrange(100, 1000):
            p = i * j
            if (canFlip(p) is True and pal < p):  # palindrome is only altered
                pal = p                           # if the product is larger
            if (i == 999 and j == 999):
                return pal                        # ends the sequence


# the main part of the program
sol3 = problem3(600851475143)
print "The largest prime factor of the number 600851475143 is {}".format(sol3)
sol4 = problem4()
print "The largest palindrome made from the product of two 3-digit numbers is"\
    " {}".format(sol4)
