import item

class Monster:
    def __init__(self, name, level, health, max_health, armor, priority, min_attack, max_attack, gold, loot):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = max_health
        self.armor = armor
        self.priority = priority
        self.min_attack = min_attack
        self.max_attack = max_attack
        self.gold = gold
        self.loot = loot


rat = Monster(
    name = "Rat",
    level = 1,
    health = 10,
    max_health = 10,
    armor = 0,
    priority = 5,
    min_attack = 1,
    max_attack = 4,
    gold = 1,
    loot = {item.spear: 5, item.buckler: 5, item.top_hat: 5, item.poncho: 5}
)

slime = Monster(
    name = "Slime",
    level = 2,
    health = 15,
    max_health = 15,
    armor = 0,
    priority = 5,
    min_attack = 2,
    max_attack = 5,
    gold = 2,
    loot = {item.rope: 5, item.shorts: 5, item.sandals: 5}
)

skeleton = Monster(
    name = "Skeleton",
    level = 3,
    health = 20,
    max_health = 20,
    armor = 0,
    priority = 5,
    min_attack = 3,
    max_attack = 6,
    gold = 3,
    loot = {item.leather_boots: 5, item.sombrero: 5}
)

vulture = Monster(
    name = "Vulture",
    level = 5,
    health = 40,
    max_health = 40,
    armor = 0,
    priority = 5,
    min_attack = 7,
    max_attack = 9,
    gold = 5,
    loot = {item.hammer: 5, item.tower_shield: 5, item.cloth_pants: 5, item.chainmail: 5}
)

ogre = Monster(
    name = "Ogre",
    level = 8,
    health = 100,
    max_health = 100,
    armor = 0,
    priority = 5,
    min_attack = 10,
    max_attack = 30,
    gold = 8,
    loot = {item.sword: 5, item.bone_chestplate: 5}
)

