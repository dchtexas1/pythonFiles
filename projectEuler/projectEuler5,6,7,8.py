###############################################################################
# Name: Dax Henson
# Date: 2017/02/09
# Description: Solves problems 5, 6, 7, and 8 of Project Euler.
###############################################################################
from math import sqrt
from fractions import gcd
# PLEASE NOTE THAT ALL INLINE COMMENTS ARE REFERENCING THE LINE BELOW THEM


# solves problem 5
'''
I noticed that the "smallest positive number that is evenly divisible" is the
same as "least common multiple," which is equal to the product of two numbers
divided by the greatest common divisor of the two. So I used fraction.gcd()

lambda allows me to use small functions without defining them, and reduce()
lets me repeatedly find the least common multiple of the given range.
'''


def problem5():
    return reduce(lambda x, y: x * y / gcd(x, y), xrange(1, 21))


# solves problem 6
'''
It's simple math. I'm just looking for the sum of the natural numbers and the
the sum of the squared natural numbers, up to a target number, in this case
100. Then I square the sum of natural numbers and subtract the sum of the
squares from it.
'''


def problem6():
    # sets target max number
    n = 100
    # sum of natural numbers formula, squared
    sns = ((n * (n + 1)) / 2) * ((n * (n + 1)) / 2)
    # sum of squared natural numbers formula
    ssn = (n * (n + 1) * (2 * n + 1)) / 6
    # finds the difference
    return sns - ssn


# solves problem 7
'''
It just runs through and checks all of the odd numbers (two is already counted)
for primality with a helper function. The helper function skips the base cases
of any number less than two and any even number, since the main function begins
at three and increments i by two.
'''


def isPrime(n):
    for i in xrange(3, int(sqrt(n)) + 1):
        # if n is evenly divisible by a natural number, it is not prime.
        if n % i == 0:
            return False
            break
    return True


def problem7():
    # number to check
    i = 1
    # tracks how many primes have been found
    primes = 1
    while (primes < 10001):
        # must be before primality check or i will go too far
        i += 2
        if (isPrime(i) is True):
            primes += 1
    return i


# solves problem 8
'''
The function travels through the string and multiplies each digit within each
instance of 13 characters not containing zero and then returns the largest
product.
'''


def problem8():
    string = "73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"
    # tracks the largest product of 13 characters
    finalProduct = 1
    for i in xrange(0, len(string) - 13):
        # ignores all zeros in every slice of 13 characters
        if ("0" not in string[i:i + 13]):
            # creates a variable to easier manipulate the current 13 characters
            window = string[i:i + 13]
            # tracks the product of the current window
            product = 1
            # runs through and multiplies each digit in the window
            for j in xrange(0, len(window)):
                product *= int(window[j])
            if (product > finalProduct):
                finalProduct = product

    return finalProduct


# the main part of the program
sol5 = problem5()
print "The smallest positive number that is evenly divisible by all of the "\
    "numbers from 1 to 20 is {}".format(sol5)
sol6 = problem6()
print "The difference between the sum of squares and square of sum of the "\
    "first 100 natural numbers is {}".format(sol6)
sol7 = problem7()
print "The 10,001st prime number is {}".format(sol7)
sol8 = problem8()
print "The greatest product of thirteen adjacent digits is {}".format(sol8)
