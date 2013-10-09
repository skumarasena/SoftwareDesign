

def consecutive_doubles():
    """Checks a list of words for three consecutive double letters. Prints any words
    that have three consecutive sets of double letters"""
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        for i in range(len(word)-6):
            if word[i] == word[i+1]:
                if word[i+2] == word[i+3]:
                    if word[i+4] == word[i+5]:
                        print word

consecutive_doubles()


def is_palindrome(s):
    """Checks whether a string is a palindrome. 

    s: string to be checked, of type string
    returns: bool """
    return s == s[::-1]

def odometer_palindrome():
    """Looks for a six-digit integer that solves the Cartalk puzzle from
    Exercise 9.8 in Think Python. Prints the solutions"""
    for i in range(int(1e6), int(1e7)):
        s = str(i)
        if(is_palindrome(s[2:])):
            s = str(i+1)
            if(is_palindrome(s[1:])):
                s = str(i+2)
                if(is_palindrome(s[1:-1])):
                    s = str(i+3)
                    if(is_palindrome(s)):
                        print i

odometer_palindrome()