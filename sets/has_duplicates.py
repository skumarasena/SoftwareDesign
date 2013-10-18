

def has_duplicates(s):
    """Checks whether a given list has duplicates in it. 

    s: list
    returns: bool"""
    return len(s) != len(list(set(s)))


name = 'samantha'
str = 'asdf'
print has_duplicates(list(name))
print has_duplicates(list(str))
