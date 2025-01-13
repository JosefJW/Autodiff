# Dual - Autodifferentiation Library

Autodiff is a custom Python library that implements automatic differentiation (autodiff) using dual numbers. It allows for the efficient computation of derivatives for functions, making it useful for optimization, machine learning, and other applications that require gradient computation.
## Features

    Compute both values and derivatives of functions using dual numbers.
    Supports basic mathematical operations (+, -, *, /, **).
    Chain operations together to compute derivatives of complex expressions.
    Easily integrable with other Python projects for machine learning or optimization.

## Requirements

    Python 3.x
    NumPy

## Installation

You can install Dual by cloning the repository or including it as a dependency in your project.
### Method 1: Clone the repository

git clone https://github.com/josefjw/autodiff.git
cd autodiff

Then, you can import it into your project like this:

from .dual.dual import Dual

### Method 2: Install via requirements.txt

You can add the following to your requirements.txt:

git+https://github.com/josefjw/autodiff.git

Then, install dependencies:

pip install -r requirements.txt

## Usage

You can create a Dual number by instantiating the Dual class, where the first argument is the value and the second argument is the derivative (typically set to 1 for the independent variable).
### Example 1: Simple function
```
from .dual.dual import Dual

x = Dual(2.0, 1.0)  # Create a dual number with value 2.0 and derivative 1.0
f = Dual.exp(x**2) * Dual.sin(x)

print("f(x) =", f.real)  # Output the value of the function
print("f'(x) =", f.dual)  # Output the derivative of the function
```
### Example 2: Complex function
```
from dual.dual import Dual

x = Dual(3.0, 1.0)
f = Dual.exp(x**2) * Dual.cos(x) + Dual.log(Dual.cosh(x))

print("f(x) =", f.real)
print("f'(x) =", f.dual)
```
## Supported Operations

    +, -, *, /, ** (basic arithmetic)
    
    Trigonometric functions: sin(), cos(), tan(), sinh(), cosh(), tanh(), 
    asin(), acos(), atan(), asinh(), acosh(), atanh()
    
    Exponential and logarithmic functions: exp(), exp2(), log(), log10(), logbase()
    
    Other: sqrt(), cbrt()

## Examples

For more complex examples, refer to the examples/ directory in the repository.

## Contributing

    Fork the repository.
    Clone your fork to your local machine.
    Create a new branch (git checkout -b feature-branch).
    Make changes and commit them (git commit -am 'Add new feature').
    Push your branch (git push origin feature-branch).
    Submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
