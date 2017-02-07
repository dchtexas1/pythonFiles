class frac(object):
    def __init__(self, n=0, d=1):
        self._n = n
        if (d == 0):
            print "Cannot divide by zero; changed to one."
            d = 1
        self._d = d

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, value):
        self._n = value

    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, value):
        if (value != 0):
            self._d = value

    def getReal(self):
        return float(self.n) / self.d

    def reduce(self):
        gcd = 1
        targ = self.n
        for i in xrange(2, targ + 1):
            if (self.n % i == 0 and self.d % i == 0):
                gcd = i
        self.n /= gcd
        self.d /= gcd

    def add(self, frac):
        new_n = self.n * frac.d + frac.n * self.d
        new_d = self.d * frac.d
        new_frac = frac(new_n, new_d)
        return new_frac

    def subtract(self)
        new_frac = 

    def __str__(self):
        self.reduce()
        return "{}/{} ({})".format(self.n, self.d, self.getReal())


# main
f1 = frac()
f2 = frac(1, 2)
f3 = frac(2, 3)
f4 = frac(6, 2)

print f1
print f2
print f3
print f4
