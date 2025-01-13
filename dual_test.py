import unittest
from .dual.dual import Dual
import math
from math import isclose

class TestDual(unittest.TestCase):
    def test_add(self):
        # Dual + Dual
        num1 = Dual(5, 6)
        num2 = Dual(3, 4)
        self.assertEqual(Dual(8, 10), num1+num2, f"Failed Dual + Dual. Expected: {Dual(8, 10)} Actual: {num1+num2}")
        
        # Dual + int
        num1 = Dual(4, 3)
        num2 = 7
        self.assertEqual(Dual(11, 3), num1+num2, f"Failed Dual + int. Expected: {Dual(11, 3)} Actual: {num1+num2}")
        
        # Dual + float
        num1 = Dual(3, 6)
        num2 = 7.2
        self.assertEqual(Dual(10.2, 6), num1+num2, f"Failed Dual + float. Expected: {Dual(10.2, 6)} Actual: {num1+num2}")
        
        # Dual + 0
        num1 = Dual(4, 3)
        num2 = 0
        self.assertEqual(Dual(4, 3), num1+num2, f"Failed Dual + 0. Expected: {Dual(4, 3)} Actual: {num1+num2}")
        
    
    def test_radd(self):
        # int + Dual
        num1 = 3
        num2 = Dual(2, 5)
        self.assertEqual(Dual(5, 5), num1+num2, f"Failed int + Dual. Expected: {Dual(5, 5)} Actual: {num1+num2}")
        
        # float + Dual
        num1 = 4.2
        num2 = Dual(3, 6)
        self.assertEqual(Dual(7.2, 6), num1+num2, f"Failed float + Dual. Expected: {Dual(7.2, 6)} Actual: {num1+num2}")
        
        # 0 + Dual
        num1 = 0
        num2 = Dual(8, 2)
        self.assertEqual(Dual(8, 2), num1+num2, f"Failed 0 + Dual. Expected: {Dual(8, 2)} Actual: {num1+num2}")
    
    def test_iadd(self):
        # Dual += Dual
        num1 = Dual(2, 3)
        num2 = Dual(8, 2)
        num1 += num2
        self.assertEqual(Dual(10, 5), num1, f"Failed Dual += Dual. Expected: {Dual(10, 5)} Actual: {num1}")
        
        # Dual += int
        num1 = Dual(1, 2)
        num2 = 3
        num1 += num2
        self.assertEqual(Dual(4, 2), num1, f"Failed Dual += int. Expected: {Dual(4, 2)} Actual: {num1}")
        
        # Dual += float
        num1 = Dual(4, 5)
        num2 = 4.3
        num1 += num2
        self.assertEqual(Dual(8.3, 5), num1, f"Failed Dual += float. Expected: {Dual(8.3, 5)} Actual: {num1}")
    
    def test_sub(self):
        # Dual - Dual
        num1 = Dual(6, 5)
        num2 = Dual(2, 3)
        self.assertEqual(Dual(4, 2), num1-num2, f"Failed Dual - Dual. Expected: {Dual(4, 2)} Actual: {num1-num2}")
        
        # Dual - int
        num1 = Dual(4, 3)
        num2 = 3
        self.assertEqual(Dual(1, 3), num1-num2, f"Failed Dual - int. Expected: {Dual(1, 3)} Actual: {num1-num2}")
        
        # Dual - float
        num1 = Dual(10, 5)
        num2 = 5.5
        self.assertEqual(Dual(4.5, 5), num1-num2, f"Failed Dual - float. Expected: {Dual(4.5, 5)} Actual: {num1-num2}")
        
        # Dual - 0
        num1 = Dual(5, 4)
        num2 = 0
        self.assertEqual(Dual(5, 4), num1-num2, f"Failed Dual - 0. Expected: {Dual(5, 4)} Actual: {num1-num2}")
    
    def test_rsub(self):
        # int - Dual
        num1 = 6
        num2 = Dual(4, 3)
        self.assertEqual(Dual(2, -3), num1-num2, f"Failed int - Dual. Expected: {Dual(2, -3)} Actual: {num1-num2}")
        
        # float - Dual
        num1 = 5.7
        num2 = Dual(3, 2)
        self.assertEqual(Dual(2.7, -2), num1-num2, f"Failed float - Dual. Expected: {Dual(2.7, -2)} Actual: {num1-num2}")
        
        # 0 - Dual
        num1 = 0
        num2 = Dual(1, 2)
        self.assertEqual(Dual(-1, -2), num1-num2, f"Failed 0 - Dual. Expected: {Dual(-1, -2)} Actual: {num1-num2}")
    
    def test_isub(self):
        # Dual -= Dual
        num1 = Dual(8, 5)
        num2 = Dual(4, 2)
        num1 -= num2
        self.assertEqual(Dual(4, 3), num1, f"Failed Dual -= Dual. Expected: {Dual(4, 3)} Actual: {num1}")
        
        # Dual -= int
        num1 = Dual(7, 6)
        num2 = 5
        num1 -= num2
        self.assertEqual(Dual(2, 6), num1, f"Failed Dual -= int. Expected: {Dual(2, 6)} Actual: {num1}")
        
        # Dual -= float
        num1 = Dual(10, 9)
        num2 = 3.5
        num1 -= num2
        self.assertEqual(Dual(6.5, 9), num1, f"Failed Dual -= float. Expected: {Dual(6.5, 9)} Actual: {num1}")
    
    def test_mul(self):
        # Dual * Dual
        num1 = Dual(5, 4)
        num2 = Dual(2, 3)
        self.assertEqual(Dual(10, 23), num1*num2, f"Failed Dual * Dual. Expected: {Dual(10, 23)} Actual: {num1*num2}")
        
        # Dual * int
        num1 = Dual(3, 2)
        num2 = 4
        self.assertEqual(Dual(12, 8), num1*num2, f"Failed Dual * int. Expected: {Dual(12, 8)} Actual: {num1*num2}")
        
        # Dual * float
        num1 = Dual(2, 6)
        num2 = 1.5
        self.assertEqual(Dual(3, 9), num1*num2, f"Failed Dual * float. Expected: {Dual(3, 9)} Actual: {num1*num2}")
        
        # Dual * 0
        num1 = Dual(4, 5)
        num2 = 0
        self.assertEqual(Dual(0, 0), num1*num2, f"Failed Dual * 0. Expected: {Dual(0, 0)} Actual: {num1*num2}")
        
    
    def test_rmul(self):
        # int * Dual
        num1 = 4
        num2 = Dual(1, 2)
        self.assertEqual(Dual(4, 8), num1*num2, f"Failed int * Dual. Expected: {Dual(4, 8)} Actual: {num1*num2}")
        
        # float * Dual
        num1 = 2.5
        num2 = Dual(2, 4)
        self.assertEqual(Dual(5, 10), num1*num2, f"Failed float * Dual. Expected: {Dual(5, 10)} Actual: {num1*num2}")
        
        # 0 * Dual
        num1 = 0
        num2 = Dual(3, 4)
        self.assertEqual(Dual(0, 0), num1*num2, f"Failed 0 * Dual. Expected: {Dual(0, 0)} Actual: {num1*num2}")
    
    def test_imul(self):
        # Dual *= Dual
        num1 = Dual(1, 2)
        num2 = Dual(3, 4)
        num1 *= num2
        self.assertEqual(Dual(3, 10), num1, f"Failed Dual *= Dual. Expected: {Dual(3, 10)} Actual: {num1}")
        
        # Dual *= int
        num1 = Dual(2, 5)
        num2 = 3
        num1 *= num2
        self.assertEqual(Dual(6, 15), num1, f"Failed Dual *= int. Expected: {Dual(6, 15)} Actual: {num1}")
        
        # Dual *= float
        num1 = Dual(1, 5)
        num2 = 1.2
        num1 *= num2
        self.assertEqual(Dual(1.2, 6), num1, f"Failed Dual *= float. Expected: {Dual(1.2, 6)} Actual: {num1}")
        
        # Dual *= 0
        num1 = Dual(2, 4)
        num2 = 0
        num1 *= num2
        self.assertEqual(Dual(0, 0), num1, f"Failed Dual *= 0. Expected: {Dual(0, 0)} Actual: {num1}")
    
    def test_truediv(self):
        # Dual / Dual
        num1 = Dual(5, 6)
        num2 = Dual(4, 2)
        self.assertEqual(Dual(5/4, 7/8), num1/num2, f"Failed Dual / Dual. Expected: {Dual(5/4, 7/8)} Actual: {num1/num2}")
        
        # Dual / int
        num1 = Dual(4, 8)
        num2 = 2
        self.assertEqual(Dual(2, 4), num1/num2, f"Failed Dual / int. Expected: {Dual(2, 4)} Actual: {num1 / num2}")
        
        # Dual / float
        num1 = Dual(3, 6)
        num2 = 1.5
        self.assertEqual(Dual(2, 4), num1/num2, f"Failed Dual / float. Expected: {Dual(2, 4)} Actual: {num1 / num2}")

        # Dual / 0
        num1 = Dual(1, 2)
        num2 = 0
        with self.assertRaises(ZeroDivisionError, msg="Failed Dual / 0. No ZeroDivisionError thrown."):
            _ = num1 / num2

    def test_rtruediv(self):
        # int / Dual
        num1 = 10
        num2 = Dual(3, 4)
        self.assertEqual(Dual(10/3, -40/9), num1/num2, f"Failed int / Dual. Expected: {Dual(10/3, -40/9)} Actual: {num1 / num2}")
        
        # float / Dual
        num1 = 15.25
        num2 = Dual(6, 3)
        self.assertEqual(Dual(15.25/6, -45.75/36), num1/num2, f"Failed float / Dual. Expected: {Dual(15.25/6, -45.75/36)} Actual: {num1 / num2}")
        
        # 0 / Dual
        num1 = 0
        num2 = Dual(3, 8)
        self.assertEqual(Dual(0, 0), num1/num2, f"Failed 0 / Dual. Expected: {Dual(0, 0)} Actual: {num1 / num2}")
        
    
    def test_itruediv(self):
        # Dual /= Dual
        num1 = Dual(8, 3)
        num2 = Dual(4, 5)
        num1 /= num2
        self.assertEqual(Dual(2, -7/4), num1, f"Failed Dual /= Dual. Expected: {Dual(2, -7/4)} Actual: {num1}")
        
        # Dual /= int
        num1 = Dual(10, 6)
        num2 = 2
        num1 /= num2
        self.assertEqual(Dual(5, 3), num1, f"Failed Dual /= int. Expected: {Dual(10, 6)} Actual: {num1}")
        
        # Dual /= float
        num1 = Dual(10, 15)
        num2 = 2.5
        num1 /= num2
        self.assertEqual(Dual(4, 6), num1, f"Failed Dual /= float. Expected: {Dual(4, 6)} Actual: {num1}")
        
        # Dual /= 0
        num1 = Dual(5, 6)
        num2 = 0
        try:
            num1 /= num2
            self.assertEqual(0, 1, "Failed Dual /= 0. ZeroDivisionError not thrown.")
        except ZeroDivisionError as e:
            pass
        except Exception as e:
            self.assertEqual(0, 1, "Wrong exception at Dual /= 0")
    
    def test_power(self):
        dual1 = Dual(2, 3)
        result = dual1 ** 2
        self.assertTrue(isinstance(result, Dual))
        self.assertTrue(isclose(result.real, 4))
        self.assertTrue(isclose(result.dual, 12))
    
    def test_log(self):
        dual1 = Dual(2, 3)
        result = dual1.log()
        self.assertTrue(isinstance(result, Dual))
        self.assertTrue(isclose(result.real, math.log(2)))
        self.assertTrue(isclose(result.dual, 3 / 2))
        
        # Test log of a non-positive number
        dual2 = Dual(-1, 2)
        with self.assertRaises(ValueError):
            dual2.log()
    
    def test_exp(self):
        dual1 = Dual(1, 1)
        result = dual1.exp()
        self.assertTrue(isinstance(result, Dual))
        self.assertTrue(isclose(result.real, math.exp(1)))
        self.assertTrue(isclose(result.dual, math.exp(1)))
    
    def test_sin(self):
        dual1 = Dual(math.pi / 2, 1)
        result = dual1.sin()
        print(f"Result real: {result.real} Result dual: {result.dual}")
        self.assertTrue(isinstance(result, Dual))
        self.assertTrue(isclose(result.real, 1))
        self.assertTrue(isclose(result.dual, 0, abs_tol=1e-16))
    
    def test_asin(self):
        dual1 = Dual(0.5, 1)
        result = dual1.asin()
        self.assertTrue(isinstance(result, Dual))
        self.assertTrue(isclose(result.real, math.asin(0.5)))
        self.assertTrue(isclose(result.dual, 1 / math.sqrt(1 - 0.5**2)))
    
    def test_repr(self):
        dual1 = Dual(3, 4)
        self.assertEqual(repr(dual1), "Dual(3, 4)")
    
    def test_str(self):
        dual1 = Dual(3, 4)
        self.assertEqual(str(dual1), "3+4ε")
        
    def test_copy(self):
        dual1 = Dual(3, 4)
        dual2 = dual1.__copy__()
        self.assertEqual(dual1, dual2)
        
    def test_len(self):
        dual1 = Dual(3, 4)
        self.assertEqual(len(dual1), 2)

    def test_real_and_dual_accessors(self):
        dual1 = Dual(3, 4)
        self.assertEqual(dual1[0], 3)
        self.assertEqual(dual1[1], 4)

        dual1[0] = 5
        dual1[1] = 6
        self.assertEqual(dual1[0], 5)
        self.assertEqual(dual1[1], 6)
    
    def test_is_zero(self):
        dual1 = Dual(0, 0)
        self.assertTrue(dual1.is_zero())
        
        dual2 = Dual(1, 0)
        self.assertFalse(dual2.is_zero())
        
    def test_is_real(self):
        dual1 = Dual(3, 0)
        self.assertTrue(dual1.is_real())
        
        dual2 = Dual(3, 4)
        self.assertFalse(dual2.is_real())