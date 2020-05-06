#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the crosswordPuzzle function below.
def crosswordPuzzle(crossword, words):
    word_dict = defaultdict(list)
    word_list = sorted(words.split(";"))
    for word in word_list:
        word_dict[len(word)].append(word)

    for i in range(10):
        for j in range(10):
            if crossword[i][j] ='-'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
