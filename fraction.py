###############################################################################
# Name: Dax Henson
# Date: 2017/02/19
# Description: Implements a fraction class.
###############################################################################


class Fraction(object):
    # constructs the fraction and its values
    # fractions are 0/1 by default

    def __init__(self, num=0, den=1):
        self.num = num
        # prohibits 0 from being the denominator by changing it to 1
        if (den == 0):
            den = 1
        self.den = den

    # getters and setters for the numerator and denominator values
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value

    @property
    def den(self):
        return self._den

    # this setter will not allow zero to be set as a value for the denominator
    @den.setter
    def den(self, value):
        if (value != 0):
            self._den = value

    # reduces a fraction to lowest terms
    def reduce(self):
        gcd = 1
        # finds the highest possible GCD
        low = min(self.num, self.den)

        # find common divisors
        for i in range(2, low + 1):
            # updates GCD upon finding a common divisors
            if (self.num % i == 0 and self.den % i == 0):
                gcd = i

        # divides the numerator and denominator by GCD
        self.num /= gcd
        self.den /= gcd

        # if the numerator is 0, the denominator becomes 1
        if (self.num == 0):
            self.den = 1

    # finds the sum of two fractions
    def __add__(self, other):
        num = (self.num * other.den) + (other.num * self.den)
        den = self.den * other.den
        sum = Fraction(num, den)
        sum.reduce()

        return sum

    # finds the difference of two fractions
    def __sub__(self, other):
        num = (self.num * other.den) - (other.num * self.den)
        den = self.den * other.den
        sum = Fraction(num, den)
        sum.reduce()

        return sum

    # finds the product of two fractions
    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        product = Fraction(num, den)
        product.reduce()

        return product

    # finds the quotient of two fractions
    def __div__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        quotient = Fraction(num, den)
        quotient.reduce()

        return quotient

    # returns the fraction as a decimal value
    def getReal(self):
        return float(self.num) / self.den

    # returns the fraction and it's decimal equivalent as a string
    def __str__(self):
        self.reduce()
        return "{}/{} ({})".format(self.num, self.den, self.getReal())


# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
# create some fractions
f1 = Fraction()
f2 = Fraction(5, 8)
f3 = Fraction(3, 4)
f4 = Fraction(1, 0)

# display them
print "f1:", f1
print "f2:", f2
print "f3:", f3
print "f4:", f4

# play around
f3.num = 5
f3.den = 8
f1 = f2 + f3
f4.den = 88
f2 = f1 - f1
f3 = f1 * f1
f4 = f4 / f3

# display them again
print
print "f1:", f1
print "f2:", f2
print "f3:", f3
print "f4:", f4
