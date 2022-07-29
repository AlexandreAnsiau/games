from copy import copy
from json import load
from random import choice
from string import ascii_lowercase


class ScrabbleSet:
    def __init__(self, list_letters=None, letters_indexes={}, dico_words=None):
        self.list_letters = self.get_list_letters(list_letters)
        self.letters_indexes = dict(letters_indexes)
        self._dico_value_letters = self.get_dico_value_letters()
        self._dico_words = self.get_dico_words(dico_words)

    @staticmethod
    def get_dico_value_letters():
        with open("dico_value_letters.json") as file:
            dico = load(file)
        return dico

    @staticmethod
    def get_list_letters(list_letters=None):
        if not list_letters:
            return [choice(ascii_lowercase) for _ in range(10)]
        return list_letters

    @staticmethod
    def get_dico_words(dico_words, encoding="utf8"):
        name_file = "mots_francais.txt" if not dico_words else dico_words
        encoding_file = "windows-1252" if not dico_words else encoding
        return {"name": name_file, "encoding": encoding_file}

    @staticmethod
    def validate_letters_indexes(word, letters_indexes=None):
        valide = True
        if letters_indexes:
            for letter, index in letters_indexes.items():
                if len(word) <= index or word[index] != letter:
                    valide = False
                    break
        return valide

    @staticmethod
    def validate_word(list_letters, word):
        valide = True
        copy_list_letters = copy(list_letters)
        for letter in word:
            if letter not in copy_list_letters:
                valide = False
                break
            else:
                copy_list_letters.remove(letter)
        return valide

    def get_words_possibilities(self):
        with open(self._dico_words["name"], "r",
                  encoding=self._dico_words["encoding"]) as file:
            dict_words = {}
            for word in file:
                word = word.lower().replace("\n", "")
                if self.validate_letters_indexes(word, self.letters_indexes):
                    if self.validate_word(self.list_letters, word):
                        letters = [letter for letter in word]
                        dict_words[word] = sum(
                            [self._dico_value_letters[letter]
                             for letter in letters
                             if self._dico_value_letters.get(letter)])
            list_words = list(dict_words.items())
        return sorted(list_words, key=lambda x: x[1], reverse=True)