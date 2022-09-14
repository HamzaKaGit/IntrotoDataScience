### Did you always want to write your own computer game?
In this `Python Object Oriented` Example you'll learn how to use Python Object Oriented Programming to build a small game.
You'll build a tiny implementation of a `Pokemon-like` game that allows you to create little creatures, feed them to gain health, and let them battle against each other. 
#### Concepts Covered
* Python Object Oriented Programming
* Game logic
* Instance methods
* @staticmethod
* Instance attributes, self
* Dunder methods: _init__, __str_
* if _name_ == '__main__'
### Code
````python
class Pokemon:
    def __init__(self, name, primary_type, max_hp):
        self.name = name
        self.primary_type = primary_type  # water, fire, grass
        self.max_hp = max_hp
        self.hp = max_hp

    @staticmethod
    def typewheel(type1, type2):
        result_map = {0 : "lose", 1 : "win", -1 : "tie"}
        # The mapping between moves and numbers
        game_map = {"water": 0, "fire": 1, "grass": 2}
        # Win-lose matrix
        rps_table = [
            [-1, 1, 0],  # water
            [0, -1, 1],  # fire
            [1, 0, -1]   # grass
        ]
        result = rps_table[game_map[type1]][game_map[type2]]
        return result_map[result]
    
    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 1
            print(f"{self.name} recovered 1 HP.")
        else:
            print(f"{self.name} is full.")

    def battle(self, other):
        result = self.typewheel(self.primary_type, other.primary_type)
        if result == 'lose':
            self.hp = 0
            print(f"{self.name} fainted!")
        elif result == 'tie':
            self.hp -= 10
            other.hp -= 10
            print(f"{self.name} and {other.name} battled hard. It's a tie.")
        elif result == 'win':
            other.hp = 0
            print(f"{self.name} won. Congratulations!")

    def __str__(self):
        return f"{self.name} ({self.primary_type}): {self.hp}/{self.max_hp}"


if __name__ == "__main__":
    bulb = Pokemon('bulbasaur', 'grass', 120)
    charm = Pokemon('charmander', 'fire', 110)
    squi = Pokemon('squirtle', 'water', 115)
    breakpoint()
````
