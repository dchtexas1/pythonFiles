###############################################################################
# Name: Dax Henson
# Date: 2017/02/09
# Description: Solves problems 5, 6, 7, and 8 of Project Euler.
###############################################################################
from math import sqrt
from fractions import gcd
# it may help to make use of some math functions (which you can import)
# it may also help to define other "helper" functions (i.e., delegate tasks!)


# solves problem 5
def problem5():
    return reduce(lambda x, y: x * y / gcd(x, y), xrange(1, 21))


# solves problem 6
def problem6():
    # sets target max number
    n = 100
    # sum of natural numbers formula
    sn = (n * (n + 1)) / 2
    # sum of squared natural numbers formula
    sns = (n * (n + 1) * (2 * n + 1)) / 6
    return sn * sn - sns


# solves problem 7
def isPrime(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    else:
        for i in xrange(3, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
                break
        return True


def problem7(targ):
    i = 1
    primes = 1
    while (primes < targ):
        i += 2
        if (isPrime(i) is True):
            primes += 1
    return i


# solves problem 8
'''

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
    finalProduct = 1
    for i in xrange(0, len(string) - 13):
        if ("0" not in string[i:i + 13]):
            window = string[i:i + 13]
            product = 1
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
sol7 = problem7(10001)
print "The 10,001st prime number is {}".format(sol7)
sol8 = problem8()
print "The greatest product of thirteen adjacent digits is {}".format(sol8)
