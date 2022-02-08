import random
import time

from character import character
from monster import rat, slime, skeleton, vulture, ogre
import item

inventory = item.Inventory()
#Clearing Terminal of old text
zz=20
while zz > 0:
    print(" ")
    zz -= 1


class Shop:
    def __init__(self, level, health, armor, min_attack, max_attack, goldgain):
        self.level = level
        self.health = health
        self.armor = armor
        self.min_attack = min_attack
        self.max_attack = max_attack
        self.goldgain = goldgain
shop = Shop(level = 1, health = 10, armor = 1, min_attack = 1, max_attack = 1, goldgain = 1)


skip_intro = True
if skip_intro == False:
    #Character backstory
    in_town = True
    character.hometown = input("You arrive at the Drunken Dwarf, a pub on the outskirts of ____: (Town Name) ")

    #Limit Town/Character names to a certain character count?

    print(f"You arrive at the Drunken Dwarf, a pub on the outskirts of {character.hometown}.")
    print("You walk inside and see the bustling scene of travelers. The bartender looks towards you.")
    character.name = input("Hey, welcome back, I remember you! You're ___!: (Character Name) ")



character_alive = True
#While the character is alive, the game loop will run. First-time setup should happen before this loop
while character_alive == True:

    print(f"You're {character.name}, a level {character.level} character with {character.gold} gold.")
    print(f"You have {character.health}/{character.max_health} health, {character.armor} armor, {character.priority} priority, and deal {character.min_attack} to {character.max_attack} damage.")
    print(" ")
    action = input("--What would you like to do? (fight, heal, shop, quit): ").lower()
    

    if action == "quit":
        #save_confirm = input("Would you like to save before you quit?: (Yes/No) ").lower()
            #if save_confirm == "yes":
                #SAVE GAME HERE, SAVE FILE TO DESKTOP
            #else:
                #break
        character_alive = False
        death_reason = "random"


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

### FIGHT IS BROKEN DUE TO NEW MONSTER FILE, REVAMP WITH MAP FILE FOR DUNGEON EXPERIENCE
    if action == "fight":
        in_combat = True

#   This can be moved to another file and pushed into a function (Generate Dungeon Level?) "eventually"
        dungeon_difficulty = 6

        dungeon_choice = random.random()
        
        print(f"TESTING PURPOSES - Dungeon_Choice = {dungeon_choice}")
        if dungeon_difficulty <= 2:
            if dungeon_choice <= .5:
                enemy = rat
            else:
                enemy = slime
        if dungeon_difficulty <= 3 and dungeon_difficulty > 2:
            if dungeon_choice <= .5:
                enemy = slime
            else:
                enemy = skeleton
        if dungeon_difficulty <= 5 and dungeon_difficulty > 3:
            if dungeon_choice <= .5:
                enemy = skeleton
            else:
                enemy = vulture
        if dungeon_difficulty <= 8 and dungeon_difficulty > 5:
            if dungeon_choice <= .5:
                enemy = vulture
            else:
                enemy = ogre
        if dungeon_difficulty > 8:
            enemy = ogre


        #Resetting monster's health to max before the fight, should be changed
        enemy.health = enemy.max_health

        print("""


        You have now entered combat!


        """)
        ####
        turn_order = []
        set_turn_order = {}
        player_input = ""

        # Add character and monsters here
        set_turn_order[character.name] = character.priority
        set_turn_order[enemy.name] = enemy.priority

        for entity in sorted(set_turn_order, key=set_turn_order.get, reverse=True):
            turn_order.append(entity)
            print(entity)


        print(turn_order) ##### TESTING PURPOSES #####

        while in_combat == True and enemy.health >= 1 and character.health >= 1:
            for turn in turn_order:
                if in_combat == True and enemy.health >= 1 and character.health >= 1 and player_input != "run":
                    print(" ")
                    print(f"""It is now {turn}'s turn!""")
                    print(" ")
                    time.sleep(0.5)
                    turn_pass = False
                    while turn_pass == False:
                        if turn == character.name:
                            player_input = input("What would you like to do? (attack, inventory, run, quit): ").lower()
                            if player_input == "attack":
                                print("attack")

                                damage = (random.randint(character.min_attack, character.max_attack)) - (enemy.armor)
                                if damage <= 0:
                                    damage = 0

                                enemy.health = (enemy.health - damage)
                                if enemy.health < 0:
                                    enemy.health = 0

                                time.sleep(0.5)
                                print(f"""
                                You attack the {enemy.name}, dealing {damage} damage.
                                The {enemy.name} has {enemy.health}/{enemy.max_health} health left.
                                """)

                                turn_pass = True

                            if player_input == "inventory": #NOT COMPLETE, will expand when item system is introduced
                                print("inventory")
                                turn_pass = True

                            if player_input == "run":
                                # if boss_room == True:
                                    #print("You cannot run in the boss room.")
                                # else:
                                character.health -= 10
                                character.gold = (character.gold * 0.5)
                                print(" ")
                                print("You have run away from the fight. You have lost half your gold, and you lose 10 health.")
                                print(" ")
                                in_combat = False
                                turn_pass = True

                            if player_input == "quit":
                                quit()


                        else:
                            if player_input != "run" or enemy.health > 0 or character.health > 0:
                                damage = (random.randint(enemy.min_attack, enemy.max_attack)) - (character.armor)
                                if damage <= 0:
                                    damage = 0
                                character.health = (character.health - damage)
                                if character.health < 0:
                                    character.health = 0 
                                    character_alive = False
                                    # Death reason still needs to be added, currently unused
                                    death_reason = "monster"
                                    break                               

                                time.sleep(0.5)
                                print(f"""
                                The {enemy.name} attacks you, dealing {damage} damage.
                                You have {character.health}/{character.max_health} health left.
                                """)                        

                            turn_pass = True
                            print(f"TURN_PASS = {turn_pass}")
                            print(" ")


    if action == "shop":
        shopinput = "buy"
        while shopinput != "menu":
            print(" ")
            shopinput = input("Welcome to the shop! You may buy/upgrade stats here. What would you like to do? (buy, menu): ").lower()
            print(" ")
            if shopinput == "buy":
                
                print(f"You may purchase the following stats:")
                print(f"Health: {character.max_health} -- Costs {shop.health}")
                print(f"Level: {character.level} -- Costs {shop.level}")
                print(f"Min/Max Damage: {character.min_attack}/{character.max_attack} -- Costs {shop.min_attack}/{shop.max_attack}")
                print(f"Gold Gain: {character.gold_gain} -- Costs {shop.goldgain}")
                print(" ")
                buyinput = input("What would you like to purchase? (health, level, damage, gold gain, menu): ").lower()
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
                            shopinput = "menu"
                        else:
                            print(" ")
                            print(f"You do not have enough gold upgrade your health. You need {shop.health} gold to upgrade, but you have {character.gold} gold.")
                            print(" ")
                            shopinput = "menu"
                    else:
                        shopinput = "menu"


                if buyinput == "level":
                    print(" ")
                    levelconfirm = input(f"You may purchase 1 level for {shop.level} gold. Do you want to continue?: (yes, no) ").lower()


                if buyinput == "damage":
                    print(" ")
                    damageconfirm = input(f"You may purchase 1 Minimum Damage for {shop.min_attack}, and 1 Maximum Damage for {shop.max_attack}. Which would you like to purchase?: (min, max, menu) ").lower()

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
                                shopinput = "menu"
                        
                        else:
                            shopinput = "menu"
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
                                shopinput = "menu"
                            else:
                                print(" ")
                                print(f"Upgrading your Maximum damage will cost {shop.max_attack}, but you only have {character.gold}.")
                                print(" ")
                                shopinput = "menu"
                        else:
                            shopinput = "menu"
                    else:
                        shopinput = "menu"  

                if buyinput == "gold gain":
                    print(" ")
                    goldgainconfirm = input(f"You may add 0.1x gold gain for {shop.goldgain} gold. Do you want to continue?: (yes, no) ").lower()
                    if goldgainconfirm == "yes":
                        if (character.gold - shop.goldgain) >= 0:
                            character.gold = character.gold - shop.goldgain
                            character.gold_gain = round((character.gold_gain + .1), 1)
                            print(f"You have paid {shop.goldgain} gold to increase your gold gain. You now have {round(character.gold_gain,1)}x increased gold gain!")
                            shop.goldgain = (shop.goldgain * 1.7)
                            shopinput = "menu"

                        else:
                            print(" ")
                            print(f"You do not have enough gold upgrade your health. You need {shop.goldgain} gold to upgrade, but you have {character.gold} gold.")
                            print(" ")
                            shopinput = "menu"                            
                    else:
                        shopinput = "menu"


    if action == "inventory":
        in_inventory = True
        while in_inventory == True:
            inventory_input = input("You are now looking in your inventory. What would you like to do? (bag, equipped, back) ")

            if inventory_input == "bag":
                print("You are now looking in your bag. You have:")
                inventory.print_bag()


            if inventory_input == "equipped":
                print("")
                print("You are now looking at your equipped items. You have:")
                inventory.print_equipped()
                print("")
                print("")
                equipped_input = input("Would you like to inspect an item, or go back? (inspect, back) ").lower()
                if equipped_input == "inspect":
                    inspect_input = input("Which slot would you like to inspect? (Head, Chest, Shield, Weapon, Legs, Shoes) ").lower()
                    if inspect_input == "head":
                        inventory.inspect_item("head")
                    if inspect_input == "chest":
                        inventory.inspect_item("chest")
                    if inspect_input == "shield":
                        inventory.inspect_item("shield")
                    if inspect_input == "weapon":
                        inventory.inspect_item("weapon")
                    if inspect_input == "legs":
                        inventory.inspect_item("legs")
                    if inspect_input == "shoes":
                        inventory.inspect_item("shoes")         
                    print("")                                                                                               
                    pass

            if inventory_input == "back":
                in_inventory = False   
                print("")
            pass
    pass





# Would you like to view your journey's stats? (Yes/No)
    # Yes? Show death stats
    # No? print("In a hurry I see...")
# Finally: Show death reason.

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