from letters import letter_frequency, letter_count

'''
finds the letter with highest frequency in txt file
'''
def highest_freq(file):
    #calls dictionary 'ratiodick' from letters.py
    dict1 = (letter_frequency(letter_count(file)))
    maxval = 0
    letter = ''

    #iterates through dictionary and sets if the value is bigger than the previous value set it to the new max value
    for key in dict1:
        #finds the highest frequency letter in the dictionary and sets it to variables 
        if dict1[key] > maxval: #will keep fist largest number approached if same number is approached again it will default to the first one
            maxval = dict1[key]
            #letter is set to equal key in loop because otherwise it will not return the highest frequency but instead the last letter in the dictionary
            letter = key

    #assert testing        
    expected_tuple = ('i', 0.10952380952380952)
    assert(expected_tuple == (letter,maxval))
    return (letter, maxval)

#test to run code       
#print(highest_freq('hw1\\frost.txt'))
