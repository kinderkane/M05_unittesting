import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
    
    ###I am not entirely familiar with these tests even after the use of the tutorial, from what I am seeing, it is hard to distinguish the 
    ###use of these tests instead of waiting for errors when running the code, the only thing that makes sense to me is 
    ###when considering a certain prompt for example in your python program, perhaps there is an error waiting to happen
    ###or an unexpected input that your code could not handle, or foreseeable issues that won't be a problem yet.