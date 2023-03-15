import unittest
import ssl
from unittest.mock import MagicMock, patch
from src.post_to_relay import post_to_relay, relay_manager_connection, create_and_sign_event

class TestPostToRelay(unittest.TestCase):
    @patch("src.post_to_relay.relay_manager_connection")
    @patch("src.post_to_relay.create_and_sign_event")
    def test_post_to_relay(self, mock_create_and_sign_event, mock_relay_manager_connection):
        message = "Test message"
        mock_event = MagicMock()
        mock_create_and_sign_event.return_value = mock_event
        mock_connection = MagicMock()
        mock_relay_manager_connection.return_value.__enter__.return_value = mock_connection

        post_to_relay(message)

        mock_create_and_sign_event.assert_called_with(message)
        mock_connection.publish_event.assert_called_with(mock_event)

class TestRelayManagerConnection(unittest.TestCase):
    @patch("src.post_to_relay.relay_manager")
    @patch("src.post_to_relay.time.sleep")
    def test_relay_manager_connection(self, mock_sleep, mock_relay_manager):
        with relay_manager_connection() as connection:
            self.assertEqual(connection, mock_relay_manager)

        expected_connection_options = {"cert_reqs": ssl.CERT_NONE}
        mock_relay_manager.open_connections.assert_called_once_with(expected_connection_options)
        mock_relay_manager.close_connections.assert_called_once()
        self.assertEqual(mock_sleep.call_count, 2)

class TestCreateAndSignEvent(unittest.TestCase):
    @patch("src.post_to_relay.private_key")
    @patch("src.post_to_relay.Event")
    def test_create_and_sign_event(self, mock_event_class, mock_private_key):
        message = "Test message"
        mock_event = MagicMock()
        mock_event_class.return_value = mock_event

        result = create_and_sign_event(message)

        self.assertEqual(result, mock_event)
        mock_event_class.assert_called_once_with(public_key=mock_private_key.public_key.hex(), content=message)
        mock_private_key.sign_event.assert_called_once_with(mock_event)

if __name__ == "__main__":
    unittest.main()