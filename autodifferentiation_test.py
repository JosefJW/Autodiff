from .dual.dual import Dual
import unittest
import math

class TestAutodiff(unittest.TestCase):

    def test_sin(self):
        x = Dual(2, 1)  # Create a dual number with x = 2 and dual = 1 for the derivative
        result = math.sin(x.real)  # Actual value
        derivative = math.cos(x.real)  # Actual derivative

        self.assertAlmostEqual(x.sin().real, result, places=5)  # Test function value
        self.assertAlmostEqual(x.sin().dual, derivative, places=5)  # Test derivative

    def test_cos(self):
        x = Dual(2, 1)  # x = 2, derivative = 1
        result = math.cos(x.real)
        derivative = -math.sin(x.real)

        self.assertAlmostEqual(x.cos().real, result, places=5)
        self.assertAlmostEqual(x.cos().dual, derivative, places=5)

    def test_exp(self):
        x = Dual(2, 1)
        result = math.exp(x.real)
        derivative = math.exp(x.real)

        self.assertAlmostEqual(x.exp().real, result, places=5)
        self.assertAlmostEqual(x.exp().dual, derivative, places=5)

    def test_sin_exp(self):
        x = Dual(2, 1)
        result = math.sin(math.exp(x.real))
        # Chain rule: derivative of sin(exp(x)) is cos(exp(x)) * exp(x)
        derivative = math.cos(math.exp(x.real)) * math.exp(x.real)

        self.assertAlmostEqual(x.exp().sin().real, result, places=5)
        self.assertAlmostEqual(x.exp().sin().dual, derivative, places=5)

    def test_custom_function(self):
        # Example: f(x) = e^(x^2) * cos(x)
        x = Dual(2, 1)  # Dual number where real part is 2 and dual part is 1
        
        # Compute the expected value manually for f(x) = e^(x^2) * cos(x)
        result = math.exp(x.real ** 2) * math.cos(x.real)
        
        # Derivative calculation:
        # Using the product rule: d/dx [f(x) * g(x)] = f'(x) * g(x) + f(x) * g'(x)
        derivative = (2 * x.real * math.exp(x.real ** 2) * math.cos(x.real)) - (math.exp(x.real ** 2) * math.sin(x.real))

        # Compute using the Dual class (chaining operations properly)
        computed_result = (Dual.exp(x**2)*Dual.cos(x)).real  # f(x) = e^(x^2) * cos(x)
        computed_derivative = (Dual.exp(x**2)*Dual.cos(x)).dual 
        
        self.assertAlmostEqual(computed_result.real, result, places=5)
        self.assertAlmostEqual(computed_derivative, derivative, places=5)

if __name__ == '__main__':
    unittest.main()