from copy import copy
from json import load
from random import choice
from string import ascii_lowercase


class ScrabbleSet:
    def __init__(self, list_letters=None, letters_indexes={},
                 dico_words="dico_words/french_words.txt"):
        """
        Parameters
        ----------
        list_letters: list
            The list of letters the player get.
        letters_indexes: dict
            A dictionary containing one or several letters present in list_letters
            with their index in researched word.
        dico_words: str
            The name of the file containing the list of the words which will be
            used to find the valid words.
        """
        self.list_letters = self.get_list_letters(list_letters)
        self.letters_indexes = dict(letters_indexes)
        self._dico_value_letters = self.get_dico_value_letters()
        self._dico_words = self.get_dico_words(dico_words)

    @staticmethod
    def get_dico_value_letters():
        """
        Return
        ------
        dict
            The dictionary which contains the value of the letters.
        """
        with open("dico_value_letters.json") as file:
            dico = load(file)
        return dico

    @staticmethod
    def get_list_letters(list_letters=None):
        """
        If any list of letters is not utilized, one random list will be generated.

        Parameters
        ----------
        list_letters: list
            The list of letter the player get.

        Return
        ------
        list
            The list of letter utilized to play the scrabble
        """
        if not list_letters:
            return [choice(ascii_lowercase) for _ in range(10)]
        return list_letters

    @staticmethod
    def get_dico_words(dico_words, encoding="utf8"):
        """
        This function is used to target the file where the words must be
        searched.

        Parameters
        ----------
        dico_words: str
            The name of the file containing the list of the words which will be
            used to find the valid words.
        encoding: str
            The encoding format of the file given for the dico_words parameter

        Return
        ------
        dict
            A dictionary containing the name and the encoding of the file where
            the words must be searched.
        """
        return {"name": dico_words, "encoding": encoding}

    @staticmethod
    def validate_letters_indexes(word, letters_indexes=None):
        """
        Parameter
        ---------
        word: str
            The inspected word.
        letters_indexes: dict
            A dictionary containig the letters and the index where they must be
            placed in the word

        Return
        ------
        bool:
            if the index of the letters in the word is the same as the those
            indicate in the letters_indexes parameters, it will return True.
        """
        valide = True
        if letters_indexes:
            for letter, index in letters_indexes.items():
                if len(word) <= index or word[index] != letter:
                    valide = False
                    break
        return valide

    @staticmethod
    def validate_word(list_letters, word):
        """
        This function will validate the word if it contains all are some the
        letters presents in the list_letters parameter. Attention, the word
        can not contain letter that are not mention in the list_letters parameter.

        Parameter
        ---------
        list_letters: list
            The list of the letters the player receive.
        word: str
            The inspected word.

        Return
        ------
        bool:
            It will return True if the word contain only letters mention in
            the list_letters parameter.
        """
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
        """
        This method will return the list of the valid word and the points the
        player will win with each possible word.

        Return
        ------
        list
            The list containing tuple with word and the points win with this
            one. This list is sorted decreasingly according the points.
        """
        with open(self._dico_words["name"], "r",
                  encoding=self._dico_words["encoding"]) as file:
            dict_words = {}
            for word in file:
                word = word.lower().replace("\n", "")
                if self.validate_letters_indexes(word, self.letters_indexes):
                    if self.validate_word(self.list_letters, word):
                        dict_words[word] = sum(
                            [self._dico_value_letters.get(letter, 0)
                             for letter in word])
            list_words = list(dict_words.items())
        return sorted(list_words, key=lambda x: x[1], reverse=True)