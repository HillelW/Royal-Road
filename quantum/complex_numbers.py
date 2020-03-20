import math
from functools import reduce


def linear_combination(list_of_vectors, list_of_scalars):
    '''given several lists of Complex objects, or several ComplexVectors, and a list of scalars,
       returns the corresponding linear combination
    
      v1 = [Complex(-1,0), Complex(0,7), Complex(2,0)]
      v2 = [Complex(0,0), Complex(2,0), Complex(4,0)]
      list_of_vectors = [v1, v2]
      list_of_scalars = [1, 2]
      linear_combination(list_of_vectors, list_of_scalars)

      or:

      v1 = ComplexVector([Complex(-1,0), Complex(0,7), Complex(2,0)])
      v2 = ComplexVector([Complex(0,0), Complex(2,0), Complex(4,0)])
      list_of_vectors = [v1, v2]
      linear_combination(list_of_vectors, [1,2])
    '''
    length = len(list_of_vectors[0])
    vectors_and_scalars = list(zip(list_of_vectors, list_of_scalars))
    scaled_vectors = []
    for vector_scalar in vectors_and_scalars:
        scalar = vector_scalar[-1]
        vector = vector_scalar[:-1][0]
        new_vector = [u.scalar_multiplication(scalar) for u in vector]
        scaled_vectors.append(new_vector)
    vectors_to_add = [(x[0], x[1]) for x in list(zip(*scaled_vectors))]
    answer= []
    for i in range(length):
        answer.append(reduce(Complex.__add__, vectors_to_add[i]))
    return answer

class Complex():
    '''represents a complex number'''
    def __init__(self, x, y=0.0):
        self.x = x
        self.y = y
     
    def __add__(self, other):
        '''returns the sum of two complex numbers'''
        return Complex(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        '''returns the result of subtracting this complex number from antoher complex number'''
        return Complex(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        '''returns the product of two complex numbers'''
        return Complex(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)
     
    def __truediv__(self, other):
        '''returns the quotient of two complex numbers using the complex conjugate of the denominator'''
        numerator = self * other.complex_conjugate()
        denominator = other * other.complex_conjugate()
        return numerator.scalar_multiplication(1/denominator.x)

    def scalar_multiplication(self, scalar):
        '''returns the result of scalar multiplciaiotn of this Copmlex object with a scalar value'''
        return Complex(scalar * self.x, scalar * self.y)
    
    def complex_conjugate(self):
        '''returns the result of complex conjugation'''
        return Complex(self.x , -self.y)
    
    def modulus(self):
        '''returns the magnitude of this complex number'''
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def modulus_squared(self):
        '''returns the squared magnitude of this complex number as a single, real number'''
        return (self * self.complex_conjugate()).x

    def __neg__(self):
        '''returns the negation of this complex number'''
        return Complex(-self.x, -self.y)

    def __eq__(self, other, epsilon=0.1):
        '''returns True if each component falls within the epsilon band, False otherwise.
        
        c1 = Complex(2.001, -5.001)
        c2 = Complex(2, -5)
        c1 == c2 # True
        '''
        return abs(self.x - other.x) < epsilon and abs(self.y - other.y) < epsilon
    
    def __str__(self):
        return f'{self.x} + {self.y}i'
    
    def __repr__(self):
        return f'({self.x}, {self.y})'

class ComplexVector():
    '''represents a list of Copmlex objects'''
    def __init__(self, list_of_complex_numbers):
        self.list_of_complex_numbers = list_of_complex_numbers
        self.current_index = 0

    def __add__(self, other):
        '''returns the sum of two complex vectors'''
        pairs = zip(self, other)
        return ComplexVector([u + v for (u, v) in pairs])

    def __sub__(self, other):
        '''returns the result of subtracting this complex vector from antoher complex vector'''
        pairs = zip(self, other)
        return ComplexVector([u - v for (u, v) in pairs])

    def __mul__(self, other):
        '''returns the component-wise product of two complex vectors'''
        pairs = zip(self, other)
        return ComplexVector([u * v for (u, v) in pairs])

    def __truediv__(self, other):
        '''returns the component-wise division of two complex vectors'''
        pairs = zip(self, other)
        return ComplexVector([u / v for (u, v) in pairs])

    def inner_product(self, other):
        pass

    def scalar_multiplication(self, scalar):
        '''returns the component-wise scalar multiplication of two complex vectors'''
        return ComplexVector([u.scalar_multiplication(scalar) for u in self.list_of_complex_numbers])
    
    def complex_conjugate(self):
        '''returns the component-wise complex-conjugate of a complex vector'''
        return ComplexVector([u.complex_conjugate() for u in self.list_of_complex_numbers])

    def __len__(self):
        return len(self.list_of_complex_numbers)

    def __iter__(self):
        '''allows complex vectors to be used with the zip() function'''
        return (x for x in self.list_of_complex_numbers)

    def __next__(self):
        '''allows complex vectors to be used in for loops'''
        try: 
            current = self.list_of_complex_numbers[self.current_index]
        except IndexError:
            raise StopIteration
        self.current_index += 1
        return current
        
    def __str__(self):
        list_of_strings = [str(c) for c in self.list_of_complex_numbers]
        return '[' + ','.join(list_of_strings) + ']'
     
    def __repr__(self):
        list_of_strings = [repr(c) for c in self.list_of_complex_numbers]
        return '[' + ','.join(list_of_strings) + ']'