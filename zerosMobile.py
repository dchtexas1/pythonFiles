def findOccurrence (s, ch):
    return ([i for i, letter in enumerate(s) if letter == ch])


n = 0
count = 0
while (n < 1000000):
    n += 1
    count = count + len(findOccurrence(str(n), "0"))
else:
    print ("The number of zeros written from 1 to 1 million is {}.".format(count))
