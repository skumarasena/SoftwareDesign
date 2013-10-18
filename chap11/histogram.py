

def orig_histogram(s):
    """Takes a string and makes a histogram of its letters.

    s: string
    Returns: dict"""
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


print orig_histogram('samantha')

def new_histogram(s):
    """Uses the dict method 'get' to write histogram more concisely (without
    an if statement).

    s: string
    Returns: dict"""
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


print new_histogram('samantha')





