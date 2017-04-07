###############################################################################
# Name: Dax Henson
# Date: 2017/04/0x
# Description:
###############################################################################
from Tkinter import *

# the room class
# note that this class is fully implemented with dictionaries as
# illustrated in the lesson "More on Data Structures"


class Room(object):
    # the constructor

    def __init__(self, name, image):
        # rooms have a name, an image (the name of a file),
        # exits (e.g., south), exit locations (e.g., to the south is room n),
        # items (e.g., table), item descriptions (for each item),
        # and grabbables (things that can be taken into inventory)
        self.name = name
        self.image = image
        self.exits = {}
        self.items = {}
        self.grabbables = []

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

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
        # append the exit and room to the appropriate dictionary
        self._exits[exit] = room

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate dictionary
        self._items[item] = desc

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
        for item in self.items.keys():
            s += item + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits.keys():
            s += exit + " "

        return s

# the game class
# inherits from the Frame class of Tkinter


class Game(Frame):
    # the constructor

    def __init__(self, parent):
        # call the constructor in the superclass
        Frame.__init__(self, parent)

    # creates the rooms
    def createRooms(self):
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
                   "There's a keycard on the desk\nbeside an inlaid terminal.")
        r1.addItem("chair", "It is smooth, black, and shiny.")
        r1.addItem("terminal", "The terminal glows an amber color. "
                   "There is text on the screen.")
        # this text can be looked, but it doesn't show up in Room.__str__
        r1.addHiddenItem("text", "The terminal displays a draft of a message
                         "to the separatist chancellor about\ntransporting a"
                         "bomb out of the basement.")

        # generates the library
        r2.addExit("south", r1)
        r2.addItem("rug", "It is awfully plush.")
        r2.addItem("bookshelves", "The bookshelves are meticulously packed
                   "with books.\n One of the books is not flush with the"
                   "others. It appears to be a journal.")
        # alas, I am a programmer, not an author
        r2.addGrabbable("journal", "\"Some poignant world-building.\"")

        # Generates a sunroom
        r3.addExit("north", r4)
        r3.addExit("west", r1)
        r3.addExit("south", None)
        r3.addItem("statue", "It has an oddly fascist... Maybe it's "
                   "the sieg heil salute.")
        r3.addItem("couch", "Rather plain, given the ornate statue nearby.")

        # generates a stairwell room
        r4.addExit("south", r3)
        # here we have "vertical" movement
        r4.addExit("down", r5)
        r4.addItem("stairwell", "There is some light downstairs, and an..."
                   "interesting smell wafts through.")

        # generates a stairwell room
        r5.addExit("up", r4)
        r5.addExit("west", r6)
        r5.addItem("stairwell", "Now that your eyes have adjusted, it's "
                   "rather dark upstairs.")

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
        r9.addExit("stairwell", "Returning to the surface will be exhausting.")

        # generates extra basement room
        r10.addExit("east", r9)
        r10.addExit("north", r11)

        # generates extra basement room
        r11.addExit("south", r10)
        r11.addExit("east", r12)

        # generates a basement room with an interactive bomb requiring a
        # keycard
        r12.addExit("west", r11)
        r12.addInteractable("bomb", "It must be deactivated to save the "
                            "Alliance. There is a card slot on the side.",
                            "on", "keycard")

        # generates an room "outside." Of course, it's only outside bc I say so
        r0.addExit("east", r6)
        r0.addItem("trees", "The tree is devoid of leaves. This would lead "
                   "you to assume that it is winter,\nexcept for the fact "
                   "that it is hot enough to fry an egg.")
        r0.addItem("grass", "The grass is brown and dead.")

        # sets which room the user starts in
        Game.currentRoom = r1
        # initialize the player's inventory
        Game.inventory = []

    # sets up the GUI
    def setupGUI(self):
        # organize the GUI
        self.pack(fill=BOTH, expand=1)

        # setup the player input at the bottom of the GUI
        # the widget is a Tkinter Entry
        # set its background to white and bind the return key to the
        # function process in the class
        # push it to the bottom of the GUI and let it fill
        # horizontally
        # give it focus so the player doesn't have to click on it
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()
        # setup the image to the left of the GUI
        # the widget is a Tkinter Label
        # don't let the image control the widget's size
        img = None
        Game.image = Label(self, width=WIDTH / 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)
        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH / 2)
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

    # sets the current room image
    def setRoomImage(self):
        if (Game.currentRoom is None):
            # if dead, set the skull image
            Game.img = PhotoImage(file="death.gif")
        else:
            # otherwise grab the image for the current room
            Game.img = PhotoImage(file=Game.currentRoom.image)
        # display the image on the left of the GUI
        Game.image.config(image=Game.img)
        Game.image.image = Game.img

    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disabled it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom is None):
            # if dead, let the player know
            Game.text.insert(END, "You are dead. The only thing you can do "
                                  "now is quit.\n")
        else:
            # otherwise, display the appropriate status
            Game.text.insert(END, str(Game.currentRoom) +
                             "\nYou are carrying: " + str(Game.inventory) +
                             "\n\n" + status)
        Game.text.config(state=DISABLED)

    # plays the game
    def play(self):
        # add the rooms to the game
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the current status
        self.setStatus("")

    # processes the player's input
    def process(self, event):
        # grab the player's input from the input at the bottom of
        # the GUI
        action = Game.player_input.get()
        # set the user's input to lowercase to make it easier to
        # compare the verb and noun to known values
        action = action.lower()
        # set a default response
        response = "I don't understand. Try verb noun. "\
                   "Valid verbs are go, look, and take"
        # exit the game if the player wants to leave (supports quit,
        # exit, and bye)
        if (action in ["quit", "exit", "bye"]):
            exit(0)
        # if the player is dead if goes/went south from room 4
        if (Game.currentRoom is None):
            # clear the player's input
            Game.player_input.delete(0, END)
            return
        # split the user input into words (words are separated by
        # spaces) and store the words in a list
        words = action.split()
        # the game only understands two word inputs
        if (len(words) == 2):
            # isolate the verb and noun
            verb = words[0]
            noun = words[1]
            # the verb is: go
            if (verb == "go"):
                # set a default response
                response = "Invalid exit."
                # check for valid exits in the current room
                if (noun in Game.currentRoom.exits):
                    # if one is found, change the current room to
                    # the one that is associated with the
                    # specified exit
                    Game.currentRoom = Game.currentRoom.exits[noun]
                # set the response (success)
                response = "Room changed."
            # the verb is: look
            elif (verb == "look"):
                # set a default response
                response = "I don't see that item."
                # check for valid items in the current room
                if (noun in Game.currentRoom.items):
                    # if one is found, set the response to the
                    # item's description
                    response = Game.currentRoom.items[noun]
            # the verb is: take
            elif (verb == "take"):
                # set a default response
                response = "I don't see that item."
                # check for valid grabbable items in the current room
                for grabbable in Game.currentRoom.grabbables:
                    # a valid grabbable item is found
                    if (noun == grabbable):
                        # add the grabbable item to the player's inventory
                        Game.inventory.append(grabbable)
                        # remove the grabbable item from the room
                        Game.currentRoom.delGrabbable(grabbable)
                        # set the response (success)
                        response = "Item grabbed."
                        # no need to check any more grabbable items
                        break
        # display the response on the right of the GUI
        # display the room's image on the left of the GUI
        # clear the player's input
        self.setStatus(response)
        self.setRoomImage()
        Game.player_input.delete(0, END)


##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()
