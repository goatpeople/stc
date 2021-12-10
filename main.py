import random
import time


#Clearing Terminal of old text
x=20
while x > 0:
    print(" ")
    x -= 1
#


class Character:
    def __init__(self, level, health, max_health, armor, priority, min_attack, max_attack, gold, gold_gain):
        self.level = level
        self.health = health
        self.max_health = max_health
        self.armor = armor
        self.priority = priority
        self.min_attack = min_attack
        self.max_attack = max_attack
        self.gold = gold
        self.gold_gain = gold_gain
character = Character(level = 1, health = 50, max_health = 50, armor = 0, priority = 500, min_attack = 40, max_attack = 50, gold = 500, gold_gain = 1)

class Monster:
    def __init__(self, level, health, max_health, armor, priority, min_attack, max_attack, reward):
        self.level = level
        self.health = health
        self.max_health = max_health
        self.armor = armor
        self.priority = priority
        self.min_attack = min_attack
        self.max_attack = max_attack
        self.reward = reward
monster = Monster(level = 1, health = 10, max_health = 10, armor = 0, priority = 5, min_attack = 1, max_attack = 5, reward = 1)  

class Shop:
    def __init__(self, level, health, armor, min_attack, max_attack, goldgain):
        self.level = level
        self.health = health
        self.armor = armor
        self.min_attack = min_attack
        self.max_attack = max_attack
        self.goldgain = goldgain
shop = Shop(level = 1, health = 10, armor = 1, min_attack = 1, max_attack = 1, goldgain = 1)

#Character backstory
in_town = True
TownName = input("You arrive at the Drunken Dwarf, a pub on the outskirts of ____: (Town Name) ")

#Limit Town/Character names to a certain character count?

print(f"You arrive at the Drunken Dwarf, a pub on the outskirts of {TownName}.")
print("You walk inside and see the bustling scene of travelers. The bartender looks towards you.")
Character_Name = input("Hey, welcome back, I remember you! You're ___!: (Character Name) ")
# NPC's will refer back to the player as {Character_Name}





Character_Alive = True
#While the character is alive, the game loop will run. First-time setup should happen before this loop
while Character_Alive == True:

    print(f"You're {Character_Name}, a level {character.level} character with {character.gold} gold.")
    print(f"You have {character.health}/{character.max_health} health, {character.armor} armor, {character.priority} priority, and deal {character.min_attack} to {character.max_attack} damage.")
    print(" ")
    action = input("--What would you like to do? (fight, heal, shop, quit): ").lower()
    

    if action == "quit":
        #save_confirm = input("Would you like to save before you quit?: (Yes/No) ").lower()
            #if save_confirm == "yes":
                #SAVE GAME HERE, SAVE FILE TO DESKTOP
            #else:
                #break
        Character_Alive = False


    if action == "heal":
        healconfirm = input(f"You will spend {character.level} gold to heal. Do you want to continue? (yes/no): ").lower()
        if healconfirm == "yes":
            if (character.gold - character.level) >= 0:
                character.gold = character.gold - character.level
                character.health = character.max_health
                print(" ")
                print(f"You have been healed! You now have {character.health}/{character.max_health} health.")
                print(" ")
                
            else:
                print(" ")
                print(f"You do not have enough gold to heal. You need {character.level} gold to heal, but you have {character.gold} gold.")
                print(" ")

        if healconfirm == "no":
            print(" ")
            print(f"You did not spend any money to heal. You have {character.health}/{character.max_health} health.")
            print(" ")

        pass


    if action == "fight":

        #Resetting monster's health to max before the fight
        monster.health = monster.max_health

        in_combat = True
        print("""


        You have now entered combat!


        """)


        if in_combat == True:
            while monster.health and character.health >= 1:
                for monster_attack in range(2):
                    damage = (random.randint(monster.min_attack, monster.max_attack)) - (character.armor)
                    if damage <= 0:
                        damage = 0

                character.health = (character.health - damage)

                time.sleep(0.5)
                print(f"""
                The monster attacks you, dealing {damage} damage.
                You have {character.health}/{character.max_health} health left.
                """)

                action = input("-- What do you do? (attack, run, quit): ").lower()
                if action == "attack":

                    time.sleep(0.5)
                    for character_attack in range(1):
                        damage = (random.randint(character.min_attack, character.max_attack)) - (monster.armor)
                        if damage <= 0:
                            damage = 0

                    monster.health = (monster.health - damage)
                    if monster.health <= 0:
                        monster.health = 0

                    print(f"""
                    You attack the monster, dealing {damage} damage.
                    The monster has {monster.health}/{monster.max_health} health left.
                    """)

                if action == "run":
                    character.health = 1
                    character.gold = (character.gold * 0.5)
                    print(" ")
                    print("You have run away from the fight. You have lost half your gold, and your health is low.")
                    print(" ")
                    in_combat = False
                    break        

                if action == "quit":
                    quit()

            else:
                
                if character.health <= 0:
                    print("You have died! You must restart your adventure.")
                    quit()


                if monster.health <= 0:
                    time.sleep(1)
                    print(f"You won the fight! You gain {monster.reward} gold!")
                    print(" ")
                    print("Out of Combat")
                    print("=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=")
                    print(" ")
                    print(" ")
                    
                    character.gold = round((character.gold + (monster.reward * character.gold_gain)), 2)
                    in_combat = False
                    
        pass





    if action == "shop":
        shopinput = "buy"
        while shopinput != "return":
            print(" ")
            shopinput = input("Welcome to the shop! You may buy/upgrade stats here. What would you like to do? (buy, return): ").lower()
            print(" ")
            if shopinput == "buy":
                
                print(f"You may purchase the following stats:")
                print(f"Health: {character.max_health} -- Costs {shop.health}")
                print(f"Level: {character.level} -- Costs {shop.level}")
                print(f"Min/Max Damage: {character.min_attack}/{character.max_attack} -- Costs {shop.min_attack}/{shop.max_attack}")
                print(f"Gold Gain: {character.gold_gain} -- Costs {shop.goldgain}")
                print(" ")
                buyinput = input("What would you like to purchase? (health, level, damage, gold gain, return): ").lower()
                print(" ")

                if buyinput == "health":
                    print(" ")
                    healthconfirm = input(f"You may purchase 5 Health for {shop.health} gold. Do you want to continue? (yes, no): ").lower()
                    if healthconfirm == "yes":
                        if (character.gold - shop.health) >= 0:
                            character.gold = character.gold - shop.health
                            character.max_health = (character.max_health + 5)
                            print(f"You have paid {shop.health} to increase your health. You now have {character.max_health} health!")
                            character.health = character.max_health
                            shop.health = (shop.health + 1)
                            shopinput = "return"
                        else:
                            print(" ")
                            print(f"You do not have enough gold upgrade your health. You need {shop.health} gold to upgrade, but you have {character.gold} gold.")
                            print(" ")
                            shopinput = "return"
                    else:
                        shopinput = "return"


                if buyinput == "level":
                    print(" ")
                    levelconfirm = input(f"You may purchase 1 level for {shop.level} gold. Do you want to continue?: (yes, no) ").lower()


                if buyinput == "damage":
                    print(" ")
                    damageconfirm = input(f"You may purchase 1 Minimum Damage for {shop.min_attack}, and 1 Maximum Damage for {shop.max_attack}. Which would you like to purchase?: (min, max, return) ").lower()

                    if damageconfirm == "min":
                        print(" ")
                        minconfirm = input(f"You have {character.gold}, and 1 Minimum Damage costs {shop.min_attack}. Would you like to upgrade?: (yes, no) ").lower()

                        if minconfirm == "yes":
                            if (character.gold - shop.min_attack) >= 0:
                                character.gold = (character.gold - shop.min_attack)
                                character.min_attack = (character.min_attack + 1)
                                shop.min_attack = (shop.min_attack + 1)
                                print(f"You now have {character.min_attack} Minimum Damage and {character.gold} gold.")
                                print(" ")
                            else:
                                print(" ")
                                print(f"Upgrading your Minimum damage will cost {shop.min_attack}, but you only have {character.gold}.")
                                print(" ")
                                shopinput = "return"
                        
                        else:
                            shopinput = "return"
                    if damageconfirm == "max":  
                        print(" ")
                        maxconfirm = input(f"You have {character.gold}, and 1 Maximum Damage costs {shop.max_attack}. Would you like to upgrade?: (yes, no) ").lower()

                        if maxconfirm == "yes":
                            if (character.gold - shop.max_attack) >= 0:
                                character.gold = (character.gold - shop.max_attack)
                                character.min_attack = (character.min_attack + 1)
                                shop.max_attack = (shop.max_attack + 1)
                                print(f"You now have {character.max_attack} Maximum Damage and {character.gold} gold.")
                                print(" ")
                                shopinput = "return"
                            else:
                                print(" ")
                                print(f"Upgrading your Maximum damage will cost {shop.max_attack}, but you only have {character.gold}.")
                                print(" ")
                                shopinput = "return"
                        else:
                            shopinput = "return"
                    else:
                        shopinput = "return"  

                if buyinput == "gold gain":
                    print(" ")
                    goldgainconfirm = input(f"You may add 0.1x gold gain for {shop.goldgain} gold. Do you want to continue?: (yes, no) ").lower()
                    if goldgainconfirm == "yes":
                        if (character.gold - shop.goldgain) >= 0:
                            character.gold = character.gold - shop.goldgain
                            character.gold_gain = round((character.gold_gain + .1), 1)
                            print(f"You have paid {shop.goldgain} gold to increase your gold gain. You now have {round(character.gold_gain,1)}x increased gold gain!")
                            shop.goldgain = (shop.goldgain * 1.7)
                            shopinput = "return"

                        else:
                            print(" ")
                            print(f"You do not have enough gold upgrade your health. You need {shop.goldgain} gold to upgrade, but you have {character.gold} gold.")
                            print(" ")
                            shopinput = "return"                            
                    else:
                        shopinput = "return"

    pass





# Would you like to view your journey's stats? (Yes/No)
    # Yes? Show death stats
    # No? print("In a hurry I see...")
# Finally: Show death reason.

#if death_reason == "dungeon"
    #You have died from a SKELETON/SLIME/ORC/ETC

#Use this for the "quit" death message.
#if death_reason == "quit"
random_death_message = random.randint(1, 4)
if random_death_message == 1:
    random_death_message = "from a heart attack!"
if random_death_message == 2:
        random_death_message = "from to a feral kitten! Yikes."
if random_death_message == 3:
    random_death_message = "by being smothered under the biggest ball of yarn."
if random_death_message == 4:
    random_death_message = "due to your own misuse of matches."
print(f"You have died {random_death_message}")


#    COMMENTS DOWN BELOW:
#
#
#   Possible additions:
#   Help section to explain the game?
#   Adding the names of your previous (dead) characters at the pub (using save data). A "Memory Wall", with character name, level, and town.
#   Different starting scenarios
#
#
#
#
#
#
#   To-Do:
#   1) Def functions to clean up repeat code?
#   2) Complete Shop -- Level and Damage
#   3) Impliment turn system