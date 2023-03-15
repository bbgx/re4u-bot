import unittest
from unittest.mock import patch, MagicMock
from src.utils import get_current_rate, compare_rates

class TestGetCurrentRate(unittest.TestCase):
    @patch("requests.get")
    def test_get_current_rate_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"USDBRL": {"bid": "5.1234"}}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        rate = get_current_rate()
        self.assertEqual(rate, 5.1234)

class TestCompareRates(unittest.TestCase):
    @patch("src.utils.post_to_relay")
    def test_compare_rates(self, mock_post_to_relay):
        messages = [
            (None, 5, "O dólar abriu o mercado custando R$ 5.00."),
            (4, 5, "O dólar subiu! O dólar está R$ 5.00."),
            (5, 4, "O dólar caiu! O dólar está R$ 4.00."),
            (5, 5, "O dólar continua R$ 5.00. Não acho que quem ganhar ou quem perder, nem quem ganhar nem perder, vai ganhar ou perder. Vai todo mundo perder."),
        ]
        for prev, current, expected_message in messages:
            compare_rates(prev, current)
            mock_post_to_relay.assert_called_with(expected_message)
            mock_post_to_relay.reset_mock()

if __name__ == "__main__":
    unittest.main()
