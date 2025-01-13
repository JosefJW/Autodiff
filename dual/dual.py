from numbers import Number
import math
import numpy as np
import sys

class Dual(Number):
    """
    A class representing dual numbers, which are a type of hypercomplex number.
    Dual numbers are composed of a real part and a dual part, where the dual part is
    often used in automatic differentiation to represent derivatives or infinitesimal values.

    Attributes:
        real (float): The real component of the dual number.
        dual (float): The dual component of the dual number.

    Methods:
        __add__(self, other): Adds two dual numbers or a dual number and a scalar.
        __radd__(self, other): Right-hand addition of a dual number and a scalar.
        __iadd__(self, other): In-place addition of a dual number and another dual number or scalar.
        __sub__(self, other): Subtracts two dual numbers or a dual number and a scalar.
        __rsub__(self, other): Right-hand subtraction of a dual number and a scalar.
        __isub__(self, other): In-place subtraction of a dual number and another dual number or scalar.
        __mul__(self, other): Multiplies two dual numbers or a dual number and a scalar.
        __rmul__(self, other): Right-hand multiplication of a dual number and a scalar.
        __imul__(self, other): In-place multiplication of a dual number and another dual number or scalar.
        __truediv__(self, other): Divides two dual numbers or a dual number and a scalar.
        __rtruediv__(self, other): Right-hand division of a dual number and a scalar.
        __itruediv__(self, other): In-place division of a dual number and another dual number or scalar.
        __pow__(self, exponent): Raises a dual number to a scalar or dual number exponent.
        __rpow__(self, other): Right-hand power of a dual number and a scalar.
        __ipow__(self, other): In-place exponentiation of a dual number by a scalar or dual number.
        __eq__(self, other): Compares if two dual numbers are equal.
        __ne__(self, other): Compares if two dual numbers are not equal.
        __neg__(self): Negates a dual number.
        __pos__(self): Returns the dual number itself.
        __abs__(self): Returns the absolute value (magnitude) of the dual number.
        __float__(self): Returns the real component as a float.
        __int__(self): Returns the real component as an integer.
        __repr__(self): Returns the official string representation of the dual number.
        __str__(self): Returns a user-friendly string representation of the dual number.
        __index__(self): Returns the integer representation of the real component.
        __hash__(self): Returns the hash value of the dual number.
        __round__(self, ndigits): Rounds the dual number to a specified number of decimal places.
        __floor__(self): Returns the largest integer less than or equal to the real component.
        __ceil__(self): Returns the smallest integer greater than or equal to the real component.
        __trunc__(self): Returns the truncated integer value of the real component.
        __getitem__(self, index): Allows access to the real or dual component using index (0 for real, 1 for dual).
        __setitem__(self, index, value): Sets the value of the real or dual component using index (0 for real, 1 for dual).
        __delitem__(self, index): Deletes the real or dual component.
        __iter__(self): Returns an iterator over the real and dual components.
        __reversed__(self): Returns the real and dual components in reversed order.
        __array__(self, dtype=None): Converts the dual number to a NumPy array.
        __sizeof__(self): Returns the memory size of the dual number.
        __bool__(self): Returns whether the dual number is non-zero.
        __copy__(self): Creates a shallow copy of the dual number.
        __deepcopy__(self, memo): Creates a deep copy of the dual number.
        __dir__(self): Returns the list of attributes and methods available for the dual number.
        __to_dict__(self): Converts the dual number to a dictionary with 'real' and 'dual' keys.
        __to_tuple__(self): Converts the dual number to a tuple of (real, dual).
        __len__(self): Returns the length (number of components) of the dual number, which is 2.
        real(self): Returns the real component of the dual number.
        dual(self): Returns the dual component of the dual number.
        conjugate(self): Returns the conjugate of the dual number.
        is_zero(self): Checks if the dual number is zero.
        is_real(self): Checks if the dual number is purely real (dual component is zero).
        to_latex(self): Converts the dual number to a LaTeX string representation.
        log(self): Computes the natural logarithm of the dual number.
        log10(self): Computes the base-10 logarithm of the dual number.
        logbase(self, base): Computes the logarithm of the dual number to a given base.
        exp(self): Computes the exponential of the dual number.
        exp2(self): Computes the base-2 exponential of the dual number.
        sqrt(self): Computes the square root of the dual number.
        cbrt(self): Computes the cube root of the dual number.
        sin(self): Computes the sine of the dual number.
        cos(self): Computes the cosine of the dual number.
        tan(self): Computes the tangent of the dual number.
        sinh(self): Computes the hyperbolic sine of the dual number.
        cosh(self): Computes the hyperbolic cosine of the dual number.
        tanh(self): Computes the hyperbolic tangent of the dual number.
        asin(self): Computes the inverse sine (arcsine) of the dual number.
        acos(self): Computes the inverse cosine (arccosine) of the dual number.
        atan(self): Computes the inverse tangent (arctangent) of the dual number.
        asinh(self): Computes the inverse hyperbolic sine of the dual number.
        acosh(self): Computes the inverse hyperbolic cosine of the dual number.
        atanh(self): Computes the inverse hyperbolic tangent of the dual number.
    """
    
    
    ln10 = math.log(10)
    ln2 = math.log(2)
    
    def __init__(self, real, dual):
        self.real = real
        self.dual = dual
    
    def __add__(self, other):
        if not isinstance(other, Dual):
            other = Dual(other, 0)
        return Dual(self.real+other.real, self.dual+other.dual)
    
    def __radd__(self, other):
        if not isinstance(other, Dual):
            other = Dual(other, 0)
        return other+self
    
    def __iadd__(self, other):
        return self+other
    
    def __sub__(self, other):
        if not isinstance(other, Dual):
            other = Dual(other, 0)
        return Dual(self.real-other.real, self.dual-other.dual)
    
    def __rsub__(self, other):
        if not isinstance(other, Dual):
            other = Dual(other, 0)
        return other-self
    
    def __isub__(self, other):
        return self-other

    def __mul__(self, other):
        if not isinstance(other, Dual):
            other = Dual(other, 0)
        return Dual(self.real*other.real, self.real*other.dual + other.real*self.dual)
    
    def __rmul__(self, other):
        if not isinstance(other, Dual):
            other = Dual(other, 0)
        return other*self
    
    def __imul__(self, other):
        return self*other
    
    def __truediv__(self, other):
        if not isinstance(other, Dual):
            other = Dual(other, 0)
        if other.real == 0:
            raise ZeroDivisionError("Divisor must have non-zero real component.")
        return Dual(self.real / other.real, (self.dual - (self.real*other.dual/other.real))/other.real)
    
    def __rtruediv__(self, other):
        if not isinstance(other, Dual):
            other = Dual(other, 0)
        return other / self
    
    def __itruediv__(self, other):
        return self / other
    
    def __pow__(self, exponent):
        if self.real == 0:
            if not isinstance(exponent, Dual):
                if exponent < 0:
                    raise ValueError("Cannot raise 0 to a negative exponent")
            else:
                if exponent.real < 0:
                    raise ValueError("Cannot raise 0 to a negative exponent")
            return Dual(0, 0)
        if not isinstance(exponent, Dual):
            exponent = Dual(exponent, 0)
        raised = self.real**exponent.real
        return Dual(raised,
                    raised*(exponent.dual*math.log(self.real) + self.dual*exponent.real/self.real))
        
    
    def __rpow__(self, other):
        if not isinstance(other, Dual):
            other = Dual(other, 0)
        return other ** self
    
    def __ipow__(self, other):
        return self ** other
    
    def __eq__(self, other):
        # Equality ==
        if not isinstance(other, Dual):
            other = Dual(other, 0)
        return self.real == other.real and self.dual == other.dual
    
    def __ne__(self, other):
        if not isinstance(other, Dual):
            other = Dual(other, 0)
        return not(self.real == other.real and self.dual == other.dual)
    
    def __neg__(self):
        return Dual(-self.real, -self.dual)
    
    def __pos__(self):
        return self
    
    def __abs__(self):
        if self.real < 0:
            if self.dual < 0:
                return Dual(-self.real, -self.dual)
            return Dual(-self.real, self.dual)
        if self.dual < 0:
            return Dual(self.real, -self.dual)
        return Dual(self.real, self.dual)
    
    def __float__(self):
        return float(self.real)
    
    def __int__(self):
        return int(self.real)
    
    def __repr__(self):
        # Official string representation
        return f"Dual({self.real}, {self.dual})"
    
    def __str__(self):
        # User friendly string
        if self.dual < 0:
            return f"{self.real}-{-self.dual}ε"
        return f"{self.real}+{self.dual}ε"
    
    def __index__(self):
        return int(self.real)
    
    def __hash__(self):
        return hash((self.real, self.dual))
    
    def __round__(self, ndigits=None):
        return Dual(round(self.real, ndigits), round(self.dual, ndigits))
    
    def __floor__(self):
        return Dual(math.floor(self.real), math.floor(self.dual))
    
    def __ceil__(self):
        return Dual(math.ceil(self.real), math.ceil(self.dual))
    
    def __trunc__(self):
        return Dual(math.trunc(self.real), math.trunc(self.dual))
    
    def __getitem__(self, index):
        if index == 0:
            return self.real
        elif index == 1:
            return self.dual
        else:
            raise IndexError("Index out of range")
        
    
    def __setitem__(self, index, value):
        if index == 0:
            self.real = value
        elif index == 1:
            self.dual = value
        else:
            raise IndexError("Index out of range")
    
    def __delitem__(self, index):
        self[index] = 0
    
    def __iter__(self, index):
        yield self.real
        yield self.dual
    
    def __reversed__(self):
        yield self.dual
        yield self.real
    
    def __array__(self, dtype=None):
        return np.array([self.real, self.dual], dtype=dtype)
    
    def __sizeof__(self):
        total_size = sys.getsizeof(self)
        total_size += sys.getsizeof(self.real)
        total_size += sys.getsizeof(self.dual)
        return total_size
    
    def __bool__(self):
        return not (self.real == 0 and self.dual == 0)
    
    def __copy__(self):
        return Dual(self.real, self.dual)
    
    def __deepcopy__(self, memo):
        return Dual(self.real, self.dual)
    
    def __dir__(self):
        return ['real', 'dual']
    
    def __to_dict__(self):
        return {'real': self.real, 'dual': self.dual}
    
    def __to_tuple__(self):
        return (self.real, self.dual)
    
    def __len__(self):
        return 2
    
    def real(self):
        return self.real
    
    def dual(self):
        return self.dual
    
    def conjugate(self):
        return Dual(self.real, -self.dual)
    
    def is_zero(self):
        return self.real == 0 and self.dual == 0
    
    def is_real(self):
        return self.dual == 0
    
    def to_latex(self):
        if self.dual >= 0:
            return f"{self.real} + {self.dual} \\epsilon"
        else:
            return f"{self.real} - {-self.dual} \\epsilon"
    
    def log(self):
        if self.real <= 0:
            raise ValueError("Logarithm undefined for non-positive real values.")
        return Dual(math.log(self.real), self.dual / self.real)
    
    def log10(self):
        if self.real <= 0:
            raise ValueError("Logarithm undefined for non-positive real values.")
        return Dual(math.log10(self.real), self.dual / (self.real * self.ln10))
    
    def logbase(self, base):
        if self.real <= 0:
            raise ValueError("Logarithm undefined for non-positive real values.")
        if base <= 0 or base == 1:
            raise ValueError("Base must be greater than 0 and not equal to 1")
        
        lnbase = math.log(base)
        return Dual(math.log(self.real) / lnbase, self.dual / (self.real * lnbase))
    
    def exp(self):
        ereal = math.exp(self.real)
        return Dual(ereal, self.dual * ereal)

    def exp2(self):
        raisedreal = 2**self.real
        return Dual(raisedreal, self.dual * raisedreal * self.ln2)
    
    def sqrt(self):
        sqrtreal = self.real ** (1/2)
        return Dual(sqrtreal, self.dual / (2*sqrtreal))
    
    def cbrt(self):
        cbrtreal = self.real ** (1/3)
        return Dual(cbrtreal, self.dual / (3*cbrtreal**2))
    
    def sin(self):
        return Dual(math.sin(self.real), self.dual * math.cos(self.real))
    
    def cos(self):
        return Dual(math.cos(self.real), -self.dual * math.sin(self.real))
    
    def tan(self):
        return Dual(math.tan(self.real), self.dual / (math.cos(self.real)**2))
    
    def sinh(self):
        return Dual(math.sinh(self.real), self.dual * math.cosh(self.real))
    
    def cosh(self):
        return Dual(math.cosh(self.real), self.dual * math.sinh(self.real))
    
    def tanh(self):
        tanhreal = math.tanh(self.real)
        return Dual(tanhreal, self.dual * (1-tanhreal**2))
    
    def asin(self):
        return Dual(math.asin(self.real), self.dual / (1-self.real**2)**(1/2))
    
    def acos(self):
        return Dual(math.acos(self.real), -self.dual / (1-self.real**2)**(1/2))
    
    def atan(self):
        return Dual(math.atan(self.real), self.dual / (1+self.real**2))
    
    def asinh(self):
        return Dual(math.asinh(self.real), self.dual / (1 + self.real**2)**(1/2))
    
    def acosh(self):
        return Dual(math.acosh(self.real), self.dual / (self.real**2 - 1)**(1/2))
    
    def atanh(self):
        return Dual(math.atanh(self.real), self.dual / (1 - self.real**2))