import random
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

    def test_list_int(self):
        for _ in range(100):
            expected_len = random.randint(10, 100)
            raw = self.titan.interpret({"type":"int-list", "min":1, "max":1000,
              "count":expected_len})
            intlist = list(map(int, raw.split()))
            self.assertEqual(expected_len, len(intlist))

            for item in intlist:
                self.assertTrue(1 <= item <= 1000)

    def test_list_float(self):
        for _ in range(100):
            expected_len = random.randint(10, 100)
            raw = self.titan.interpret({"type":"float-list", "min":0.01,
              "max":3.14159265358, "count":expected_len})
            floatlist = list(map(float, raw.split()))
            self.assertEqual(expected_len, len(floatlist))

            for item in floatlist:
                self.assertTrue(0.01 <= item <= 3.14159265358)

    def test_list_str(self):
        possible_charsets = (string.hexdigits, string.punctuation,
          string.ascii_letters, None)
        for _ in range(100):
            expected_len = random.randint(10, 100)
            charset = random.choice(possible_charsets)
            strlist = self.titan.interpret({"type":"str-list", "min-len":4,
              "max-len":8, "count":expected_len, "charset":charset}).split()
            self.assertEqual(expected_len, len(strlist))

            for item in strlist:
                self.assertTrue(4 <= len(item) <= 8)
                
                for c in item:
                    if charset:
                        self.assertTrue(c in charset)
                    else:
                        self.assertTrue(c in "".join((string.ascii_lowercase, string.digits)))

if __name__ == "__main__":
    unittest.main()
