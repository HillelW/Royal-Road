'''demonstrates how arithmetic functions that map N x N --> N
   can be implemented in Python'''


def add_one(number):
    return number + 1

def subtract_one(number):
    return number - 1

'''The below algorithms compute the usual arithmetic functions
   using recursion. 
   
   However, these are too difficult for children to understand.'''

def add_recursive(number1, number2):
    if number2 == 0:
        return number1
    return add_one(add_recursive(number1, subtract_one(number2)))

def multiply_recursive(number1, number2):
    if number2 == 0:
        return 0
    return add(number1, multiply_recursive(number1, subtract_one(number2)))

'''The above recursive algorithms can be converted to the following iterative algorithms:'''

def add(number1, number2):
    sum_so_far = number1
    for _ in range(number2):
        sum_so_far += 1
    return sum_so_far

def multiply(number1, number2):
    product_so_far = number1
    for _ in range(number2 - 1):
        product_so_far = add(product_so_far, number1)
    return product_so_far

'''alternatively, multiplication can be explained by emphasizing
   the way in which two inputs to the multiplicaiton function become
   more than two inputs into the addition function:'''

def generalized_addition(*inputs):
    sum_so_far = 0
    for number in inputs:
        sum_so_far = add(sum_so_far, number)
    return sum_so_far

def multiplication(input1, input2):
    list_of_inputs = [input1 for x in range(input2)]
    return generalized_addition(*list_of_inputs)

def division(a, b):
    '''division is just repeated subtraction - need to write this for integers below and convert to iterative form'''
    if a < b:
        return 0
    else:
        return 1 + division(a-b, b)

'''The above algorithms all compute functions that map N x N --> N.
   However, in grade school, we don't restrict ourselves to such functions.
   Instead, we also consider more general functions that map Z x Z --> Z, 
   where Z is the set of integers. 

   The following recursive algorithms compute addition and subtraction in this more general context:'''

def add_integers(x,y):
    if y > 0:
        return add_integers(x, y-1) + 1
    elif y < 0:
        return add_integers(x, y+1) - 1
    else:
        return x


def subtract_integers(x,y):
    if y > 0:
        return subtract_integers(x, y-1) - 1
    elif y < 0:
        return subtract_integers(x, y+1) + 1
    else:
        return x

def multiply_integers(x, y):
    if x == 0 or y == 0:
        return 0

    elif y < 0:
        return -x + multiply_integers(x, y + 1)

    else: 
        return x + multiply_integers(x, y - 1)

'''todo: convert the new recursive algorithms into iterative form'''
