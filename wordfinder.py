
from random import choice #import the choice method from the random library. Will return a random  element from non-empty sequen

def create_word_list(words):
    file = open(words, 'r')
    word_list=[] #initiliaze empty array where we will append words of the file
    for word in file:
        word_list.append(word.strip()) #the strip method gets rid of the new line character /n
    file.close()
    print(f"{len(word_list)} words read")
    return word_list #want this accessible for the random method in WordFinder method


class WordFinder:
    """Word Finder: finds random words from a dictionary.
    
    """
    ...
    def __init__(self, word_file):
        "initialize your WordFinder instance with a word_file (e.g., 'words.txt') The number of words in the file will be printed"
        self.words = create_word_list(word_file)
    
    def random(self):
        "using the random method, a random word from the word list will be returned"
        return choice(self.words)


def create_filtered_word_list(words):
    file = open(words, 'r')
    word_list=[] #initiliaze empty array where we will append words of the file
    for word in file: #being very specific here...
        word_list.append(word.strip()) #the strip method gets rid of the new line character /n
    file.close()
    for word in word_list:
        if word is '' or word[0] is '#':
            word_list.remove(word)

    print(f"{len(word_list)} words read")
    return word_list #want this accessible for the random method in WordFinder method

class SpecialWordFinder(WordFinder):
    def __init__(self, word_file):
        self.words=create_filtered_word_list(word_file)

    def random(self):
        return choice(self.words)
