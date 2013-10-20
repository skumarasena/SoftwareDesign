
def histogram(s):
    """Uses the dict method 'get' to write histogram more concisely (without
    an if statement).

    s: string
    Returns: dict"""
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def most_frequent(s):
    """Prints letters in decreasing order of frequency.

    s: string
    Returns: None"""
    d = histogram(s)
    
    t = []
    for letter, freq in d.items():
        t.append((freq, letter))
    
    t.sort(reverse = True)
    
    res = []
    for freq, letter in t:
        res.append(letter)

    return res
        

print most_frequent('samantha')
