###############################################################################
# Name: Dax Henson
# Date: 2017/02/09
# Description: Solves problems 9, 10, 11, and 12 of Project Euler.
###############################################################################
from math import sqrt


def problem9():
    found = False
    for a in xrange(1000 / 3):
        for b in xrange(a, 500):
            c = 1000 - a - b
            if (a * a + b * b == c * c and a + b + c == 1000):
                print "{}, {}, {}".format(a, b, c)
                found = True
                break
        if (found is True):
            break

    return a * b * c


def isPrime(n):               # checks if n is prime
    if n % 2 == 0 and n > 2:  # pre-empts even numbers greater than two
        return False          # checks if n is evenly divisible by any number
    return all(n % i for i in xrange(3, int(sqrt(n)) + 1))


def problem10():
    sum = 2
    i = 3
    while (i < 2000000):
        if isPrime(i):
            sum += i
        i += 2
    return sum


def problem10():
    sum = 2
    i = 3
    while (i < 2000000):
        if isPrime(i):


def problem11():
    pass


def problem12():
    pass


# the main part of the program
sol9 = problem9()
print "The product of the Pythagorean triple that sums to 1000 "\
      "is {}".format(sol9)
sol10 = problem10()
print "The difference between the sum of squares and square of sum of the "\
      "first 100 natural numbers is {}".format(sol10)
sol11 = problem11()
print "The 10,001st prime number is {}".format(sol11)
sol12 = problem12()
print "The greatest product of thirteen adjacent digits is {}".format(sol12)
