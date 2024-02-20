import random
import string

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True

"""
game = Game()
print(f"Grid: {game.grid}")
my_word = "SHOE"
result = game.is_valid(my_word)
print(f"The word '{my_word}' is valid: {result}")
"""

new_game = Game()
new_game.grid = list('KWIENFUQW')
my_word = "FEUN"
result = new_game.is_valid(my_word)
print(f"The word '{my_word}' is valid: {result}")
