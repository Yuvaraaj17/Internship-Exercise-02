import unittest
import fib

class FibTest(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib.fib(5),[0,1,1,2,3])
        self.assertEqual(fib.fib(7),[0,1,1,2,3,5,8])
        self.assertEqual(fib.fib(2),[0,1,1])
        self.assertEqual(fib.fib(0),[0])
        
        with self.assertRaises(ValueError):
            fib.fib(-2)

if __name__=="__main__":
    unittest.main()