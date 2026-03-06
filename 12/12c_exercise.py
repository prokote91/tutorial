class Human:
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack

    def current_health(self):
        return f"current health: {self.health}"

    def current_attack(self):
        return f"current attack: {self.attack}"

    def heal_buff(self, amount):
        if amount > 0:
            self.health += amount
            return f"healed {amount}. Current health is {self.health}"
        else:
            return "failed"

    def attack_buff(self, amount):
        if amount > 0:
            self.health == amount
            return f"buffed by {amount}. current attack is {self.attack}"
        else:
            return " failed"


Human1 = Human(100, 120)
print(Human1.current_health())
print(Human1.current_attack())
print(Human1.heal_buff(20))
print(Human1.attack_buff(40))
