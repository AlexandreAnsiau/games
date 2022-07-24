class ScrabbleSet:
    def __init__(self, list_letters=None):
        self.list_letters = self.get_list_letters(list_letters)
        self._dico_value_letters = self.get_dico_value_letters()
        
    @staticmethod
    def get_dico_value_letters():
        dico = {
            "d": 2,
            "g": 2,
            "m": 2, 
            "b": 3,
            "c": 3,
            "p": 3, 
            "f": 4,
            "h": 4,
            "v": 4,
            "j": 8,
            "q": 8,
            "k": 10, 
            "w": 10, 
            "x": 10, 
            "y": 10, 
            "z": 10
        }

        for ascii_letter in ascii_lowercase:
            if ascii_letter not in dico:
                dico[ascii_letter] = 1
        return dico
    
    @staticmethod
    def get_list_letters(list_letters=None):
        if not list_letters:
            return [random.choice(ascii_lowercase) for _ in range(10)]
        return list_letters

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
        with open("/Users/Alex/Desktop/mots_francais.txt", "r", encoding="windows-1252") as file:
            dict_words = {}
            for word in file:
                word = word.lower().replace("\n", "")
                letters = [letter for letter in word]
                if self.validate_word(self.list_letters, word):
                    dict_words[word] = sum([self._dico_value_letters[letter] for letter in letters 
                                            if self._dico_value_letters.get(letter)]) 
            list_words = list(dict_words.items())
        return sorted(list_words, key=lambda x: x[1], reverse=True)
