
def word_dict():
    """Creates a dict of whitespace-stripped words from a file named 'words.txt'

    Returns: dict of strings
    """
    fin = open('words.txt')
    w_dict = {}
    for line in fin:
        word = line.strip()
        w_dict[word] = word
    return w_dict


def rotate_word(s1, n):
   """Rotates a word by a given number of letters.

    s1: string
    n: int
    Returns: string"""
   s2 = ''
   for c in s1:
       i = (ord(c)-97+n) % 26
       ch = chr(i+97)
       s2 = s2 + ch
   return s2

def rotate_pairs(w_dict, n):
    """Prints all rotate pairs in a given list of words.

    w_dict: dict
    n: int
    Returns: None"""
    for word in w_dict:
        if rotate_word(word, n) in w_dict:
            print word, rotate_word(word, n)


w_dict = word_dict()
rotate_pairs(w_dict, 13)
