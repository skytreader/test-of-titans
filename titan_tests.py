import random
import string
import unittest

from titan import Titan

class TitanTests(unittest.TestCase):
    
    def setUp(self):
        self.titan = Titan()

        self.int_min = 1
        self.int_max = 1000
        self.float_min = 0.01
        self.float_max = 3.14159265358
        self.str_minlen = 4
        self.str_maxlen = 8
        self.list_minlen = 10
        self.list_maxlen = 100

        self.test_precision = 100
    
    def test_atomic_int(self):
        for _ in range(self.test_precision):
            retint = int(self.titan.interpret({"type":"int", "min":self.int_min,
              "max":self.int_max}))
            self.assertTrue(self.int_min <= retint <= self.int_max)

    def test_atomic_float(self):
        for _ in range(self.test_precision):
            retfloat = float(self.titan.interpret({"type":"float", "min":self.float_min,
              "max":self.float_max}))
            self.assertTrue(self.float_min <= retfloat <= self.float_max)

    def test_atomic_string(self):
        for _ in range(self.test_precision):
            retstr = self.titan.interpret({"type":"str", "charset":string.hexdigits,
              "min-len":self.str_minlen, "max-len":self.str_maxlen})
            self.assertTrue(self.str_minlen <= len(retstr) <= self.str_maxlen)

            for c in retstr:
                self.assertTrue(c in string.hexdigits)

    def test_list_int(self):
        for _ in range(self.test_precision):
            expected_len = random.randint(self.list_minlen, self.list_maxlen)
            raw = self.titan.interpret({"type":"int-list", "min":self.int_min,
              "max":self.int_max, "count":expected_len})
            intlist = list(map(int, raw.split()))
            self.assertEqual(expected_len, len(intlist))

            for item in intlist:
                self.assertTrue(self.int_min <= item <= self.int_max)

    def test_sorted_list_int(self):
        half_run = int(self.test_precision / 2)
        for _ in range(half_run):
            expected_len = random.randint(self.list_minlen, self.list_maxlen)
            raw = self.titan.interpret({"type":"int-list", "min":self.int_min,
              "max":self.int_max, "count":expected_len, "sort-by":"desc"})
            intlist = list(map(int, raw.split()))
            self.assertEqual(expected_len, len(intlist))
            sorted_intlist = sorted(intlist, reverse=True)
            self.assertEqual(intlist, sorted_intlist)

        for _ in range(half_run):
            expected_len = random.randint(self.list_minlen, self.list_maxlen)
            raw = self.titan.interpret({"type":"int-list", "min":self.int_min,
              "max":self.int_max, "count":expected_len, "sort-by":"asc"})
            intlist = list(map(int, raw.split()))
            self.assertEqual(expected_len, len(intlist))
            sorted_intlist = sorted(intlist)
            self.assertEqual(intlist, sorted_intlist)

    def test_list_float(self):
        for _ in range(self.test_precision):
            expected_len = random.randint(self.list_minlen, self.list_maxlen)
            raw = self.titan.interpret({"type":"float-list", "min":self.float_min,
              "max":self.float_max, "count":expected_len})
            floatlist = list(map(float, raw.split()))
            self.assertEqual(expected_len, len(floatlist))

            for item in floatlist:
                self.assertTrue(self.float_min <= item <= self.float_max)

    def test_sorted_list_float(self):
        half_run = int(self.test_precision / 2)
        for _ in range(half_run):
            expected_len = random.randint(self.list_minlen, self.list_maxlen)
            raw = self.titan.interpret({"type":"float-list", "min":self.float_min,
              "max":self.float_max, "count":expected_len, "sort-by":"desc"})
            floatlist = list(map(float, raw.split()))
            self.assertEqual(expected_len, len(floatlist))
            sorted_floatlist = sorted(floatlist, reverse=True)
            self.assertEqual(floatlist, sorted_floatlist)

        for _ in range(half_run):
            expected_len = random.randint(self.list_minlen, self.list_maxlen)
            raw = self.titan.interpret({"type":"float-list", "min":self.float_min,
              "max":self.float_max, "count":expected_len, "sort-by":"asc"})
            floatlist = list(map(float, raw.split()))
            self.assertEqual(expected_len, len(floatlist))
            sorted_floatlist = sorted(floatlist)
            self.assertEqual(floatlist, sorted_floatlist)

    def test_list_str(self):
        possible_charsets = (string.hexdigits, string.punctuation,
          string.ascii_letters, None)
        for _ in range(self.test_precision):
            expected_len = random.randint(self.list_minlen, self.list_maxlen)
            charset = random.choice(possible_charsets)
            strlist = self.titan.interpret({"type":"str-list", "min-len":self.str_minlen,
              "max-len":self.str_maxlen, "count":expected_len, "charset":charset}).split()
            self.assertEqual(expected_len, len(strlist))

            for item in strlist:
                self.assertTrue(self.str_minlen <= len(item) <= self.str_maxlen)
                
                for c in item:
                    if charset:
                        self.assertTrue(c in charset)
                    else:
                        self.assertTrue(c in "".join((string.ascii_lowercase, string.digits)))

    def test_sorted_list_str(self):
        half_run = int(self.test_precision / 2)
        possible_charsets = (string.hexdigits, string.punctuation,
          string.ascii_letters, None)

        for _ in range(half_run):
            expected_len = random.randint(self.list_minlen, self.list_maxlen)
            charset = random.choice(possible_charsets)
            strlist = self.titan.interpret({"type":"str-list", "min-len":self.str_minlen,
              "max-len":self.str_maxlen, "count":expected_len, "charset":charset,
              "sort-by":"desc"}).split()
            self.assertEqual(expected_len, len(strlist))
            sorted_strlist = sorted(strlist, reverse=True)
            self.assertEqual(sorted_strlist, strlist)

        for _ in range(half_run):
            expected_len = random.randint(self.list_minlen, self.list_maxlen)
            charset = random.choice(possible_charsets)
            strlist = self.titan.interpret({"type":"str-list", "min-len":self.str_minlen,
              "max-len":self.str_maxlen, "count":expected_len, "charset":charset,
              "sort-by":"asc"}).split()
            self.assertEqual(expected_len, len(strlist))
            sorted_strlist = sorted(strlist)
            self.assertEqual(sorted_strlist, strlist)

    def test_list_isnot_int(self):
        is_not_list = self.titan.interpret({
            "type": "int-list", "min": 4, "max": 8, "count": 2,
            "varlabel": "queen"
        })

        for _ in range(self.test_precision):
            intlist = self.titan.interpret({
                "type": "int-list", "min": 4, "max": 8, "count": 2,
                "is-not": "queen"
            })
            self.assertNotEqual(is_not_list, intlist)

    def test_list_notin_int(self):
        not_in_list = self.titan.interpret({
            "type": "int-list", "min": self.int_min, "max": self.int_max,
            "count": self.list_maxlen, "varlabel": "spamkcd"
        }).split()
        not_in_list = [int(x) for x in not_in_list]

        for _ in range(self.test_precision):
            intlist = self.titan.interpret({
                "type": "int-list", "min": self.int_min, "max": self.int_max,
                "count": self.list_maxlen, "not-in": "spamkcd"
            })

            for i in intlist:
                self.assertTrue(i not in not_in_list)

    def test_list_isnot_str(self):
        is_not_str = self.titan.interpret({
            "type": "str-list", "max-len": 2, "charset": "abc", "varlabel": "abc",
            "count": 2
        })

        for _ in range(self.test_precision):
            strlist = self.titan.interpret({
                "type": "str-list", "max-len": 2, "charset": "abc", "is-not": "abc",
                "count": 2
            })
            self.assertNotEqual(is_not_str, strlist)

    def test_list_notin_str(self):
        not_in_list = self.titan.interpret({
            "type": "str-list", "max-len": 2, "charset": "abc", "varlabel": "abc",
            "count": int(self.list_maxlen / 4)
        }).split()

        for _ in range(self.test_precision):
            strlist = self.titan.interpret({
                "type": "str-list", "max-len": 2, "charset": "abc", "not-in": "abc",
                "count": self.list_maxlen
            }).split()

            for s in strlist:
                self.assertTrue(s not in not_in_list)

    def test_reftype_int(self):
        for label_id in range(self.test_precision):
            label = "varlabel" + str(label_id)
            intlist = self.titan.interpret({"type":"int-list", "min":self.int_min,
              "max":self.int_max, "count":self.list_maxlen, "varlabel":label})
            intlist = list(map(int, intlist.split()))

            for _ in range(self.test_precision):
                refint = int(self.titan.interpret({"type":"ref", "varlabel":label}))
                self.assertTrue(refint in intlist)

    def test_reftype_float(self):
        for label_id in range(self.test_precision):
            label = "varlabel" + str(label_id)
            floatlist = self.titan.interpret({"type":"float-list", "min":self.float_min,
              "max":self.float_max, "count":self.list_maxlen, "varlabel":label})
            floatlist = list(map(float, floatlist.split()))

            for _ in range(self.test_precision):
                reffloat = float(self.titan.interpret({"type":"ref", "varlabel":label}))
                self.assertTrue(reffloat in floatlist)

    def test_reftype_str(self):
        for label_id in range(self.test_precision):
            label = "varlabel" + str(label_id)
            strlist = self.titan.interpret({"type":"str-list", "min-len":self.str_minlen,
              "max-len":self.str_maxlen, "count":self.list_maxlen, "varlabel":label})
            floatlist = strlist.split()

            for _ in range(self.test_precision):
                refstr = self.titan.interpret({"type":"ref", "varlabel":label})
                self.assertTrue(refstr in strlist)
