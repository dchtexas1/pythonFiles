"""Displays an input quadratic function in standard form."""


def f(x):
    """Returns the y value for a certain x value in the input function."""
    return a * x ** 2.0 + b * x + c


a = input("Leading coefficient: ")
b = input("Second coefficient: ")
c = input("Constant: ")
print "Your quadratic function is f(x)={}x^2 + {}x + {}".format(a, b, c)
h = ((-b) / (2.0 * a))
k = f(h)
print "Your function in standard form is f(x)={}(x-{})^2+{}".format(a, h, k)

quartNum = input("How many quarters will you give me? ")
dollars = quartNum / 4.0
if quartNum == 0:
    print("I wish you had given me a quarter...")
else:
    print("I have " + str(quartNum) + " quarters!")
    if dollars != 1.0:
        print("That is " + str(dollars) + " dollars!")
    else:
        print("That is " + str(dollars) + " dollar!")
    print("Thank you!")
