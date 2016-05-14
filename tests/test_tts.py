from unittest import TestCase
from chatterbot.conversation import Statement
from chatterbot_voice import Voice


class TextToSpeechTests(TestCase):

    def setUp(self):
        self.adapter = Voice()

    def test_response_returned(self):
        """
        Test that a response statement is returned from the adapter.
        """
        statement = Statement("Testing speech synthesis.")

        self.assertEqual(
            self.adapter.process_response(statement),
            statement.text
        )
