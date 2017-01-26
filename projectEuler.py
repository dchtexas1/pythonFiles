###############################################################################
# Name: Dax Henson
# Date: 2017/01/20
# Description: Solves problems 1 and 2 of Project Euler.
###############################################################################


# solves problem 1
def problem1():
    sum1 = 0
    for i in xrange(1000):              # looks at every number up to 1000 and
        if (i % 3 == 0 or i % 5 == 0):  # checks if they are multiples of 3 | 5
            sum1 += i                   # to determine if they should be summed
    return sum1


# solves problem 2
def problem2():
    n = 1
    m = 0
    tmp = 0
    sum2 = 0
    for x in xrange(51):
        if (n < 4000000):               # adds two numbers together, and then
            tmp = n                     # increments the numbers by the
            n += m                      # fibonacci sequence and checks if they
            m = tmp                     # are multiples of 2 (even). if they
            if (n % 2 == 0):            # are, they will be summed together
                sum2 += n
        else:
            break
    return sum2


# the main part of the program
sol1 = problem1()
print "The sum of all the multiples of 3 or 5 below 1000 is {}".format(sol1)
sol2 = problem2()
print "The sum of the even-valued Fibonacci terms " \
    "not exceeding four million is {}".format(sol2)
