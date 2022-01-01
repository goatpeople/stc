class Equip():
  def __init__(self, name, desc, level, max_health, armor, priority, min_attack, max_attack, slot):
    self.name = name   
    self.description = desc   
    self.level_requirement = level
    self.max_health = max_health
    self.armor = armor
    self.priority = priority
    self.min_attack = min_attack
    self.max_attack = max_attack
    self.slot = slot



class Inventory(object):    
  def __init__(self):
    self.bag = {}

  def add_item(self, item):
    if item in self.bag:
      self.bag[item] += 1
    else:
      self.bag[item] = 1

  def print_bag(self):
    print('\t'.join(['Name', 'Quantity']))
    print('\t'.join(['----', '--------']))
    for item in inventory.bag:
      print('\t'.join([str(x) for x in [item.name, inventory.bag[item]]]))




spear = Equip(
  name = "Spear",
  desc = "A pointy stick",
  level = 1,
  max_health = 0,
  armor = 0,
  priority = 0,
  min_attack = 3,
  max_attack = 4,
  slot = "weapon"
)
rope = Equip(
  name = "Rope",
  desc = "A pointy stick",
  level = 1,
  max_health = 0,
  armor = 0,
  priority = 0,
  min_attack = 3,
  max_attack = 4,
  slot = "weapon"
)

item_list = [spear, rope]

inventory = Inventory()

inventory.add_item(spear)
inventory.add_item(spear)
inventory.add_item(rope)
inventory.add_item(spear)
inventory.add_item(spear)
inventory.add_item(spear)
inventory.add_item(spear)
inventory.add_item(spear)
print(inventory.bag)
inventory.print_bag()

playerinput = input("input: ")

