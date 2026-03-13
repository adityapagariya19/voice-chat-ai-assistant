import speech_recognition as sr
import logging
import winsound

from config import (
    LISTEN_TIMEOUT,
    SOUND_LISTENING,
    SOUND_COMMAND
)


class SpeechListener:
    """
    SpeechListener handles microphone input
    and converts speech into text commands.

    Features:
    - microphone calibration
    - ambient noise adjustment
    - timeout handling
    - command confirmation sound
    """

    def __init__(self):

        logging.info("Initializing Speech Listener")

        # Speech recognition engine
        self.recognizer = sr.Recognizer()

        # Microphone device
        self.microphone = sr.Microphone()

        # Calibrate microphone
        self.calibrate_microphone()

    # --------------------------------------------------
    # MICROPHONE CALIBRATION
    # --------------------------------------------------

    def calibrate_microphone(self):
        """
        Adjust microphone for ambient noise.
        """

        try:

            with self.microphone as source:

                print("Calibrating microphone...")

                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=2
                )

                print("Microphone ready")

        except Exception as e:

            logging.error(f"Microphone calibration failed: {e}")

    # --------------------------------------------------
    # PLAY LISTENING SOUND
    # --------------------------------------------------

    def play_listening_sound(self):
        """
        Play sound when assistant starts listening.
        """

        try:
            winsound.PlaySound(
                SOUND_LISTENING,
                winsound.SND_FILENAME | winsound.SND_ASYNC
            )
        except Exception:
            pass

    # --------------------------------------------------
    # PLAY COMMAND SOUND
    # --------------------------------------------------

    def play_command_sound(self):
        """
        Play sound when command is detected.
        """

        try:
            winsound.PlaySound(
                SOUND_COMMAND,
                winsound.SND_FILENAME | winsound.SND_ASYNC
            )
        except Exception:
            pass

    # --------------------------------------------------
    # MAIN LISTEN METHOD
    # --------------------------------------------------

    def listen(self):
        """
        Capture voice command from microphone.
        Returns recognized text.
        """

        try:

            with self.microphone as source:

                self.play_listening_sound()

                print("Listening...")

                audio = self.recognizer.listen(
                    source,
                    timeout=LISTEN_TIMEOUT,
                    phrase_time_limit=8
                )

            command = self.recognize(audio)

            if command:

                self.play_command_sound()

                return command.lower()

            return None

        except sr.WaitTimeoutError:

            # No speech detected
            return None

        except Exception as e:

            logging.error(f"Listening error: {e}")
            return None

    # --------------------------------------------------
    # SPEECH RECOGNITION
    # --------------------------------------------------

    def recognize(self, audio):
        """
        Convert audio into text.
        """

        try:

            text = self.recognizer.recognize_google(audio)

            print(f"User said: {text}")

            return text

        except sr.UnknownValueError:

            print("Could not understand audio")

            return None

        except sr.RequestError:

            print("Speech recognition service unavailable")

            return None