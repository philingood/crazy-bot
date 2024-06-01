import unittest
from unittest.mock import patch, MagicMock

from handlers.ask_gpt import ask_gpt


class TestAskGpt(unittest.TestCase):
    @patch("handlers.ask_gpt.Client")
    @patch("handlers.ask_gpt.SYSTEMMSG", "Hello, system!")
    def test_ask_gpt(self, MockClient):
        mock_create = MockClient.return_value.chat.completions.create
        mock_create.return_value = MagicMock(
            choices=[MagicMock(message=MagicMock(content="Hello response"))]
        )

        response = ask_gpt(client=MockClient())

        self.assertEqual(response, "Hello response")
        mock_create.assert_called_once_with(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Hello, system!"},
                {"role": "user", "content": "Hello"},
            ],
        )


if __name__ == "__main__":
    unittest.main()

