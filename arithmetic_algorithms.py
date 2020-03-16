'''demonstrates how arithmetic functions that map N x N --> N
   can be implemented in Python'''

import math

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

'''The above recursive algorithms can be converted into the following iterative algorithms:'''

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
    '''division is just repeated subtraction:'''
    if a < b:
        return 0
    else:
        return 1 + division(a-b, b)

'''Now that we have covered some important recursive algorithms, we must discuss why current teaching methods are turning off 
   students' brains and making it impossible for them to learn mathematics properly.

   When teaching division, most teachers try to compute both the quotient and the remainder
   at the same time. This causes extreme confusion to students. 
   
   A better way to teach division is to separate these two ideas into two separate functions: a quotient function that 
   computes how many times we can subtract the divisor from the dividend before the result becomes negative,
   and a second function which computes the remainder after doing the subtraction involved in the quotient function.
   In Python, the quotient function is called // and the remainder funciton is called %. Python lets us compute both
   simultaneously using the function named divmod.
   
   This confusion is compounded when teachers tell students to do a division and obtain a single real number instead of two integers.
   For example using the quotient and remainder idea, if we divide 10 by 3, we get a quotient of 3 and a remainder of 1.
   This is simply a shorthand for saying that the follwoing equation is true:

   10 = 3 * 1 + 1.

   The number to the right of 3 is called the quotient, and the number after the plus sign is the remainder. However, teachers then turn 
   around and tell students that they want them to say that 10 divided by 3 is 3.3333333333... . How did we go from obtaining two integers from 
   division to obtaining a single real number that has an infinite decimal expansion?

   A sneaky trick is being played here. If we treat the two inputs as integers, then we can only get a quotient and remainder as the output, which 
   are both integers. However, the teachers are implicilty telling the students to now treat the two inputs as real numbers and do an entirely different
   operation called division of real numbers. It turns out that when we divide one real number by another, we can get a single real number as the output. 
   The algorithm that computes the division of two real numbers is called 'long division' in school. In Programming languages, the former algorithm is known
   as 'integer division' and the latter algorithm is known as 'floating point division.
   
   We cannot claim to understand what is going on here until we can clearly explain how we go from obtaining the tuple (3, 1) from the division of 10 by 3
   to obtaining the single real number 3.3333... from that division.
   
   We need to drill down into the long division algorithm to understand this.

   Recall that given a dividend a and a divisor d, integer division asks us to find TWO integers q and r such that the folloing equation is true:

   a = dq + r. 

   We call q the 'quotient' and r the 'remainder'
   
   'The transition from integer division to division of real numbers occurs when given a dividend a and a divisor d, we insist that the equation:

    a = dq + 0

    for some real number q. 

    Notice that in most cases, q will not be an integer. 
    
    For example, if a = 10 and d = 3, then the equation:

    10 = 3 x q + 0 

    has no integer solutions. 

    However, if we allow q to be a real number, then the equation ALWAYS has a solution. Historically, the real numbers
    were invented for precisely this reason: assuming they exist allows us to solve equations which would otherwise have no
    solution. For example, without real numbers, we cannot solve the following equation:

    x^2 = 1.

    Without real numbers, the above equation has no solution, since it has been known since the Greeks (using a proof by contradiction) 
    that the square root of two cannot be writtne as a rational number involving two integers.
    
    In our example:

    10 = 3 x 3.333333... + 0

    We can now see how long division comes into the picture. We use the quotient and remainder functions when we are
    interested in integer division. We use long division when we are interested in real number division. 

    Apparently, long division has the amazing property that it is able to churn out the real number we are interested in,
    one digit at a time. In other words, the long division allows us to obtain some finite number of digits from a decimal expansion
    that has infinitely many digits. We cannot go very far in mathematics without confronting the idea of infinity.

    We need to understand exaclty how the long division algorithm is able to accomplish this amazing feat.

    We can see how to get from integer division to long division by remembering that integer division invovles repeatedly subtracting
    the quotient from what remains of the original dividend, and keeping track of how many subtraction operations we do, and what remains 
    at the end.

    For example, to divide 10 by 3 using integer division, we do:

    10 - 3 = 7 # quotient so far is 1, remainder so far is 7
    7 - 3 = 4  # quotient so far is 2, remainder so far is 4
    4 - 3 = 1  # quotient so far is 3, remainder so far is 1. 

    We stop here since if we continue subtracting, the result will become negative. 

    Now, subtracting the divisor each time is a bit tedious. It would be more efficient if we instead subtracted *multiples* of the divisor each time. 
    In this case, instead of incrementing the quotient by 1 each time, we could increment by some larger amount each time. 

    We can see why we might want to do this more clearly by considering a case where the dividend is large relative to the divisor. For example, 
    suppose we want to divide 500 by 4. It would clearly be tedious to only subtract 7 each time, since it would take many iterations until we get an answer.

    Instead, we want to subtract *groups* of 4 in batches from whatever remains. It is this idea of subtracting gropus which gives real divison a different flavor
    than integer division. In particular, in the case of integer division, we do not build up the result one digit at a time. However, in the case of real division, 
    we do build up the result one integer at a time. Each time we obtain another digit of the result, we never revise that digit.

    We are now confronted with the following optimization problem: 
    
    What's the best way to group the 4s so that they do the most work and I have to do the least steps?

    The long division algorithm proposes that we only need to look at one digit of the dividend at a time when making these decisions. 

    Furthremore, the long division algorithm claims that we can do this using the integer divsion we already learned.

    In our example, we would first find the shortest sequence of digits starting from the left of 960 that 4 goes into at least once. This is 9. 

    We have the equation:

    9 = 4 x 2 + 1. 

    The key to understanding this is that we are not really talking about 4 and 9, we are talkng about 4 and 900. If we look at the place of the 9, 
    we see that it stands for 900. Thus, the above equation is really shorthand for the equation:

    900 = 4 x 200 + 100. 

    This is why we insist that the 2 is written above the 9. 

    Now that we have the first digit of the quotient, we need to compute how much is left of the original dividend. We do this by subtracting 4 x 200 from 960.

    This gives us 960 - 800 =  160. 

    Instead of repeatedly subtracting 4 from 900 repeatedly and incrementing the quotient by 1 each time, we subtracted 200 groups of 4 from 900 and then incremented
    the quotient by 200. 

    We then continue in the same way, but using what remains of the original dividend:

    160

    To signify that the quotient is 4 and the remainder is 1, we traditionally write a 4 on top, and the remainder below the 4.

    To compute how much is left of the original dividend, we now subtract 4 from 5, etc.

    The long division algorithm makes repeated use of the divmod funciton.

   '''  

def quotient(input1, input2):
    '''returns the quotient when input1 is divided by input2. The quotient is simply a count of how many times we can 
       subtract input2 from input1 until the result becomes negative.'''
    if input2 == 0:
        raise ZeroDivisionError
    quotient_so_far = 0
    remainder_so_far = input1
    while remainder_so_far >= input2:
        remainder_so_far -= input2
        quotient_so_far += 1
    return quotient_so_far

'''we can compute the remainder using the same logic from the above function, except we remove any mention of the quotient,
   and return the remainder instead of the quotient:'''

def remainder(input1, input2):
    '''returns the remainder when input1 is divided by input2'''
    if input2 == 0:
        raise ZeroDivisionError
    remainder_so_far = input1
    while remainder_so_far >= input2:
        remainder_so_far -= input2
        return remainder_so_far

'''the division function taught in school is what Python calls the 'divmod' function. It returns both the quotient and the
   remainder at the same time in the form of a tuple:'''

def quotient_and_remainder(input1, input2):
    '''returns the quotient when input1 is divided by input2. The quotient is simply a count of how many times we can 
       subtract input2 from input1 until the result becomes negative.'''
    if input2 == 0:
        raise ZeroDivisionError
    quotient_so_far = 0
    remainder_so_far = input1
    while remainder_so_far >= input2:
        remainder_so_far -= input2
        quotient_so_far += 1
    return quotient_so_far, remainder_so_far

'''the following version fo the quotient and remainder function is conceptually simpler to understand:'''

def quotient_and_remainder2(input1, input2):
    if input2 == 0:
        raise ZeroDivisionError
    quotient_result = quotient(input1, input2)
    remainder_result = remainder(input1, input2)
    return (quotient_result, remainder_result)

def long_division(numerator, denominator):
    '''returns an arbitrarily long prefix from the corresponding decimal expansion.
        use islice to control the accuracy of the answer.
        See https://bocoup.com/blog/long-division-in-javascript
        '''
    numerator_string = str(numerator)
    numerator_length = len(numerator_string)
    remainder = 0
    quotient_so_far = ''
    i = 0

    while True:
        if i < numerator_length:
            digit = int(numerator_string[i])

        else: 
            digit = 0

        # append a period when the length of the quotient equals the length of the dividend
        if i == numerator_length:
            quotient_so_far = quotient_so_far + "."

        quotient_so_far = quotient_so_far + str(math.floor((digit + (remainder * 10)) / denominator))
        remainder = (digit + (remainder * 10)) % denominator
        i += 1

        yield float(quotient_so_far)

# from itertools import islice

# for digit in islice(long_division(1, 3), 10):
#     print(digit)

def long_multiplication(multiplicand, multiplier):
    '''faster than the repeated addition method, just like long division is faster than the
       repeated subtraction method.'''
    pass

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