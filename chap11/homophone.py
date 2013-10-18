from pronounce import read_dictionary

def homophones(r_dict):
    """Solves Cartalk Puzzler in Exercise 11.11 (Ch. 11 of Think Python). 
    
    r_dict: dict
    Returns: None"""
    for word in r_dict:
        if len(word) == 5:
            word1 = word[1:]
            word2 = word[0] + word[2:]
            if word1 in r_dict and word2 in r_dict:
                pron1 = r_dict[word1]
                pron2 = r_dict[word2]
                if pron1 == pron2:
                    print word



r_dict = read_dictionary()
homophones(r_dict)
