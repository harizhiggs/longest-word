import random
import string
import requests

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
        return self.__check_dictionary(word)

    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        return json_response['found']

"""
game = Game()
print(f"Grid: {game.grid}")
my_word = "SHOE"
result = game.is_valid(my_word)
print(f"The word '{my_word}' is valid: {result}")
"""

new_game = Game()
new_game.grid = list('KWIENFUQW')
my_word = "FUQ"
result = new_game.is_valid(my_word)
print(f"The word '{my_word}' is valid: {result}")
