import pyttsx3
import threading
import queue
import logging
import winsound

from config import (
    VOICE_RATE,
    VOICE_VOLUME,
    SOUND_STARTUP
)


class VoiceEngine:
    """
    VoiceEngine handles all text-to-speech operations
    for the JARVIS assistant.

    Features:
    - Thread-safe speech queue
    - Non-blocking voice output
    - Voice configuration
    - Startup sound
    - Graceful shutdown
    """

    def __init__(self):

        logging.info("Starting Voice Engine")

        # Initialize TTS engine
        self.engine = pyttsx3.init()

        # Speech queue
        self.queue = queue.Queue()

        # Thread lock
        self.lock = threading.Lock()

        # Running flag
        self.running = True

        # Configure engine
        self.configure_engine()

        # Start speech worker thread
        self.worker = threading.Thread(target=self._speech_worker)
        self.worker.daemon = True
        self.worker.start()

        # Play startup sound
        self.play_startup_sound()

    # --------------------------------------------------
    # ENGINE CONFIGURATION
    # --------------------------------------------------

    def configure_engine(self):
        """
        Configure voice engine parameters.
        """

        try:

            self.engine.setProperty("rate", VOICE_RATE)
            self.engine.setProperty("volume", VOICE_VOLUME)

            voices = self.engine.getProperty("voices")

            # Select first voice
            if voices:
                self.engine.setProperty("voice", voices[0].id)

        except Exception as e:
            logging.error(f"Voice configuration failed: {e}")

    # --------------------------------------------------
    # STARTUP SOUND
    # --------------------------------------------------

    def play_startup_sound(self):
        """
        Play system startup sound.
        """

        try:
            winsound.PlaySound(SOUND_STARTUP, winsound.SND_FILENAME)
        except Exception:
            pass

    # --------------------------------------------------
    # SPEAK METHOD
    # --------------------------------------------------

    def speak(self, text: str):
        """
        Add speech request to queue.
        """

        if not text:
            return

        logging.info(f"Assistant speaking: {text}")

        self.queue.put(text)

    # --------------------------------------------------
    # SPEECH WORKER THREAD
    # --------------------------------------------------

    def _speech_worker(self):
        """
        Worker thread that processes speech queue.
        """

        while self.running:

            try:

                text = self.queue.get()

                with self.lock:

                    self.engine.say(text)
                    self.engine.runAndWait()

                self.queue.task_done()

            except Exception as e:

                logging.error(f"Speech worker error: {e}")

    # --------------------------------------------------
    # CHANGE VOICE
    # --------------------------------------------------

    def set_voice(self, index: int):
        """
        Change voice by index.
        """

        try:

            voices = self.engine.getProperty("voices")

            if 0 <= index < len(voices):
                self.engine.setProperty("voice", voices[index].id)

        except Exception as e:

            logging.error(f"Voice change error: {e}")

    # --------------------------------------------------
    # CHANGE RATE
    # --------------------------------------------------

    def set_rate(self, rate: int):
        """
        Change speaking rate.
        """

        try:
            self.engine.setProperty("rate", rate)
        except Exception:
            pass

    # --------------------------------------------------
    # CHANGE VOLUME
    # --------------------------------------------------

    def set_volume(self, volume: float):
        """
        Change voice volume.
        """

        try:

            if 0.0 <= volume <= 1.0:
                self.engine.setProperty("volume", volume)

        except Exception:
            pass

    # --------------------------------------------------
    # STOP ENGINE
    # --------------------------------------------------

    def stop(self):
        """
        Stop voice engine safely.
        """

        logging.info("Stopping Voice Engine")

        self.running = False

        try:
            self.engine.stop()
        except Exception:
            pass