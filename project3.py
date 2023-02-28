########
#import modules
#######
########
#define functions
####### first you start in the compound and have a choice of surredering to the ATF or going to the nursery to retrieve your kids. If you go surrender to the ATF then the game ends immediately. If you go to the nursery then you retreive your kids and are given the option to go to the farm or back to the compound. if you go to the farm you obtain the food and are given the option ot go back to the compound or go to the chapel. If or when you have visited all locations you have the option to escape. if you escape you win. 
# have_you_been_to_the_nursery (boolean. starts false but after visiting the nursery location it updates and becomes true.)
# have_you_been_to_the_farm (boolean. starts false but ater you have visited the farm it becomes food)
# have_you_been_to_the_chapel (boolean. starts off false but changes to true after you have visited the chapel)
def start():
    print("Waco Project. \n\t It is March 15 and you are a Branch Davidian and are planning to escape from the grasps of David Koresh. You can't leave though without your kids. You have to retrieve your kids, gather some food, and pray at the chapel before you escape. Or you could leave and surrender to the ATF")
    compound()
def compound():
    print("You are in the Compound")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tnursery\n\tATF\n\tescape")
    if move.lower() == "nursery":
        nursery()
    elif move.lower() == "atf":
        atf()
    elif move.lower() == "escape":
        escape()
    else:
        print("N/A, choose a displayed option")
def nursery():
    print("You are in nursery")
    global have_you_been_to_the_nursery
    have_you_been_to_the_nursery = True 
    move = input("\nWhere would you like to go? Say one of these choices:\n\tcompound\n\tfarm\n")
    if move.lower() == "compound":
        compound()
    elif move.lower() == "farm":
        farm()
    else:
       print("N/A, choose a displayed option")
def farm():
    print("You are in the farm")
    global have_you_been_to_the_farm
    have_you_been_to_the_farm = True
    move = input("\nWhere would you like to go? Say one of these choices:\n\tcompound\n\tchapel\n")
    if move.lower() == "compound":
        compound()
    elif move.lower() == "chapel":
        chapel()
    else:
       print("N/A, choose a displayed option")
def chapel():
    print("You are in the farm")
    global have_you_been_to_the_chapel
    have_you_been_to_the_chapel = True
    move = input("\nWhere would you like to go? Say one of these choices:\n\tcompound\n\tescape\n")
    if move.lower() == "compound":
        compound()
    elif move.lower() == "escape":
        escape()
    else:
       print("N/A, choose a displayed option")
def escape():
    if have_you_been_to_the_nursery == False:
        print("you have to go to the nursery before being allowed to succeed")
    elif have_you_been_to_the_farm == False:
        print("you have to go to the farm before being allowed to succeed")
    elif have_you_been_to_the_chapel == False:
        print("you have to go to the chapel before being allowed to succeed")
    else:
        print("congrats. You have succeeded in escaping")

def atf():
    print("You are now surrendering to the ATF and have lost the game")


########
#main
#######
have_you_been_to_the_nursery = False
have_you_been_to_the_farm = False
have_you_been_to_the_chapel = False
start()