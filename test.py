def problem3(n):
    factor = []
    for i in xrange(1, int(n**0.5)+1):
        if (n % i == 0):
            factor.extend([i, n / i])
    return factor


def problem12():
    factors = []
    tnum = 0
    num = 1
    while len(factors) < 500:
        tnum += num
        num += 1
        factors = problem3(tnum)
    return tnum


print problem12()
