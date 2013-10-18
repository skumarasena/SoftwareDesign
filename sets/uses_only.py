

def uses_only(word, letters):
    """Ensures that a word is made up only of the letters in 'letters'.

    word: string
    letters: string
    Returns: bool"""
    return set(list(word)) <= set(list(letters))
    
word = 'sam'
letters = 'samantha'
print uses_only(word, letters)
