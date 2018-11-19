# This is a procedural appraoch to a text based rpg game
# The Zombie is attacking the human
# The Human as the option to:
# 1.Attack
# 2.Defend
# 3.Dance
# 4.Leave
human_health = 100
human_power = 80
zombie_health = 100
zombie_power = 80
import os

player_name = raw_input("Whats your name?")
user_input = raw_input("What option would you like to choose?")


def Attack(): 
    global zombie_health
    print "Welcome, %s." % player_name      #These variables are in the function scope
    
    while human_health > 0 and zombie_health > 10:
        print "You have %d health and %d power." % (human_health, human_power)
        print "The zombie has %d health and %d power." % (zombie_health, zombie_power)
        print "What do you want to do?"
        print "1. Attack"
        print "2. Defened"
        print "3. Dance"
        print "4. Leave"

        if user_input == "1":
            # The human has attacked the zombie
            zombie_health -= human_power
            print "You attackted the zombie. %d" % human_health
            

        elif user_input == "2":
            # The human has Defened there person
            zombie_health -= human_health
            Defend()
            print "You defended yourself. Watch out!!"

        elif user_input == "3":
            print "The Zombie is getting groovy"



def Defend():
     if user_input == "2":
            # The human has Defened there person
            zombie_health -= human_health
            print "You defended yourself. Watch out!!"
        else:
            os.system("say The Master won.")
            raw_input("Hit enter to continue")
            os.system("clear")

def Dance():
    if user_input == "3":
        print "The Zombie is dancing...."
Dance()