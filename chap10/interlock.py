

def word_list():
    """Creates a list of whitespace-stripped words from a file named 'words.txt'

    Returns: list of strings
    """
    fin = open('words.txt')
    w_list = []
    for line in fin:
        word = line.strip()
        w_list.append(word)
    return w_list

def is_in_list(w_list, word):
    """Checks whether a given word is in the list.

    w_list: list of strings
    word: string
    Returns: bool
    """
    for w in w_list:
        if w == word:
            return True
    return False

def is_interlock(w_list, word):
    """Checks whether a word is made up of two interlocking words.
   
    word_list: a list of strings
    word: string
    Returns: bool
    """
    even = word[::2]      #even-numbered characters in word
    odd = word[1::2]      #odd-numbered characters in word

    is_even = is_in_list(w_list, even)       #are the even-numbered characters a word?
    is_odd = is_in_list(w_list, odd)         #are the odd-numbered characters a word?
    return is_even and is_odd


def print_interlockers(w_list):
    """Prints all interlocking words (and their component words) from a word list.
    
    word_list: list of strings
    Returns: None
    """
    for i in range(len(w_list)):
        word = w_list[i]
        if is_interlock(w_list, word):
            print word, word[::2], word[1::2]


w_list = word_list()
print_interlockers(w_list)
