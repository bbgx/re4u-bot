import unittest
from unittest.mock import patch
from main import is_weekday, is_business_hours, is_hour_beginning, get_and_compare_rate
from datetime import datetime

class TestHelperFunctions(unittest.TestCase):
    def test_is_weekday(self):
        weekday = datetime(2023, 3, 13)
        weekend = datetime(2023, 3, 12)
        self.assertTrue(is_weekday(weekday))
        self.assertFalse(is_weekday(weekend))

    def test_is_business_hours(self):
        during_business_hours = datetime(2023, 3, 13, 15, 0)
        outside_business_hours = datetime(2023, 3, 13, 8, 0)
        self.assertTrue(is_business_hours(during_business_hours))
        self.assertFalse(is_business_hours(outside_business_hours))

    def test_is_hour_beginning(self):
        at_hour_beginning = datetime(2023, 3, 13, 9, 0)
        not_at_hour_beginning = datetime(2023, 3, 13, 9, 1)
        self.assertTrue(is_hour_beginning(at_hour_beginning))
        self.assertFalse(is_hour_beginning(not_at_hour_beginning))

class TestGetAndCompareRate(unittest.TestCase):
    @patch("main.get_current_rate")
    @patch("main.compare_rates")
    def test_get_and_compare_rate(self, mock_compare_rates, mock_get_current_rate):
        mock_get_current_rate.return_value = 5.0
        current_time = datetime(2023, 3, 13, 15, 0)

        with patch("main.datetime") as mock_datetime:
            mock_datetime.now.return_value = current_time
            mock_datetime.side_effect = lambda *args, **kwargs: datetime(*args, **kwargs)

            get_and_compare_rate()

        mock_get_current_rate.assert_called_once()
        mock_compare_rates.assert_called_once()

if __name__ == "__main__":
    unittest.main()
