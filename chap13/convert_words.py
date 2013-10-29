import string

def convert_words(filename):
    """Strips words in file of whitespace and punctuation.

    filename: string
    Returns: list of strings"""
    fin = open(filename)
    s = string.whitespace + string.punctuation
    
    w_list = []
    for line in fin:
        for c in s:
            if c in line:
                w = line.replace(c, '')
                word = w.strip()
        w_list.append(word.lower())
    return w_list

print convert_words('strings.txt')
