import random

class Rule():

    def __init__(self):
        self.inWord = [False for i in range(5)]
        self.inLoc = [False for i in range(5)]
        self.words = Rule.load_file('Data\wordle_words.txt')
        self.SECRET = random.choice(self.words)
    
    def solve(self, word):
        self.inWord = [False for i in range(5)]
        self.inLoc = [False for i in range(5)]
        if self.SECRET == ''.join(word):
            self.inWord = [True for i in range(5)]
            self.inLoc = [True for i in range(5)]
            return True, self.inWord, self.inLoc
        else:
            secret = [s for s in self.SECRET]
            for i in range(len(word)):
                if word[i] == self.SECRET[i]:
                    self.inLoc[i] = word[i] == self.SECRET[i]
                    secret[i] = ' '
            for i in range(len(word)):
                self.inWord[i] = word[i] in secret

            return False, self.inWord, self.inLoc

    def load_file(path):
        words = []
        with open(path, 'r') as f:
            for line in f.readlines():
                word = line.strip().upper()
                words.append(word)
        return words
    def get_secret(self):
        return self.SECRET

    def isValidWord(self, word):
        return word in self.words


  
