'''Fraction class: 

   The numerator can be any integer. 
   The denominator can be any integer greater than 0 
   (negative fractions have a negative numerator).
   
   It happens to be that we can obtain a real number by dividing the numerator
   by the denominator. However, we will not do this, since it is extremely confusing for children.
   Instead, any fraction operation will return anohter fraction object as output. In other words, 
   we will not treat the horizontal line that separates the numerator from the denominator as a division operation.

   See https://codereview.stackexchange.com/questions/83322/fraction-class-in-python
'''

def gcd(m,n):
    '''used to find common denominator when adding two fractions'''
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

class Fraction:
    def __init__(self, numerator, denominator):
        greatest_factor = Fraction.gcd(numerator, denominator)

        self.numerator = numerator // greatest_factor
        self.denominator = denominator // greatest_factor
        
        # denominator cannot be negative
        if self.denominator < 0:
            self.denominator = abs(self.denominator)
            self.numerator = -1 * self.numerator

        # denominator cannot be 0
        elif self.denominator == 0:
            raise ZeroDivisionError

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def simplify(numerator, denominator):
        '''returns an eqivalent but simpler Fraction by finding the GCD of the numerator and denominator,
           then dividing both by the GCD.'''
        greatest_factor = Fraction.gcd(numerator, denominator)
        return Fraction(numerator // greatest_factor, denominator // greatest_factor)

    def __add__(self,other):
        '''returns the sum in simplified form'''
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction.simplify(new_numerator, new_denominator)

    def __sub__(self, other):
        '''returns the difference in unsimplified form'''
        return Fraction.simplify(self.numerator * other.denominator - self.denominator * other.numerator, self.denominator * other.denominator)

    def __mult__(self, other):
        '''returns the product in unsimplified form'''
        return Fraction.simplify(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        '''returns the quotient in unsimplified form'''
        return Fraction.simplify(self.numerator * other.denominator, self.denominator * other.numerator)

    def __iadd__(self,other):
        '''returns the sum in simplified form'''
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction.simplify(new_numerator, new_denominator)

    def __isub__(self, other):
        '''returns the difference in unsimplified form'''
        return Fraction.simplify(self.numerator * other.denominator - self.denominator * other.numerator, self.denominator * other.denominator)

    def __imult__(self, other):
        '''returns the product in unsimplified form'''
        return Fraction.simplify(self.numerator * other.numerator, self.denominator * other.denominator)

    def __itruediv__(self, other):
        '''returns the quotient in unsimplified form'''
        return Fraction.simplify(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __le__(self, other):
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __invert__(self):
        '''returns a fraction where the numerator is the previous denominator and vice-versa'''
        return Fraction(self.denominator, self.numerator)

    def __abs__(self):
        return Fraction(abs(self.denominator), abs(self.numerator))

    def __repr__(self):
        return str(self.numerator) + "/" + str(self.denominator)