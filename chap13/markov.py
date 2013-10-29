"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import string
import random


suffixes = {}

def process_file(filename, skip_header=True):
    """Returns a list of prefixes mapped to suffixes.

    filename: string
   
    Returns: list of words in file
    """
    res =  []
    fp = file(filename)
    
    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        words = line.rstrip().split()
        for word in words:
            res.append(word)
    return res


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_words(w_list):
    """Maps prefixes to suffixes from the given word list.

    w_list: list of strings
    """
    
    for i in range(len(w_list)-2):
        prefix = (w_list[i], w_list[i+1])
        suffix = w_list[i+2]
        if prefix not in suffixes:
            suffixes[prefix] = [suffix]
        else:
            suffixes[prefix].append(suffix)
    return suffixes


def random_text():
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """
    t = []
    first = random.choice(suffixes.keys())
    t.extend(list(first))
    for i in range(200):
        prefix = t[len(t)-2], t[len(t)-1]
        if prefix in suffixes:
            t.append(random.choice(suffixes[prefix]))
        else:
            t.extend(list(random.choice(suffixes.keys())))
    
    return t

def print_text(w_list):
  """Prints text from list.

    w_list: list of words"""
  for word in w_list:
      print word,   
    


if __name__ == '__main__':
    w_list1 = process_file('emma.txt', skip_header = True)
    w_list2 = process_file('tom_sawyer.txt', skip_header = False)
    w_list = w_list1 + w_list2
    
 
    process_words(w_list)
    print_text(random_text())
