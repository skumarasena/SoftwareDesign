


def rotate_word(s1, n):
    s2 = ''
    for c in s1:
        i = (ord(c)-97+n) % 26
        ch = chr(i+97)
        s2 = s2 + ch
    return s2

print rotate_word('samantha', 20)
