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
    equip it into the correct slot.

    :param item(Equip): the item to equip.
    """
    if item not in inventory.bag:
      slot_item = inventory.equipped[item.slot]
      if slot_item is not None and item.name == slot_item.name:
        print(f"Can't equip: the {item.name} is already equipped as a {item.slot}.")
        return
        
      print(f"Can't equip: you have no {item.name} to equip!")
      return

    slot_item = inventory.equipped[item.slot]
    if slot_item is not None:
      inventory.add_item(slot_item)

    inventory.bag[item] -= 1
    if inventory.bag[item] == 0:
      del inventory.bag[item]
    inventory.equipped[item.slot] = item


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
    

inventory = Inventory()

spear = Equip(
  name = "Spear",
  desc = "A pointy stick",
  level = 0,
  max_health = 0,
  armor = 0,
  priority = 0,
  min_attack = 0,
  max_attack = 0,
  slot = "Weapon"
)

rope = Equip(
  name = "Rope",
  desc = "A tangle of plant fibers",
  level = 0,
  max_health = 0,
  armor = 0,
  priority = 0,
  min_attack = 0,
  max_attack = 0,
  slot = "Weapon"
)

hammer = Equip(
  name = "Hammer",
  desc = "A cracked blacksmith tool",
  level = 0,
  max_health = 0,
  armor = 0,
  priority = 0,
  min_attack = 0,
  max_attack = 0,
  slot = "Weapon"
)

sword = Equip(
  name = "Sword",
  desc = "A twiggy poker",
  level = 0,
  max_health = 0,
  armor = 0,
  priority = 0,
  min_attack = 0,
  max_attack = 0,
  slot = "Weapon"
)