import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dual import Dual
import math

def nested_trig(x=math.pi):
    dx = Dual(x, 1)
    f = Dual.sin(Dual.cos(dx**2))
    
    print(f"f(x) = sin(cos(x^2))")
    print(f"f({x}) = {f.real}")
    print(f"f'({x}) = {f.dual}")
    print()

def trig_power(x=5):
    dx = Dual(x, 1)
    f = (Dual.sin(dx**2 + 1))**3.5
    
    print(f"f(x) = (sin(x^2 + 1))^3.5")
    print(f"f({x}) = {f.real}")
    print(f"f'({x}) = {f.dual}")
    print()

def lots_of_trig(x=math.pi/2):
    dx = Dual(x, 1)
    f = Dual.sinh(abs(Dual.tanh(Dual.cosh(Dual.atan(dx**2)))))*Dual.asin(dx/2)
    
    print(f"f({x}) = sinh(|tanh(cosh(atan(x^2)))|) * asin(x/2)")
    print(f"f({x}) = {f.real}")
    print(f"f'({x}) = {f.dual}")
    print()

def powers_of_trig(x=0.5):
    dx = Dual(x, 1)
    f = Dual.atanh(dx)**Dual.sin(dx)**Dual.cos(dx)**Dual.tan(dx)**Dual.atanh(dx)
    
    print(f"f({x}) = atanh(x) ^ (sin(x) ^ (cos(x) ^ (tan(x) ^ atanh(x))))")
    print(f"f({x}) = {f.real}")
    print(f"f'({x}) = {f.dual}")

nested_trig()
trig_power()
lots_of_trig()
powers_of_trig()