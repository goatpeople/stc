# I'll be making comments to explain my thought process
# For clarity on questions, I'll mark them like this:

### QUESTION HERE

class Equip():
  def __init__(self, name, slot):
    self.name = name   
    self.slot = slot

class Inventory(object):    
  def __init__(self):
    self.bag = {}
    self.equipped = {
        "weapon" : "",
        "shield" : "",
    }
inventory = Inventory()

# These are the items that can be equipped and stored in the bag, all with the "weapon" slot. I use that to access the "weapon" key in the 'inventory.equipped' dict.
spear = Equip(
  name = "Spear",
  slot = "weapon"
)
rope = Equip(
  name = "Rope",
  slot = "weapon"
)
hammer = Equip(
  name = "Hammer",
  slot = "weapon"
)
sword = Equip(
  name = "Sword",
  slot = "weapon"
)


def add_item(item):
  if item in inventory.bag:
    inventory.bag[item] += 1
  else:
    inventory.bag[item] = 1


def equip_item(item):
  if item in inventory.bag and inventory.bag[item] > 0:
    # My goal is to remove the currently equipped item and put it back in the bag.

    # I get a KeyError on the 'rope' object for modifying the dictionary twice (If I understand that corrently)
    # This is the issue I am stuck on. I've tried creating a temporary dictionary, modifying that, and returning it, but I doubt I'm doing it correctly.
    # I just don't know how to get around the KeyError without making a mess.

    ### What would a proper function look like to accomplish this goal?
    if inventory.equipped[item.slot] != "":
      removed_item = inventory.equipped[item.slot]
      inventory.bag[removed_item] += 1

    inventory.bag[item] -= 1
    inventory.equipped[item.slot] = item
    
  else:
    print("Item is not in your inventory.")


def print_bag():
  print('\t'.join(['Name', 'Quantity']))
  print('\t'.join(['----', '--------']))

  # My goal here is one of two things:
  # 1) Mainly, to print whatever items are in the bag and the quantity.
  # 2) I thought it would be sneaky to clear all "0" quantity items here, because it would only ever display the bag when it is printing.
  #    That way, the bag doesn't remember what items AREN'T in the bag and it looks cleaner, without removing 0 items from the dictionary

  # I'm not sure if creating a temporary dictionary is a good idea here or not. Like the 'equip_item', I'm trying to get around a KeyError.
  # At this point, I don't know the proper way to be able to modify separate dictionaries and have them operate in unison.
  
  ### Would it be a good idea to clear "0" values in the 'inventory.bag' dict after modifying it in any way (defining like a check_empty function and plugging that in), or clear them only when printing?
  ### Like the 'equip_item' function above (line 46), what would be the proper way to modify a dictionary multiple times without getting a KeyError?

  # I can feel that I am close, but after trying to figure this one issue out for the past week, I've run out of ideas.
  temp_dict = inventory.bag
  for item in inventory.bag:
    if inventory.bag[item] == 0:
      temp_dict = inventory.bag
      temp_dict.pop(item)
      return temp_dict
    print('\t'.join([str(item) for item in [item.name, temp_dict[item]]]))
  

add_item(sword)
add_item(hammer)
add_item(rope)
add_item(spear)

# All four items are in the bag and properly displayed.
print_bag()


# First item is equipped, gets removed from the bag and placed into the 'inventory.equipped' dict with no problem, as expected.
equip_item(spear)
print_bag()
print("")

# This is where we run into the KeyError issue for modifying the dict too many times.
equip_item(rope)
print_bag()

### I created this new file in order to try and import the functions to the 'main' loop, but how does the Inventory class (and item objects) get imported as well?
#   I was having an issue with accessing the items when on a different file. The functions import perfectly, but I don't know if objects are able to be imported. (I hope I am using the terminology correctly!)