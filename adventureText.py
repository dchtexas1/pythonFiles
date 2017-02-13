###############################################################################
# Name: Dax Henson
# Date: 2017/02/12
# Description: Adventure Text Game
###############################################################################
# imports sleep for use in trap()
from time import sleep
###############################################################################
# the blueprint for a room


class Room(object):
    # the constructor

    def __init__(self, name):
        # rooms have a name, exits, exit locations, items, item Descs
        # and grabbables (things that can be taken into inventory)
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescs = []
        # hidden items are the same as items, but don't show up in room.__str__
        self.hiddenItems = []
        self.hiddenItemDescs = []
        self.grabbables = []
        # grabbables have descriptions now
        self.grabbableDescs = []
        # interactables are like items with binary state and require grabbables
        self.interactables = []
        self.interactableDescs = []
        self.interactableState = []
        self.interactableReqs = []

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescs(self):
        return self._itemDescs

    @itemDescs.setter
    def itemDescs(self, value):
        self._itemDescs = value

    @property
    def hiddenItems(self):
        return self._hiddenItems

    @hiddenItems.setter
    def hiddenItems(self, value):
        self._hiddenItems = value

    @property
    def hiddenItemDescs(self):
        return self._hiddenItemDescs

    @hiddenItemDescs.setter
    def hiddenItemDescs(self, value):
        self._hiddenItemDescs = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    @property
    def grabbableDescs(self):
        return self._grabbableDesc

    @grabbableDescs.setter
    def grabbableDescs(self, value):
        self._grabbableDesc = value

    @property
    def interactables(self):
        return self._interactables

    @interactables.setter
    def interactables(self, value):
        self._interactables = value

    @property
    def interactableDescs(self):
        return self._interactableDescs

    @interactableDescs.setter
    def interactableDescs(self, value):
        self._interactableDescs = value

    @property
    def interactableState(self):
        return self._interactableState

    @interactableState.setter
    def interactableState(self, value):
        self._interactableState = value

    @property
    def interactableReqs(self):
        return self._interactableReqs

    @interactableReqs.setter
    # interactables are set to on by default
    def interactableReqs(self, value="on"):
        self._interactableReqs = value

    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)

    # This is code I would like to implement in the future, for doors
    # def delExit(self, exit, room):
    #    self._exits.remove(exit)
    #    self._exitLocations.remove(room)

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate lists
        self._items.append(item)
        self._itemDescs.append(desc)

    def addHiddenItem(self, item, desc):
        self._hiddenItems.append(item)
        self._hiddenItemDescs.append(desc)

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item, desc):
        # append the item to the list
        self._grabbables.append(item)
        self._grabbableDesc.append(desc)

    # removes a grabbable item from the room
    # the item is a string (e.g., key)
    def delGrabbable(self, item, desc):
        # remove the item from the list
        self._grabbables.remove(item)
        self._grabbableDesc.remove(desc)

    def addInteractable(self, item, desc, state, reqs):
        self._interactables.append(item)
        self._interactableDescs.append(desc)
        self._interactableState.append(state)
        self._interactableReqs.append(reqs)

    # returns a string description of the room
    def __str__(self):
        # first, the room name
        # some room names require slightly different grammar
        if (currentRoom in [r0, r4, r5, r8, r9]):
            s = "You are {}.\n".format(self.name)
        else:
            s = "You are in {}.\n".format(self.name)

        # next, the items in the room
        s += "You see: "
        for item in self.items:
            s += item + " "
        # interactables are visible too
        for interactable in self.interactables:
            s += interactable + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "

        return s


###############################################################################
# creates the rooms
def createRooms():
    # some functions elsewhere need to check for these rooms
    global currentRoom, r0, r4, r5, r8, r9, r12

    # Generates all of the empty rooms
    # all the rooms have names instead of "Room n"
    r1 = Room("an office")
    r2 = Room("a library")
    r3 = Room("a sunroom")
    r4 = Room("at the top of a stairwell")
    r5 = Room("at the bottom of a stairwell")
    r6 = Room("a sitting room")
    r7 = Room("a kitchen")
    r8 = Room("at the top of a dark stairwell")
    r9 = Room("at the bottom of a stairwell, in a basement")
    r10 = Room("a basement")
    r11 = Room("a basement")
    r12 = Room("a basement")
    r0 = Room("outside")

    # generates the office
    r1.addExit("north", r2)
    r1.addExit("east", r3)
    # This keycard is used to change the state of the bomb
    r1.addGrabbable("keycard", "It is used to prove one's credentials.")
    r1.addItem("desk", "A modern desk, made of glass and carbon-fiber. "
               "There is a keycard on the desk\nbeside an inlaid terminal.")
    r1.addItem("chair", "It is smooth, black, and shiny.")
    r1.addItem("terminal", "The terminal glows an amber color. "
               "There is text on the screen.")
    # this text can be looked, but it doesn't show up in Room.__str__
    r1.addHiddenItem("text", "The terminal displays a draft of a message to "
                     "the separatist chancellor about\ntransporting a bomb "
                     "out of the basement.")

    # generates the library
    r2.addExit("south", r1)
    r2.addItem("rug", "It is awfully plush.")
    r2.addItem("bookshelves", "The bookshelves are neatly packed with books.\n"
               "One of the books is not flush with the others. It appears to "
               "be a journal.")
    # alas, I am a programmer, not an author
    r2.addGrabbable("journal", "\"Some poignant world-building.\"")

    # Generates a sunroom
    r3.addExit("north", r4)
    r3.addExit("west", r1)
    r3.addExit("south", None)
    r3.addItem("statue", "It has an oddly fascist feel to it... Perhaps it is "
               "because of the sieg heil pose.")
    r3.addItem("couch", "Rather plain, given the ornate statue nearby.")

    # generates a stairwell room
    r4.addExit("south", r3)
    # here we have "vertical movement" though technically there's no dimensions
    r4.addExit("down", r5)
    r4.addItem("stairwell", "There is some light downstairs, and an..."
               "interesting smell wafts through.")

    # generates a stairwell room
    r5.addExit("up", r4)
    r5.addExit("west", r6)
    r5.addItem("stairwell", "It's rather dark upstairs, now that your eyes "
               "have adjusted.")

    # generates a sitting room, with access to the outside
    r6.addExit("east", r5)
    r6.addExit("south", r7)
    r6.addExit("west", r0)
    r6.addItem("fireplace", "It is warm, but dying.")
    r6.addItem("coffee table", "It is littered with decorative pieces.")

    # generates a kitchen
    r7.addExit("north", r6)
    r7.addExit("east", r8)
    r7.addItem("oven", "There is an apple pie warming in it.")

    # generates another stairwell room
    r8.addExit("west", r7)
    r8.addExit("down", r9)
    r8.addItem("stairwell", "This stairwell is extremely deep.")

    # generates basement stairwell room
    r9.addExit("up", r8)
    r9.addExit("west", r10)
    r9.addExit("stairwell", "Returning to the surface will surely exhausting.")

    # generates extra basement room
    r10.addExit("east", r9)
    r10.addExit("north", r11)

    # generates extra basement room
    r11.addExit("south", r10)
    r11.addExit("east", r12)

    # generates a basement room with an interactive bomb requiring a keycard
    r12.addExit("west", r11)
    r12.addInteractable("bomb", "It must be deactivated to save the Alliance. "
                        "There is a card slot on the side.", "on", "keycard")

    # generates an room "outside." Of course, it's only outside bc I say so
    r0.addExit("east", r6)
    r0.addItem("trees", "The tree is devoid of leaves. This would lead you "
               "to assume that it is winter,\nexcept for the fact that it is "
               "hot enough to fry an egg.")
    r0.addItem("grass", "The grass is brown and dead.")

    # sets which room the user starts in
    currentRoom = r1


# displays an appropriate "message" when the player dies
# yes, this is intentionally obfuscated!
def death():
    print " " * 17 + "u" * 7
    print " " * 13 + "u" * 2 + "$" * 11 + "u" * 2
    print " " * 10 + "u" * 2 + "$" * 17 + "u" * 2
    print " " * 9 + "u" + "$" * 21 + "u"
    print " " * 8 + "u" + "$" * 23 + "u"
    print " " * 7 + "u" + "$" * 25 + "u"
    print " " * 7 + "u" + "$" * 25 + "u"
    print " " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 + "\"" + " " * 3 + "\"" + "$" * 6 + "u"
    print " " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7 + "$" * 4 + "\""
    print " " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" + "$" * 3
    print " " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3
    print " " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 + "$" * 3 + "u" * 2 + "$" * 4 + "\""
    print " " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7 + "\""
    print " " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u"
    print " " * 13 + "u$\"$\"$\"$\"$\"$\"$u"
    print " " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$" * 2 + " " * 7 + "u" * 3
    print " u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + " " * 7 + "u" + "$" * 4
    print " " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 + "\"" + " " * 5 + "u" * 2 + "$" * 6
    print "u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 + "u" * 4 + "$" * 10
    print "$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2 + "$" * 9 + "\"" * 3 + "$" * 3 + "\""
    print " " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 + " " + "\"" * 2 + "$" + "\"" * 3
    print " " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3
    print " " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 + " \"\"" + "$" * 11 + "u" * 3 + "$" * 3
    print " " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" * 11 + "\""
    print " " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" * 4 + "\"\""
    print " " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\""


# this is a slightly different way to die; still leads to death()
def trap():
    sleep(5)
    response = "The bomb starts ticking! Whoops!"
    print "\n{}".format(response)
    sleep(5)
    death()


###############################################################################
# START THE GAME!!!
createRooms()
inventory = []
# lets the inventory be looked, no matter which room you are in
inventoryDesc = []
# allows the user to input the first letter instead of the full direction
directions = ["north", "south", "east", "west", "up", "down"]
shortcuts = ["n", "s", "e", "w", "u", "d"]

while True:
    if (currentRoom is None):
        death()
        break

    # checks if the bomb state has been altered, thus killing you
    if (currentRoom == r12):
        if (currentRoom.interactableState[[i for i, j in enumerate(currentRoom.interactables) if j == 'bomb'][0]] == "off"):
            trap()
            break

    status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)

    print "=================================================================="\
          "============="
    print status

    action = raw_input("What do you want to do? ")
    action = action.lower()

    # allows the user to send blank input without a response being printed
    while (action == ""):
        action = raw_input("")
    else:
        response = "I don't understand. Try valid noun.\n"\
            "Valid verbs are:\n\nMovement: [go, head]\nSight:    [look, check]\n"\
            "Action:   [take, get] [use]"

    if (action in ["quit", "exit", "bye"]):
        break

    words = action.split()
    if (len(words) == 2):
        verb = words[0]
        noun = words[1]

        if (verb in ["go", "head"]):
            response = "Invalid exit"

            # expands shortcuts to the full direction for parsing
            if (noun in shortcuts):
                noun = directions[shortcuts.index(noun)]

            for i in range(len(currentRoom.exits)):
                if (noun == currentRoom.exits[i]):
                    currentRoom = currentRoom.exitLocations[i]

                    response = "Room changed."

                    break

        elif (verb in ["look", "check"]):
            response = "I don't see that item."

            for i in range(len(currentRoom.items)):
                if (noun == currentRoom.items[i]):
                    response = currentRoom.itemDescs[i]
                    break

            # allows interactables to be looked
            for i in range(len(currentRoom.interactables)):
                if (noun == currentRoom.interactables[i]):
                    response = currentRoom.interactableDescs[i]
                    break

            # allows hiddenItems to be looked, despite that they're not seen
            for i in range(len(currentRoom.hiddenItems)):
                if (noun == currentRoom.hiddenItems[i]):
                    response = currentRoom.hiddenItemDescs[i]
                    break

            # allows un-taken grabbables to be looked
            for i in range(len(currentRoom.grabbables)):
                if (noun == currentRoom.grabbables[i]):
                    response = currentRoom.grabbableDescs[i]
                    break

            # allows taken grabbables to be looked
            for i in range(len(inventory)):
                if (noun == inventory[i]):
                    response = inventoryDesc[i]
                    break

        elif (verb in ["take", "get"]):
            response = "I don't see that item."
            for i in range(len(currentRoom.grabbables)):
                if (noun == currentRoom.grabbables[i]):
                    inventory.append(currentRoom.grabbables[i])
                    inventoryDesc.append(currentRoom.grabbableDescs[i])
                    currentRoom.delGrabbable(currentRoom.grabbables[
                                             i], currentRoom.grabbableDescs[i])

                    response = "Item grabbed."
                    break

        elif (verb in ["use"]):
            response = "You don't have that item."
            for item in inventory:
                if (noun == item):
                    response = "{} could not be used".format(item)
                    for i in range(len(currentRoom.interactableReqs)):
                        if (noun == currentRoom.interactableReqs[i]):
                            if (currentRoom.interactableState[i] == "on"):
                                currentRoom.interactableState[i] = "off"
                            elif (currentRoom.interactableState[i] == "off"):
                                currentRoom.interactableState[i] = "on"

                            response = "{} used.".format(item)
                            break
    print "\n{}".format(response)
