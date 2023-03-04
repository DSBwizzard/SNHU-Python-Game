# Matthew Albrecht

import time # lets us use sleep() to delay text in a few places


player_location = 'Central Hallway' # initialize player location
player_inv = [] # a list to hold all the cool stuff the player will obtain

# A dictionary which links rooms to other rooms.
rooms = {
        'Central Hallway': {'North': 'Toy Store', 'West': 'Hole-in-One! Sports Store', 'South': 'Rear Hallway', 'East': 'Shiny Treasures Jewelry Store'},
        'Toy Store': {'South': 'Central Hallway', 'East': 'Sooper-Play-Zone! Foam Dart Shootout'},
        'Sooper-Play-Zone! Foam Dart Shootout': {'West': 'Toy Store'},
        'Shiny Treasures Jewelry Store': {}, # There is no turning back once you face the thief
        'Hole-in-One! Sports Store': {'East': 'Central Hallway'},
        'Rear Hallway': {'North': 'Central Hallway', 'East': "Ballet n' Ballroomz Dance Studio", 'South': 'Maintenance Office', 'West': 'Quirky Hardware Store'},
        'Quirky Hardware Store': {'East': 'Rear Hallway'},
        'Maintenance Office': {'North': 'Rear Hallway'},
        "Ballet n' Ballroomz Dance Studio": {'West': 'Rear Hallway'}
    }

items = { # maps items to locations
        'Toy Store': 'Robot',
        'Sooper-Play-Zone! Foam Dart Shootout': 'Gun',
        'Hole-in-One! Sports Store': 'Helmet',
        'Quirky Hardware Store': 'Spring',
        'Maintenance Office': 'Key',
        "Ballet n' Ballroomz Dance Studio": 'Ribbon'
    }

# occurs when player enters jewelry store. Ends the game!
def showtime():
    print("You need to get into the maintenance hall while the thief isn't paying attention. You quickly sneak")
    print("towards the locked hallway door while they're busy pointing at something in a display case.\n")
    input("Press Enter to continue...")

    if 'Key' in player_inv:
        print('\nYou make it to the door, and hastily unlock it with the Maintenance Hall Key before shuffling inside.')
        print('You follow the hallway to reach the maintenance entrance of the jewelry store. The thief is standing at'
              ' an angle where they would see you open the door.')
        print("You need to distract the thief with something.\n")
        input("Press Enter to continue...")
        print()
    else:
        print("\nYou make it to the door but instantly realize that you don't have the key to open it with.")
        print("Before you can get away, the thief sees you! They start to move closer...")
        time.sleep(3)
        print("Game over...")
        quit()

    if 'Robot' in player_inv:
        print("You turn the Robot on, open the door just a crack, and send the toy walking towards the thief.")
        print("The little toy whirs and beeps as it wanders vaguely in the direction of the criminal.")
        print("This catches their attention, and they shift their body to the side to get a good look at the"
              " toy on the floor.")
        print("Now! This is your chance!\n")
        input("Press Enter to continue...")
        print()
    else:
        print("You reach for your Action Figure, but realize you never grabbed it.")
        print("Anxiously you realize that, without something to distract the thief, you're gonna have to bail.\n")
        input("Press Enter to continue...")
        print()
        print("You sneak back out the first door, however it slams shut as you try to close it behind you! The thief"
              " clearly hears this, and they start to move closer...")
        time.sleep(3)
        print("Game over...")
        quit()

    if 'Gun' in player_inv:
        print("You aim your Dart Gun at the unaware thief's hand. They're not paying much attention to their pistol"
              " at the moment.")
        print("You hold your breath, steady your aim as best you can, and pull the trigger!\n")
        input("Press Enter to continue...")
        print()
    else:
        print("You reach for your Dart Gun and panic when you realize it isn't with you. You must not have"
              " picked it up!")
        print("The thief kicks the Action Figure aside, and looks to where it came from to see you kneeling in the"
              " doorway.")
        print("They turn to face you and all too quickly you realize you're in trouble.")
        time.sleep(3)
        print("Game over...")
        quit()

    if 'Spring' in player_inv:
        print('A deep "KTHUNK" is heard as the foam dart is launched with great force by the Heavy-Duty'
              ' Spring installed in the Dart Gun.')
        print("Your aim was true, and the dart slams directly into the pistol, sending it sailing out of the criminal's"
              " hand.")
        print("As the handgun noisily clatters across the shop floor, the thief turns to you in bewilderment.")
        print("You need to act now, while you still have surprise on your side!\n")
        input("Press Enter to continue...")
        print()
    else:
        print("As you watch the small foam dart float gently towards the thief, you realize that you never collected")
        print("or installed the Heavy-Duty Spring into the gun.")
        print("The dart gently tickles the hand of the thief, who turns and sees you kneeling in the doorway.")
        print("You very quickly realize that you're in trouble.")
        time.sleep(3)
        print("Game over...")
        quit()

    if 'Helmet' in player_inv:
        print("You dash forward! Shouting loudly, you extend your shoulder and crash aggressively into the thief,"
              " slamming the two of you into the floor.")
        print("You're just slightly rattled, but entirely unfazed otherwise thanks to the reliable Football Helmet"
              " you made sure to wear.")
        print("The criminal is clearly winded, but seems to be coming to their senses again. You're not done yet!\n")
        input("Press Enter to continue...")
        print()
    else:
        print("You spring to your feet and prepare to tackle the thief. Just before you start to run, however,"
              " you realize that you don't have a Football Helmet on.\n")
        print("You've been told that you've broken a door once, roughhousing without a helmet, and the fact that you")
        print("can't remember doing that is the reason you promised yourself you'd always play it safe going forward.\n")
        print("While you stand there reminiscing and wondering about your missing helmet, the thief has started to")
        print("move towards you - and it's clear they aren't worried about safety equipment...")
        time.sleep(3)
        print("Game over...")
        quit()

    if 'Ribbon' in player_inv:
        print("Moving quickly, you unravel the Gymnastics Ribbon you brought and start tying the thief's arms and legs"
              " together.")
        print("While you were uncertain at first, the ribbon is surprisingly very strong and the now-alert thief is"
              " fully restrained.\n")
        input("Press Enter to continue...")
        print()
        print("You jump back up and quickly take stock of what just happened. You feel a little light-headed, and more")
        print("jittery than the time you drank 3 energy drinks at one time...\n")
        time.sleep(4)
        print("But you turn around to hear cheers and whistling from a small crowd who had seen your bravery.")
        print("Several police officers move past you to collect the thief, and as they walk the criminal away"
              " it only in this moment fully dawns on you -")
        print("You saved the Jewelry Store!")
        print()

        print("Congratulations! Thank you for playing.")
        time.sleep(3)
        quit()
    else:
        print("You catch your breath and stand up, reach for your rope to restrain the thief, and do a double take as"
              " your hand grabs at nothing but empty air.")
        print("What happened?! Where is the Gymnastics Ribbon? Did you drop it somewhere in the excitement?")
        print("Panicked, you search the area around you as the now-alert thief stands up.\n")
        print("The crook, seemingly assessing the situation, decides to cut their losses and run. You give chase, but")
        print("They turn out to be much faster than you, and you can only watch as they escape to the outdoors...")
        time.sleep(3)
        print("Game over...")
        quit()


def help(): # shows the player what they can type at any time
    print()
    print('You must find 6 items throughout the Shopping Mall, which you will use to thwart a robbery-in-progress.')
    print('Remember, you will need all 6 items to pull of your super-sweet plan! Approaching the thief with any less'
          ' will surely go poorly.\n')
    print('Check your inventory with "inventory".')
    print('You can "move" between rooms, such as "move north".')
    print('Use "where" to check where you can go from your current location.')
    print('You can "look" to examine your surroundings and find anything interesting in any given room.')
    print('You can "take" items you find in rooms, such as "take key".')


def move(pl_loc, direction): # let the player move around the world
    if direction in rooms[pl_loc]:  # If cardinal direction is valid, based on dictionary and player's location
        new_location = rooms[player_location][direction]  # Move player
        return new_location
    else:
        print("\nYou can't go there! Use {} for a list of places you can reach from here.".format('"where"'))
#        for key, value in rooms[pl_loc].items():  # Gather and show player where they can go from here
#            print('{} to the {}'.format(key, value))
        return pl_loc

def look(pl_loc): # show the player what is around them, including importantly, items
    print()
    if pl_loc == 'Central Hallway':
        print('You are in the central hallway of the shopping mall. Many stores of all types surround you.')
        print("To the East is the jewelry store, actively being held up by the thief.")
        print('You should only engage the thief once you have everything you need to stop them.')
    elif pl_loc == 'Toy Store':
        print("The toy store is one of the mall's biggest attractions, featuring the latest in fun gadgets and games.")
        time.sleep(2)
        print("This is Rickey's favorite store.")
        if "Robot" not in player_inv:
            time.sleep(1)
            print('There is a Robot here.')
    elif pl_loc == 'Sooper-Play-Zone! Foam Dart Shootout':
        print(
            "This is a shooting range where visitors challenge each other using foam dart guns.")
        print("There are obstacles and walls scattered throughout to hide behind, and spring ambushes from.")
        if "Gun" not in player_inv:
            time.sleep(1)
            print('There is a Gun here.')
    elif pl_loc == 'Hole-in-One! Sports Store':
        print(
            "This is one of the mall's most recent additions. This large, spacious store has wide racks and shelves of"
            " various sporting goods.")
        print("Unfortunately, most of the stuff that would help in a fight is locked up.")
        print("Looking around you also notice that, despite the store's name, you see nothing related to golf anywhere.")
        if "Helmet" not in player_inv:
            time.sleep(1)
            print('There is a Helmet here.')
    elif pl_loc == 'Rear Hallway':
        print("You're standing within the mall's southern wing. There are several large cars on display here.")
        print("You've always wondered how they get those cars inside of the mall... or who goes car shopping in a mall.")
    elif pl_loc == 'Quirky Hardware Store':
        print(
            "This hardware store definitely earns its namesake. It's little more than a cramped room full of small"
            " wire shelves.")
        print("The shelves hold disorganized bins which are overflowing with unlabeled hardware and tools.")
        print("The store's mascot is a silly-looking blue robot. You've always liked that goofy guy.")
        if "Spring" not in player_inv:
            time.sleep(1)
            print('There is a Spring here.')
    elif pl_loc == 'Maintenance Office':
        print(
            "You find yourself in the mall's maintenance office, surprisingly alone. Usually there's at least"
            " one employee here at the desk, ")
        print("keeping an eye on the room and its contents.")
        time.sleep(2)
        print("How convenient!")
        if "Key" not in player_inv:
            time.sleep(1)
            print('There is a Key here.')
    elif pl_loc == "Ballet n' Ballroomz Dance Studio":
        print("This area is used as a dance studio for practice or performances. Across the room on the far end from"
            " where you're standing are short bleacher seats.")
        print("Those, while perfect for seating many visitors for shows, are probably the most uncomfortable thing man"
            " has ever created.")
        if "Ribbon" not in player_inv:
            time.sleep(1)
            print('There is a Ribbon here.')

    time.sleep(2)
    input("\nPress Enter to continue...")


def take(pl_loc, item): # is it stealing if you ultimately save the mall money?
    print()
    if (pl_loc, item) in items.items():
        player_inv.append(item) # give player item
        del items[pl_loc] # remove from item dict
        print("You take the {}. Use {} to see what you're holding now!".format(item, '"inventory"'))
    else:
        print('You {} see a {} here. Use "look" to see what is around you.'.format("don't", item))

def inventory(): # show the payer all the cool stuff they've taken
    if len(player_inv) == 0:
        print("\nYou are currently holding 0 out of 6 items.")
    else:
        print("\nYou are currently holding {} out of 6 items. Specifically you are holding:".format(len(player_inv)))
        for i in range(len(player_inv)):
            print(player_inv[i])

def where(pl_loc): # show the player where they can go based on their current location
    print()
    print('From here, you can reach the following locations:\n')
    for key, value in list(rooms[pl_loc].items()):
        x = str(key + ' to the ' + value)
        print(x)

print("You are Rickey, a brave young man wandering around his favorite shopping mall.")
time.sleep(3)
print("Suddenly, a crash! To your East you see a thief holding up the jewelry store!")
time.sleep(3)
print('"Not in MY mall", you think to yourself. You know you can stop the criminal...')
time.sleep(3)
print("...but you'll need to prepare first!\n")
time.sleep(2)
print('Use "help" for a list of commands.')


while True:
    print('\nYou are in the {}.'.format(player_location))
    user_input = input('What will you do? ').title() # Get input and normalize capitalization
    command = user_input.split()

    if command[0] == 'Move':
        player_location = move(player_location, command[1])
        if player_location == 'Shiny Treasures Jewelry Store':
            print("\nYou approach the jewelry store and stare at the thief.")
            print("They're ordering the employee around, waving a pistol to get what they want out of the display cases.")
            print("You know you can stop this. Despite feeling nervous, you take a moment to pump yourself up -"
                  " it's showtime!\n")
            input("Press Enter to continue...")
            print()
            showtime()

    elif command[0] == 'Look':
        look(player_location)

    elif command[0] == "Help":
        help()

    elif command[0] == "Where":
        where(player_location)

    elif command[0] == "Take":
        take(player_location, command[1])

    elif command[0] == "Inventory":
        inventory()

    else:
        print("You don't know how to {}. Type {} for a list of commands.\n".format(user_input, '"help"')) # This message shows if user enters an invalid command
