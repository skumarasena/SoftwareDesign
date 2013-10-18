


def avoids(word, letters):
    return set(list(word)).isdisjoint(set(list(letters)))


word = 'qwerty'
letters = 'asdfg'

print avoids(word, letters)
