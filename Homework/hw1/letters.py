import string
def letter_count(file):
    '''
    dictionary for counting the amount of each letter occurs 
    and putting that amount in a list
    '''
    dict_letters = {}
    with open(file, 'r') as f:
        txtstr = f.read().replace('\n','')
        #turns into list of string
        txtstr = txtstr.split(' ')
        txtstrnew = list(''.join(txtstr))

        #make all lowercase
        txtstrnew = [letter.casefold() for letter in txtstrnew]

        #turns into list of characters
        for char in txtstrnew:

            #removes all non-ascii values
            if char in string.ascii_lowercase:
                if char in dict_letters:    
                    dict_letters[char] += 1
                else:
                    dict_letters[char] = 1

    #assert testing                 
    expected_dict = {'f': 12, 'i': 23, 'r': 14, 'e': 23, 'a': 13, 'n': 9, 'd': 10, 'c': 6, 's': 14, 'o': 20, 'm': 3, 'y': 3, 't': 20, 'h': 12, 'w': 8, 'l': 6, 'v': 2, 'b': 2, 'u': 5, 'p': 1, 'k': 2, 'g': 2}
    assert(expected_dict == (dict_letters))
    return dict_letters


#test to run code    
#print(letter_count('hw1\\frost.txt'))

'''
finds the ratio of frequency of the letter to total amount of letters in the text
'''
def letter_frequency(dict_letters):
    totalchar =0
    ratiodict = {}

    #finds total characters used
    for key in dict_letters:
        totalchar += dict_letters[key]

    #finds frequency ratio
    for key in dict_letters:
        ratiodict[key] = dict_letters[key]/totalchar

    #assert testing 
    expectedfreq = {'f': 0.05714285714285714, 'i': 0.10952380952380952, 'r': 0.06666666666666667, 'e': 0.10952380952380952, 'a': 0.06190476190476191, 'n': 0.04285714285714286, 'd': 0.047619047619047616, 'c': 0.02857142857142857, 's': 0.06666666666666667, 'o': 0.09523809523809523, 'm': 0.014285714285714285, 'y': 0.014285714285714285, 't': 0.09523809523809523, 'h': 0.05714285714285714, 'w': 0.0380952380952381, 'l': 0.02857142857142857, 'v': 0.009523809523809525, 'b': 0.009523809523809525, 'u': 0.023809523809523808, 'p': 0.004761904761904762, 'k': 0.009523809523809525, 'g': 0.009523809523809525}
    assert(expectedfreq == (ratiodict))

    return ratiodict

#test to run code    
#print(letter_frequency(letter_count('hw1\\frost.txt')))




