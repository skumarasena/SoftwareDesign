

def make_key(s):
    """Makes a sorted list of letters in a given word.
    
    s: string
    Returns: string"""
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t

def find_anagrams():
    """Finds all sets of anagrams in 'words.txt'.
    
    Returns: dict of strings"""
    fin = open('words.txt')
    d = {}
    for line in fin:
        word = line.strip()
        key = make_key(word)
        if key not in d:
            d[key] = [word]
        else:
            d[key].append(word)
    return d

def print_anagrams(d):
    """Prints anagram groups.
    
    d: dict
    Returns: None"""
    for key, anag in d.items():
        if len(anag) > 1:
            print key, anag 

#d = find_anagrams()
#print_anagrams(d)

def order_anagrams():
    """Orders anagram pairs by length.
    
    Returns: list of strings"""
    d = find_anagrams()
    
    t = []
    for anag in d.values():
        if len(anag) > 1:
            t.append((len(anag), anag))
    
    t.sort(reverse = True)
    
    res = []
    for l, anag in t:
        res.append(anag)
    return res

#print order_anagrams()


def scrabblegrams():
    """Finds set of 8 letters with largest number of anagrams.

    Returns: string"""
    d = find_anagrams()
    
    t = []
    for key, anag in d.items():
        if len(anag) > 1:
            if len(key) == 8:
                t.append((len(anag), key, anag))
    
    t.sort(reverse = True)
    
    return t[0][1]

print scrabblegrams()
