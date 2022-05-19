

from ast import literal_eval
import os
from os import system
import time
import sys
import random


def clear():
    os.system('clear')

def fprint(string):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.05)
    print()



#def madLibs(input):
#    print(f"""\'Welcome to the class, students. Today we'll be covering consumerism in a socialist economy.'
#"But suddenly, something bursts into the room. It's a giant {input}!""")

#def madLibs2(adjective, adjective2):
#    print(f"It is {adjective} and powerful! It rears its {adjective2} head.")


confirm = "nope"

while confirm != "yes":
    clear()
    print("Welcome to Myles' Mad Libs text game.")
    print("Unless prompted otherwise, please answer in singular quantities (e.g. 'carrot' not 'carrots'")
    print("Please answer in lower-case letters, unless your answer is a proper noun.")
    confirm = (input("Type 'yes' to continue -->  "))

    if confirm == "yes":
        clear()
        place = input("Your favourite old movie -->  ")
        clear()
        weather = input("Type of weather, ending in -y -->  ")
        clear()
        utensil = input("A kitchen utensil -->  ")
        clear()
        neighbour = input("Your least favourite Simpsons character -->  ")
        clear()
        vegetable = input("The healthiest vegetable you can think of -->  ")
        clear()
        exclamation = input("An exclamation, starting with a capital letter (e.g. 'Wow!' 'What the hell?') -->  ")
        clear()
        adj = input("A past tense adjective (e.g. 'startled' 'amazed') -->  ")
        clear()
        car = input("Your favourite model of car -->  ")
        clear()
        zombie1 = input("A non-human fictional character -->  ")
        clear()
        food = input("Your favourite flavour of soup -->  ")
        clear()
        dystopia = input("A dystopian movie -->  ")
        clear()
        cha1 = input("Your second-favourite Beatles member -->  ")
        clear()
        cha2 = input("A character from a TV series you've never watched -->  ")
        clear()
        cha3 = input("The name you would give a pet tarantula -->  ")
        clear()
        music = input("A Marvel character -->  ")

        clear()
        fprint("Welcome to the wondrous land of " + place + "ville!")
        time.sleep(2)
        fprint("It is a " + weather + " day today here in " + place + "ville.")
        time.sleep(2)
        fprint("But this weather is disturbed by a sudden shaking of the earth under your feet.")
        time.sleep(2)
        fprint("You glance over at your neighbour " + neighbour + "'s house. They appear to be out gardening.")
        time.sleep(2)
        fprint("But soon, you realize that they are actually harvesting brains, not " + vegetable + "s!")
        time.sleep(2)
        fprint("You run out onto the street. '" + exclamation + "' you scream. 'Zombies!'")
        time.sleep(2)
        fprint("All your neighbours begin stumbling clumsily toward you. You are " + adj + " to realize that they, too, are all zombies.")
        time.sleep(2)
        fprint("You run to your garage to find your " + car + " parked inside.")
        time.sleep(2)
        fprint("You loudly rev the engine, unless it's an electric car, in which case you quietly activate the engine.")
        time.sleep(2)
        fprint("Slowly you wheel it out of the garage, when suddenly a zombie " + zombie1 + " leaps onto your windshield. It is holding a " + utensil + "!")
        time.sleep(2)
        fprint("You activate the windshield wipers. They push it off the windshield, but leave zombie goo all over. You'll have to get that cleaned.")
        time.sleep(2)
        fprint("'" + exclamation + "' you holler, as you propel your " + car + " through waves of zombies.")
        time.sleep(2)
        fprint("Eventually you make it to a " + dystopia + "-style hideout. You meet with the survivors.")
        time.sleep(2)
        fprint("Among the survivors are: Jason Knox, a librarian turned shirtless crossbow sunglasses guy, you know the type.")
        time.sleep(2)
        fprint(cha2 + ", who is currently holding a big chainsaw. They look ready to kill.")
        time.sleep(2)
        fprint(cha1 + ", who you discover is secretly an accordian player, and the camp cook.")
        time.sleep(2)
        fprint(cha3 + ", who needs no indroduction, nor indeed an explanation.")
        time.sleep(2)
        fprint("You all hop in the " + car + ". The " + place + "ville " + music + "s are on the radio-- your favourite band.")
        time.sleep(2)
        fprint("You drive through the streets of " + place + "ville, killing loads of zombies on your way.")
        time.sleep(2)
        fprint(cha1 + " throws " + food + " soup in the zombies' eyes. " + cha3 + " jumps out of the car and starts kicking them to death.")
        time.sleep(2)
        fprint(cha2 + " follows this by chainsawing anything they can reach from the car window.")
        time.sleep(2)
        fprint("Jason Knox does what he does best-- shoot his crossbows and flex his muscles.")
        time.sleep(2)
        fprint("And you join in by saying your trademark catchphrase, '" + exclamation + "!'")
        time.sleep(2)
        
        fprint("Thank you for playing my game! I hope you enjoyed it.")




#madLibs(input("Enter a noun -->  "))
#madLibs2(input("Enter an adjective -->  "), input("Enter another -->  "))







