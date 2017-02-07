###############################################################################
# Name: Dax Henson
# Date: 2017/02/0x
# Description: Adventure Text Game
###############################################################################

###############################################################################
# the blueprint for a room


class Room(object):
    # the constructor

    def __init__(self, name):
        # rooms have a name, exits, exit locations, items, item descriptions
        # and grabbables (things that can be taken into inventory)
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
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
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.append(item)

    # removes a grabbable item from the room
    # the item is a string (e.g., key)
    def delGrabbable(self, item):
        # remove the item from the list
        self._grabbables.remove(item)

    # returns a string description of the room
    def __str__(self):
        # first, the room name
        s = "You are in {}.\n".format(self.name)

        # next, the items in the room
        s += "You see: "
        for item in self.items:
            s += item + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "

        return s


###############################################################################
# creates the rooms
def createRooms():
    global currentRoom

    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")

    r1.addExit("east", r2)
    r1.addExit("south", r3)
    r1.addGrabbable("key")
    r1.addItem("table", "It is made of oak. A golden key rests on it.")
    r1.addItem("chair", "It is made of wicker and no one is sitting on it.")

    r2.addExit("south", r4)
    r2.addExit("west", r1)
    r2.addItem("rug", "It is awfully plush.")
    r2.addItem("fireplace", "It is warm, but dying.")

    r3.addExit("north", r1)
    r3.addExit("east", r4)
    r3.addGrabbable("book")
    r3.addItem("bookshelf", "The bookshelf is neatly packed with books.\n"
               "One of the books is not flush with the others.")
    r3.addItem("statue", "There is nothing special about it.")
    r3.addItem("desk", "The statue is resting on it. So is a book.")

    r4.addExit("north", r2)
    r4.addExit("west", r3)
    r4.addExit("south", None)
    r4.addGrabbable("six-pack")
    r4.addItem("table", "It is made of oak. A golden key rests on it.")
    r4.addItem("chair", "It is made of wicker and no one is sitting on it.")

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


###############################################################################
# START THE GAME!!!
createRooms()
inventory = []


while True:
    if (currentRoom is None):
        death()
        break
    status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)

    print "==================================================================="
    print status

    action = raw_input("What do you want to do? ")
    action = action.lower()

    while (action == ""):
        action = raw_input("")
        action = action.lower()
    else:
        response = "I don't understand. Try valid noun.\n"\
            "Valid verbs are:\n\n[go, head]\n[look, check]\n[take, get]"

    if (action in "quit", "exit", "bye"):
        break

    words = action.split()
    if (len(words) == 2):
        verb = words[0]
        noun = words[1]

        if (verb in "go", "head"):
            response = "Invalid exit"

            if (noun == "n"):
                noun = "north"

            if (noun == "e"):
                noun = "east"

            if (noun == "s"):
                noun = "south"

            if (noun == "w"):
                noun = "west"

            for i in range(len(currentRoom.exits)):
                if (noun == currentRoom.exits[i]):
                    currentRoom = currentRoom.exitLocations[i]

                    response = "Room changed."

                    break

        elif (verb in "look", "check"):
            response = "I don't see that item."

            for i in range(len(currentRoom.items)):
                if (noun == currentRoom.items[i]):
                    response = currentRoom.itemDescriptions[i]
                    break
        elif (verb in "take", "get"):
            response = "I don't see that item."
            for grabbable in currentRoom.grabbables:
                if (noun == grabbable):
                    inventory.append(grabbable)
                    currentRoom.delGrabbable(grabbable)
                    response = "Item grabbed."
                    break

    print "\n{}".format(response)
