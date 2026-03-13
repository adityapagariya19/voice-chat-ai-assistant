import logging
from config import WAKE_WORD


class WakeWordDetector:
    """
    WakeWordDetector ensures the assistant only responds
    when the wake word (e.g. 'jarvis') is spoken.

    Example command:
        "jarvis open youtube"

    The detector extracts:
        "open youtube"
    """

    def __init__(self):

        self.wake_word = WAKE_WORD.lower()

        logging.info(f"Wake word set to: {self.wake_word}")

    # --------------------------------------------------
    # CHECK WAKE WORD
    # --------------------------------------------------

    def detect(self, text: str):
        """
        Check if the wake word exists in speech.
        Returns command without wake word.
        """

        if not text:
            return None

        text = text.lower()

        if self.wake_word in text:

            # Remove wake word
            command = text.replace(self.wake_word, "").strip()

            if command == "":
                return None

            return command

        return None

    # --------------------------------------------------
    # STRICT MATCH
    # --------------------------------------------------

    def strict_detect(self, text: str):
        """
        Only accept commands starting with wake word.

        Example:
            'jarvis open youtube' -> accepted
            'open youtube jarvis' -> rejected
        """

        if not text:
            return None

        text = text.lower()

        if text.startswith(self.wake_word):

            command = text[len(self.wake_word):].strip()

            if command == "":
                return None

            return command

        return None

    # --------------------------------------------------
    # CHECK ONLY
    # --------------------------------------------------

    def is_wake_word_present(self, text: str):
        """
        Simple check if wake word exists.
        """

        if not text:
            return False

        return self.wake_word in text.lower()