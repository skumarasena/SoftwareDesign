

def reverse_lookup1(d, v):
    """Original reverse_lookup, which finds the first dict key that maps
    to a given value. 

    d: dict
    v: value type
    Returns: key type"""
    for k in d:
        if d[k] == v:
            return k
    raise ValueError

def reverse_lookup2(d, v):
    """New reverse_lookup, which finds all dict keys that map to a given value.
    
    d: dict
    v: value type
    Returns: list"""
    s = []
    for k in d:
        if d[k] == v:
            s.append(k)
    return s

name = {'a': 3, 'h': 1, 'm': 1, 'n': 1, 's': 1, 't': 1}
print reverse_lookup2(name, 1)
