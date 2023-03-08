import unittest
from unittest.mock import patch, Mock
from utils import get_current_rate, compare_rates

class TestUtils(unittest.TestCase):
    @patch('utils.requests.get')
    def test_get_current_rate(self, mock_get):
        # Mock the API response
        mock_data = {'USDBRL': {'bid': '5.00'}}
        mock_response = Mock()
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        # Call the function and check the result
        rate = get_current_rate()
        self.assertEqual(rate, 5.0)

    def test_compare_rates(self):
        # Test case 1: current rate is higher than previous rate
        previous_rate = 4.0
        current_rate = 5.0
        result = compare_rates(previous_rate, current_rate)
        self.assertEqual(result, current_rate)

        # Test case 2: current rate is lower than previous rate
        previous_rate = 5.0
        current_rate = 4.0
        result = compare_rates(previous_rate, current_rate)
        self.assertEqual(result, current_rate)

        # Test case 3: current rate is equal to previous rate
        previous_rate = 5.0
        current_rate = 5.0
        result = compare_rates(previous_rate, current_rate)
        self.assertEqual(result, previous_rate)

if __name__ == '__main__':
    unittest.main()
