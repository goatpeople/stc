class Character:
    def __init__(self, name, hometown, level, health, max_health, armor, priority, min_attack, max_attack, gold, gold_gain):
        self.name = name   
        self.hometown = hometown     
        self.level = level
        self.health = health
        self.max_health = max_health
        self.armor = armor
        self.priority = priority
        self.min_attack = min_attack
        self.max_attack = max_attack
        self.gold = gold
        self.gold_gain = gold_gain

    def print_stats(self):
        print(f"""
        Character Stats
        ---------------------
        Current Health: {character.health}
        Maximum Health: {character.max_health}
        Armor:          {character.armor}
        Priority:       {character.priority}
        Minimum Attack: {character.min_attack}
        Maximum Attack: {character.max_attack}
        """)


# Default character stats
character = Character(
    name = "Default",
    hometown = "Default",
    level = 1,
    health = 50,
    max_health = 50,
    armor = 0,
    priority = 10,
    min_attack = 5,
    max_attack = 10,
    gold = 500,
    gold_gain = 1
    )
