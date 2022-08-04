"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """Finds random word in file

    >>> wf = WordFinder("animals.txt")

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """
    def __init__(self, file):
        file = open(file)
        self.words = self.filter(file)

    def filter(self, file):
        """Returns just the words from the file"""

        return [word.strip() for word in file]

    def random(self):
        """Returns random word from file"""

        return choice(self.words)

class SpecialWordFinder(WordFinder):
    """Finds random words in files that contain empty lines & comments

    >>> swf = SpecialWordFinder("food.txt")

    >>> swf.random() in ["kale", "apple", "mango"]
    True

    >>> swf.random() in ["parsnips", "apple", "mango"]
    True
    """
    def filter(self, file):
        """Filters out comments and empty lines"""

        return [word.strip() for word in file if word.strip() and not word.startswith("#")]
