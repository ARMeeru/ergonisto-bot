from unittest.mock import Mock
from main import echo

# Create a test function to test the echo function
def test_echo():
    update = Mock()
    context = Mock()
    update.message.text = "Hello"
    update.message.reply_text = Mock()
    echo(update, context)
    update.message.reply_text.assert_called_with("Hello")

# Run the test
test_echo()

# Print to console if the test passed
print("Yo Ho Ho and a Bottle of Rum!")