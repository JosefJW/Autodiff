from dual import Dual

def product_of_polynomials(x=3.5):
    dx = Dual(x, 1)
    f = (dx**2 + 3*dx)*(dx**3 - 2*dx)
    
    print(f"f(x) = (x^2 + 3x) * (x^3 - 2x)")
    print(f"f({x}) = {f.real}")
    print(f"f'({x}) = {f.dual}")
    print()

def quotient_of_polynomials(x=2):
    dx = Dual(x, 1)
    f = (dx**3 + 5*dx) / (dx**2 + 1)
    
    print(f"f(x) = (x^3 + 5x) / (x^2 + 1)")
    print(f"f({x}) = {f.real}")
    print(f"f'({x}) = {f.dual}")
    print()

def polynomial_to_a_power(x=1.5):
    dx = Dual(x, 1)
    f = (dx**2 + 2*dx)**6
    
    print(f"f(x) = (x^2 + 2x)^6")
    print(f"f({x}) = {f.real}")
    print(f"f({x}) = {f.dual}")
    print()

def nested_polynomial_powers(x=4):
    dx = Dual(x, 1)
    f = ((((dx+2)**2)/3)**(-1/8))*dx**2
    
    print(f"f(x) = ((((x+2)^2)/3)^(-1/8))*x^2")
    print(f"f({x}) = {f.real}")
    print(f"f({x}) = {f.dual}")
    print()

product_of_polynomials()
quotient_of_polynomials()
polynomial_to_a_power()
nested_polynomial_powers()