import random

'''import math 

math.pi
math.cos(3.1425)


import math as m #shortcut so don't have to type full math
m.pi
m.cos(m.pi)
#make a guess number game


#just specific functionality
from math import pi,cos
cos(pi)


from math import * #* imports everything within math 
    #this could be bad because we do not know everything within the module and it may mess up with code we have written earlier 
'''
#pick a number
correct =  random.randint(1,100)
#untill they guess the number:
attempt = 1
while True:

    #ask user  to guess number
    #validate input
    guess = int(input("enter number between 1 and 100: "))

    #if too low - 'print' ''too low''
    if guess > correct:
        print('too high')
    # if too high print too high
    elif guess < correct:
        print('too low')
    else:
        break
    attempt = attempt + 1
print("Guessed {} in {} guess".format(correct, attempt))
#haven't 
#print out nice message
#parameterized max and min
#validated user input