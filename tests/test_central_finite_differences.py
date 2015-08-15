import unittest
import os,sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__))))
import finitdiff

class Suite(unittest.TestCase):
    def test_derivative_of_x_squared(self):
        diff = finitdiff.first_order_central(self, lambda x: x, x=1.0, h=0.1)
        self.assertAlmostEqual(diff,1)

if __name__ == '__main__':
    unittest.main()
