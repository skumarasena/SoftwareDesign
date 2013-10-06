


def rotate_word(s1, n):
    """Rotates a word by a given number of characters.

    s1: string
    n: integer

    Returns: string
    """

    s2 = ''
    for c in s1:
        i = (ord(c)-97+n) % 26
        ch = chr(i+97)
        s2 = s2 + ch
    return s2

print rotate_word('samantha', 20)
