from scrabble import ScrabbleSet

list_letters = ["a", "b", "o", "u", "t"]

scrabble_set = ScrabbleSet(list_letters, {"a": 2}, "english_words.txt")

print(scrabble_set.get_words_possibilities())