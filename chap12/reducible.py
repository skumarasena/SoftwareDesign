


def word_dict():
    """Creates a dict of whitespace-stripped words from a file named 'words.txt'

    Returns: dict of strings
    """
    fin = open('words.txt')
    print fin
    w_dict = {}
    for line in fin:
        word = line.strip()
        w_dict[word] = word
    
    w_dict['a'] = 'a'
    w_dict['i'] = 'i'
    w_dict[''] = ''
    return w_dict



def children(word, w_dict):
    """Returns a list of all the words that can be formed by removing one 
    letter from word.
    
    word: string
    word_dict: dict of strings
    Returns: list of strings"""
    
    res = []
    for i in range(len(word)):
        s = list(word)
        s.remove(s[i])
        child = ''.join(s)
        if child in w_dict:
            res.append(child)
    return res


memo = {}
memo[''] = ['']

def is_reducible(word, w_dict):
    """Returns list of children if word is reducible.

    word: string
    w_dict: dict of strings
    Returns: list of strings"""
    if word in memo:
        return memo[word]
    
    res = []
    for child in children(word, w_dict):
        if is_reducible(child, w_dict):
            res.append(child)
            
    memo[word] = res
    return res

def reducibles(w_dict):
    """Returns a list of all the reducible words in 'words.txt'.
    
    w_dict: dict of strings
    Returns: list of strings"""
    res = []
    for word in w_dict:
        s = is_reducible(word, w_dict)
        if s != []:
            res.append(word)
    return res


#w_dict = word_dict()
#print reducibles(w_dict)

def biggest_reducible(w_dict):
    """Returns the largest reducible word in w_dict.

    w_dict: dict of strings
    Returns: string"""
    red = reducibles(w_dict)
    
    t = []
    for word in red:
        t.append((len(word), word))

    t.sort(reverse = True)
    
    return t[0][1]
        
w_dict = word_dict()
print biggest_reducible(w_dict)
