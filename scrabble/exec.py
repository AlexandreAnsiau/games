from scrabble import ScrabbleSet

list_letters = ["v", "o", "i", "t", "u", "r", "e"]

scrabble_set = ScrabbleSet(list_letters, {"v": 0})

print(scrabble_set.get_words_possibilities())