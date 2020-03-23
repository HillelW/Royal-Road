'''
calculus is about functions that take real numbers as input 
and return real numbers as output. 

For example, the following is a standard example of a function 
that is studied in calculus:

f: R --> R,
f(input) = input^2. 

The above function takes any real number as input, and returns 
the square of that number as output. 

To help us reason about such real-valued functions of real inputs, 
we can use sequences. A sequence is function that takes natural numbers 
as inputs and returns a real number as output. 

For example, the following is an example of a sequence:

g: N --> N,
g(input) = input^2. 

Superficially, the functions f and g look similar. However, they are very
different, since we can only plug in natural numbers as inputs into g. For example, 
g(0.5) makes no sense.

Because computers use finite strings of 0s and 1s, they can only represent numbers that 
can be written as finite strings. As a result, if we want to use computers to understand 
real numbers which are infinite strings of 0s and 1s, we can only use APPROXIMATIONS. We will
need to keep this in mind as we proceed. 

We begin our study of the calculus with the notion of an infinite sequence, and the limit of an 
infinite sequence.

To understand the limit of a sequence, we must pay attention to what happens to the output as 
the input becomes arbitrarily large. 

Consider again the function g above. As the input becomes larger and larger, the output also becomes 
arbitrarily large. As a result, the sequence g is not very interesting from this perspective. 
In contrast, consider the following sequence:

 h: N --> N,
 h(input) = 1 / input

 In terms of a set-theoretic definition, h corresponds to the following set of ordered pairs:

 {(input, output) | output = 1/input and input is a natural number greater than 0}.

 as a first pass, we can compute h as follows in Python. We will call it the 'reciprocal function':
'''

def reciprocal(input):
    # only allow natural numbers as inputs
    if type(input) != int or input < 1:
        raise TypeError('Input must be a natural number greater than 0!')
    return 1 / input

'''now that we have our reciprocal function, we want to investigate what happes to the output as the input
   becomes arbitrarily large. We can do this by feeding it larger and larger numbers as input:'''

for input in range(1, 100):
    print(reciprocal(input))

'''
As the input becomes larger and larger, we notice two things:

1. The output becomes smaller and smaller.
2. The output becomes closer and closer to 0. 

In this case, the number 0 functions as a kind of WALL which the outputs of the sequence cannot pass. We
therefore call 0 the LIMIT of this particular sequence.

We can easily come up with other sequences that have non-zero limits. 

For example, consider the following sequence:

h2: N --> N,
h(input) = 1 + (1 / input)

Intuitively, as the input becomes larger and larger, the second term in the sum will go to 0, and we will simply be left with 
some number that is arbitrarily close to 1. In Python, this function cna be computed as follows:

'''

def reciprocal_plus_one(input):
    return 1 + reciprocal(input)

'''if we use a for loop like the one we used to inspect the reciprocal function, we will see that the output of this new
   function becomes arbitrarily close to 1 as the input becomes arbitrarily large. We therefore say that the limit of this sequence
   is 1. 
   
   We use the notation lim input --> infinity f = a to indicate tha the limit of the function f is the number a.

   We can see how a sequence can be related to a real-valued function of a real variable by considering the function:

    h2: R --> R,
    h(input) = 1 / input.

    Notice that h2 has the same limit as h, even though the two functions have different domains. We can verify the limit of h2 using
    the sympy library: 
'''

import sympy as sym

inp = sym.Symbol('input')

sym.limit(1 / inp, inp, sym.oo) # 0

'''likewise, we can compute:'''

expression = 1 + (1 / inp)

sym.limit(expression, inp, sym.oo) # 1

'''The fact that two sequences with different domains can have the same limit 
    will be importnat when we consider the derivative of a real-valued function of a real variable.'''