from unittest import TestCase
from chatterbot_voice import VoiceInput


class SpeechToTextTests(TestCase):

    def setUp(self):
        self.adapter = VoiceInput()

    def test_attempt_jack_control_start(self):
        """
        Test that no exceptions are triggered.
        """
        self.adapter.attempt_jack_control_start()
