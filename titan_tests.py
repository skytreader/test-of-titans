import string
import unittest

from titan import Titan

class TitanTests(unittest.TestCase):
    
    def setUp(self):
        self.titan = Titan()
    
    def test_atomic_int(self):
        for _ in range(100):
            retint = int(self.titan.interpret({"type":"int", "min":1, "max":1000}))
            self.assertTrue(1 <= retint <= 1000)

    def test_atomic_float(self):
        for _ in range(100):
            retfloat = float(self.titan.interpret({"type":"float", "min":0.01,
              "max":3.14159265358}))
            self.assertTrue(0.01 <= retfloat <= 3.14159265358)

    def test_atomic_string(self):
        for _ in range(100):
            retstr = self.titan.interpret({"type":"str", "charset":string.hexdigits,
              "min-len":4, "max-len":8})
            self.assertTrue(4 <= len(retstr) <= 8)

            for c in retstr:
                self.assertTrue(c in string.hexdigits)

if __name__ == "__main__":
    unittest.main()
