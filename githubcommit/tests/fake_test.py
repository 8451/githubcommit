import unittest
from unittest import TestCase

class ThisIsAFakeTest(TestCase):
    def test_this_will_always_pass(self):
        self.assertTrue(True)
        
if __name__ == '__main__':
    unittest.main()