
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


def reverse_pair():
    """ Prints a list of reverse-pair words.

    Returns: None
    """
    w_list = word_list()
    for i in range(len(w_list)):
        word = w_list[i]
        rev_word = word[::-1]
        if w_list.count(rev_word) > 0:
            print word, rev_word


reverse_pair()
