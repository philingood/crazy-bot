from unittest.mock import MagicMock, patch

import pytest
from handlers.ask_gpt import ask_g4f


@pytest.mark.required
@pytest.mark.parametrize("response_content", ["Hello response"])
@patch("handlers.ask_gpt.Client")
@patch("handlers.ask_gpt.SYSTEMMSG", "Hello, system!")
def test_ask_g4f(mock_client, response_content):
    mock_create = mock_client.return_value.chat.completions.create
    mock_create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content=response_content))]
    )

    response = ask_g4f(message="Hello", client=mock_client())
    assert response == response_content

    mock_create.assert_called_once_with(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Hello, system!"},
            {"role": "user", "content": "Hello"},
        ],
    )


if __name__ == "__main__":
    pytest.main()
