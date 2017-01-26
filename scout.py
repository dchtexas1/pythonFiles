"""For Zane Hixon."""
import time
p = "might be"
q = "might be"
r = "might be"
s = "good"


class person(object):
    """defines people"""

    def __init__(self):
        super(person, self).__init__()

    def displayPerson(self):
        print "      Your name is : ", self.name
        print "    Your gender is : ", self.gender
        print "Your appearance is : ", self.appear
        print ("\nYou {} annoying.".format(p))
        print ("You {} cared for.".format(q))
        print ("You {} a {} significant other.".format(r, s))

    def loved(self):
        # The gender thing can sound wierd bc of Agender (no gender),
        # but None means null set in python. It's a programming thing.
        if ((self.name is not None) and (self.gender is not None)):
            x = 1
        if ((self.appear is not None) and (self.annoying is not None)):
            y = 1
        if ((x == 1) and (y == 1)):
            print ("\nI love you. It doesn't matter what attributes you have.")


gf = person()
dating = raw_input("Are you dating Dax?\n[y/n] ")


if (dating == "y"):
    gf.name = raw_input("\nWhat is your name?\n").capitalize()
    gf.gender = raw_input("\nWhat is your gender?\n").capitalize()
    gf.appear = raw_input("\nDescribe how attractive you are:\n").capitalize()
    gf.annoying = raw_input("\nAre you annoying?\n")
    if (gf.annoying.startswith("y")):
        p = "are"
    else:
        p = "are not"
    gf.caredFor = raw_input("\nDo people care about you?\n")
    if (gf.caredFor.startswith("n")):
        q = "are not"
    else:
        q = "are"
    gf.goodGF = raw_input("\nAre you a good significant other?\n")
    if (gf.goodGF.startswith("n")):
        r = "are not"
    else:
        r = "are"
    message = raw_input("\nWould you like a message from Dax?\n[y/n] ")
    a = "\n\"When you answered those questions, you added attributes to a "
    b = "digital version of yourself.\"\nThe following is the version you "
    c = "entered:\n"
    d = "\nThis is the correct version, which I see:\n"
    if (message == "y"):
        print(a + b + c)
        time.sleep(3)
        gf.displayPerson()
        if (gf.annoying != "No"):
            setattr(gf, 'annoying', "No")
            p = "are not"
        if (gf.appear != "Very pretty"):
            setattr(gf, 'appear', "Very pretty; Beautiful even")
        if (gf.caredFor != "Yes"):
            setattr(gf, 'caredFor', "Yes")
            q = "are"
        if (gf.goodGF != "Yes"):
            setattr(gf, 'goodGF', "Yes")
            r = "are"
            s = "wonderful"
        time.sleep(20)
        print(d)
        time.sleep(1)
        gf.displayPerson()
        time.sleep(15)
        gf.loved()
        time.sleep(60)


else:
    print("This program is not for you.")
