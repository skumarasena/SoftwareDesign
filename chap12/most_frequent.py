
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
    Returns: list of strings"""
    d = histogram(s)
    
    t = []
    for letter, freq in d.items():
        t.append((freq, letter))
    
    t.sort(reverse = True)
    
    res = []
    for freq, letter in t:
        res.append(letter)

    return res


 
def most_frequent2(s):
    """New version of most_frequent: prints letters in decreasing
    order of frequency.
    
    s: string
    Returns: list of strings"""
    return sorted(tuple(histogram))
        

print most_frequent('samantha')
