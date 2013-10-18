

def list_intersection(s1, s2):
    """Returns the intersection of two sets.

    s1: set
    s2: set
    returns: list"""
    return list(s1 & s2)


s = set(list('samantha'))
a = set(list('anne'))

print list_intersection(s, a)
