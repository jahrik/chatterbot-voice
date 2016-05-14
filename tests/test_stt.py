from unittest import TestCase
from chatterbot.conversation import Statement
from chatterbot_voice import Voice


class SpeechToTextTests(TestCase):

    def setUp(self):
        self.adapter = Voice()

    def test_attempt_jack_control_start(self):
        """
        Test that no exceptions are triggered.
        """
        self.adapter.attempt_jack_control_start()
