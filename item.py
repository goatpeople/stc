from character import character

class Equip():
    def __init__(self, name, desc, level, max_health, armor, priority, min_attack, max_attack, slot):
        self.name = name
        self.description = desc     
        self.level = level
        self.max_health = max_health
        self.armor = armor
        self.priority = priority
        self.min_attack = min_attack
        self.max_attack = max_attack
        self.slot = slot

    def __repr__(self):
        return self.name

class Inventory(object):
  def __init__(self):
    self.bag = {}
    self.equipped = {
        "Weapon" : None,
        "Shield" : None,
        "Head" : None,
        "Chest" : None,
        "Legs" : None,
        "Shoes" : None,
    }

  def add_item(self, item):
    if item in inventory.bag:
      inventory.bag[item] += 1
    else:
      inventory.bag[item] = 1


  def equip_item(self, item):
    """
    Remove supplied item from the inventory bag (if not already equipped) and
    equip it into the correct slot. Adjusts character's stats as necessary.

    :param item(Equip): the item to equip.
    """
    if item not in inventory.bag:
      slot_item = inventory.equipped[item.slot]
      if slot_item is not None and item.name == slot_item.name:
        print(f"Can't equip: the {item.name} is already equipped as a {item.slot}.")
        return
        
      print(f"Can't equip: you have no {item.name} to equip!")
      return
    if item.level < character.level:
      print(f"This item requires level {item.level}, whereas your character is only level {character.level}.")
      return
      
    slot_item = inventory.equipped[item.slot]
    if slot_item is not None:
      inventory.add_item(slot_item)

      # Removing previously equipped item's stats
      character.max_health -= slot_item.max_health
      character.health -= slot_item.max_health
      # Making sure the character doesn't die as a result of removing a health item
      if character.health <= 0:
        character.health = 1
      character.armor -= slot_item.armor
      character.priority -= slot_item.priority
      character.min_attack -= slot_item.min_attack
      character.max_attack -= slot_item.max_attack

    inventory.bag[item] -= 1
    if inventory.bag[item] == 0:
      del inventory.bag[item]
    inventory.equipped[item.slot] = item

    # Adding the new stats to the character
    character.max_health += item.max_health
    character.armor += item.armor
    character.priority += item.priority
    character.min_attack += item.min_attack
    character.max_attack += item.max_attack


  def print_bag(self):
    """
    Print the contents of the inventory bag.
    """
    print('\t'.join(['Name', 'Qty', ' Slot']))
    print('\t'.join(['----', '---', '------']))
    for item in inventory.bag:
      print('\t'.join([item.name, f"{inventory.bag[item]}", item.slot]))
    print(" ")

  def print_equipped(self):
    print(f"""
                  ______
                 | Head |
                   {inventory.equipped["Head"]}
                 |______|     
            =====  Chest  =====
            |    | {inventory.equipped["Chest"]}     
            |    |      |      |   Shield
    Weapon  |    |      |      |    {inventory.equipped["Shield"]}
    {inventory.equipped["Weapon"]}                        
            |    ========      |
                 | Legs |
                   {inventory.equipped["Legs"]}
                 |      |
                 |      |
            =====  Shoes =====
                   {inventory.equipped["Shoes"]}
    """)  
 
  def inspect_item(self, input):
    cased_input = input.lower().title()
    if cased_input in inventory.equipped:
      item = inventory.equipped[cased_input]
      if item == None:
        print(f'You have nothing equipped in your "{cased_input}" slot.')
        return
      print(f"Name:         {item.name}")
      print(f"Description:  {item.slot}")
    else:
      print(f'Cannot find anything in your "{cased_input}" slot.')

  def __str__(self):
    return self.__repr__()

  def __repr__(self):
    out = "bag: "
    for b in self.bag:
      out + f"{b} {self.bag[b]}"
    return


inventory = Inventory()


# Weapon
spear = Equip(
  name = "Spear",
  desc = "A pointy stick.",
  level = 1,
  max_health = 5,
  armor = 0,
  priority = 10,
  min_attack = 3,
  max_attack = 5,
  slot = "Weapon"
)

rope = Equip(
  name = "Rope",
  desc = "A tangle of plant fibers.",
  level = 2,
  max_health = 10,
  armor = 0,
  priority = 15,
  min_attack = 7,
  max_attack = 9,
  slot = "Weapon"
)

hammer = Equip(
  name = "Hammer",
  desc = "A cracked blacksmith tool.",
  level = 4,
  max_health = 20,
  armor = 0,
  priority = 25,
  min_attack = 8,
  max_attack = 16,
  slot = "Weapon"
)

sword = Equip(
  name = "Sword",
  desc = "A twiggy poker.",
  level = 6,
  max_health = 30,
  armor = 0,
  priority = 40,
  min_attack = 15,
  max_attack = 20,
  slot = "Weapon"
)


# Shield
buckler = Equip(
  name = "Buckler",
  desc = "A small shield, about the size of a quarter.",
  level = 1,
  max_health = 20,
  armor = 3,
  priority = 10,
  min_attack = 0,
  max_attack = 0,
  slot = "Shield"
  )

tower_shield = Equip(
  name = "Tower Shield",
  desc = "The biggest shield there is, too bad you can't move it...",
  level = 4,
  max_health = 50,
  armor = 8,
  priority = 20,
  min_attack = 0,
  max_attack = 0,
  slot = "Shield"
)


# Head
top_hat = Equip(
  name = "Top Hat",
  desc = "You expect yourself to be fancy, but nothing can elevate your class.",
  level = 1,
  max_health = 3,
  armor = 2,
  priority = 5,
  min_attack = 0,
  max_attack = 0,
  slot = "Head"
)

sombrero = Equip(
  name = "Sombrero",
  desc = "Normally a good sun hat, but yours is poked full of holes.",
  level = 3,
  max_health = 8,
  armor = 5,
  priority = 10,
  min_attack = 0,
  max_attack = 0,
  slot = "Head"
)

# Chest
poncho = Equip(
  name = "Poncho",
  desc = "Good for keeping the rain out.",
  level = 1,
  max_health = 0,
  armor = 1,
  priority = 3,
  min_attack = 0,
  max_attack = 0,
  slot = "Chest"
)

chainmail = Equip(
  name = "Chainmail",
  desc = "The rings are made from an apprentice blacksmith. You only grabbed it since it was on sale!",
  level = 4,
  max_health = 10,
  armor = 5,
  priority = 8,
  min_attack = 0,
  max_attack = 0,
  slot = "Chest"
)

bone_chestplate = Equip(
  name = "Bone Chestplate",
  desc = "This chestplate is made from the various bones of... who knows! Let's hope they drank their milk.",
  level = 6,
  max_health = 20,
  armor = 10,
  priority = 20,
  min_attack = 0,
  max_attack = 0,
  slot = "Chest"
)


# Legs
shorts = Equip(
  name = "Shorts",
  desc = "You can feel the breeze run across your legs in these.",
  level = 2,
  max_health = 5,
  armor = 2,
  priority = 5,
  min_attack = 0,
  max_attack = 0,
  slot = "Legs"
)

cloth_pants = Equip(
  name = "Cloth pants",
  desc = "You took these off of someone's clothesline. Gently used?",
  level = 4,
  max_health = 10,
  armor = 5,
  priority = 10,
  min_attack = 0,
  max_attack = 0,
  slot = "Legs"
)

#Shoes
sandals = Equip(
  name = "Sandals",
  desc = "The tag states: Please do not wear socks with these.",
  level = 2,
  max_health = 5,
  armor = 4,
  priority = 5,
  min_attack = 0,
  max_attack = 0,
  slot = "Shoes"
)

leather_boots = Equip(
  name = "Leather Boots",
  desc = 'Your basic shoe, but you have to wonder, what animal made this "leather"?',
  level = 3,
  max_health = 10,
  armor = 8,
  priority = 10,
  min_attack = 0,
  max_attack = 0,
  slot = "Shoes"
)