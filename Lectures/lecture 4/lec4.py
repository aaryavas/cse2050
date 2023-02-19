#Test driven development
'''
Red 
1) Run a test
2) run the ttest to verify 
        a) it fails
        
        '''
''' 
Green
Modify the code to pass the test 
'''

''' 
Refactor/Blue

Refactor redundant code

'''

'''
writing test case first helps you better write your functions in an optimal effiecent way
encapsulated 
you know if your code works 

'''

def factorial(x):
    #return factorial of x

    #is x an int?

    

    #is x >= 1
    print('testing factorial(5)')
    assert factorial(5)== 120


    print('testing factiorial(1.3)')

    try:
        factorial(1.3)
        raise AssertionError('factorial(1.3) did not work')

    except ValueError:
        pass


    product =1

    while x > 1: 
        product *= x

assert factorial(5) == 120