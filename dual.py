from numbers import Number
import math
import numpy as np
import sys

class Dual(Number):
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
        return math.sqrt(self.real**2 + self.dual**2)
    
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