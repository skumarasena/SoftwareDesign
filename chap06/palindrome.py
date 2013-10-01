"""Module that provides is_palindrome.

Author of is_palindrome: Samantha Kumarasena
"""

def first(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[0]


def last(word):
    """Returns the *last* character of a word.

    word: string

    returns: length 1 string
    """
    return word[-1]


def middle(word):
    """Returns all but the first and last character of a word.

    word: string

    returns: string
    """
    return word[1:-1]


def is_palindrome(word):
    """Returns True if 'word' is a palindrome. Returns False otherwise.

    word: string
    
    returns: True/False."""

    if(len(word) == 0):
        return True
    elif last(word) != first(word):
        return False
    return is_palindrome(middle(word))

print(is_palindrome('anna'))
print(is_palindrome('ana'))
print(is_palindrome('samantha'))
