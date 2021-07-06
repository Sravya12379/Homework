import unittest
from hw9 src.py import check

class test(unittest.TestCase):
    def test_check(self):
        expected= "true"
        result=check(32)
        self.assertEqual(expected,result )

if __name__=='__main__' :
    unittest.main()

