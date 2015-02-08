import unittest

from titan import Titan

class TitanTests(unittest.TestCase):
    
    def setUp(self):
        self.titan = Titan()
    
    def test_atomic_int(self):
        for _ in range(100):
            retint = int(self.titan.interpret({"type":"int", "min":1, "max":1000}))
            self.assertTrue(1 <= retint <= 1000)

if __name__ == "__main__":
    unittest.main()
