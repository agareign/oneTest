import unittest

# Define the function to be tested
def interest_calculator(p, r, n):
    """ Simple interest calculation assuming daily interest accumulation """
    return round(p * r * n / 36500, 2)  # Assuming interest is simple and rounded to 2 decimals

# TestInterestCalculator inherits attributes and methods from the class
# TestCase in the testing framework unittest
class TestInterestCalculator (unittest.TestCase):

    # Define a set of unit tests where each test tests one thing only
    # Tests should start with test_ and the name should explain
    # what is being tested

    def test_zeroprincipal(self):
        """ Test case where principal amount is zero """
        # Arrange - set up test parameters
        p = 0
        r = 3
        n = 31
        result_should_be = 0

        # Action - Call the method to be tested
        interest = interest_calculator(p, r, n)

        # Assert - test what should be true
        self.assertEqual(result_should_be, interest)

    def test_yearly_interest(self):
        """ Test case where principal is 17000 with 3% interest over a year """
        # Arrange - set up test parameters
        p = 17000
        r = 3
        n = 365
        
        # Action - Call the method to be tested
        result_should_be = 270.36
        interest = interest_calculator(p, r, n)

        # Assert - test what should be true
        self.assertEqual(result_should_be, interest)
        
# Run the tests
if __name__ == '__main__':
    unittest.main()
