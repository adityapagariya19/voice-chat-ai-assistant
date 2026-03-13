import json
import threading

from config import COMMANDS_DATASET
from database.db_manager import DatabaseManager
from voice.voice_engine import VoiceEngine
from voice.speech_listener import SpeechListener
from core.command_processor import CommandProcessor
from automation.automation_engine import AutomationEngine
from system.resource_monitor import ResourceMonitor


class AssistantCore:
    """
    Central control unit of the JARVIS AI system.
    Responsible for coordinating all subsystems.
    """

    def __init__(self):

        print("Initializing JARVIS Core...")

        # --------------------------------------------------
        # DATABASE
        # --------------------------------------------------

        self.database = DatabaseManager()

        # --------------------------------------------------
        # VOICE SYSTEM
        # --------------------------------------------------

        self.voice_engine = VoiceEngine()

        # Try initializing microphone
        try:
            self.listener = SpeechListener()
            print("Microphone initialized successfully")
        except Exception:
            print("Microphone not available. Voice input disabled.")
            self.listener = None

        # --------------------------------------------------
        # COMMAND SYSTEM
        # --------------------------------------------------

        self.command_processor = CommandProcessor()

        # --------------------------------------------------
        # AUTOMATION
        # --------------------------------------------------

        self.automation_engine = AutomationEngine()

        # --------------------------------------------------
        # SYSTEM MONITOR
        # --------------------------------------------------

        self.system_monitor = ResourceMonitor()

        # --------------------------------------------------
        # DATASETS
        # --------------------------------------------------

        self.commands_dataset = self.load_commands_dataset()

        # --------------------------------------------------
        # RUNNING STATE
        # --------------------------------------------------

        self.running = False

    # ------------------------------------------------------
    # LOAD DATASETS
    # ------------------------------------------------------

    def load_commands_dataset(self):

        try:
            with open(COMMANDS_DATASET, "r") as f:
                return json.load(f)
        except Exception as e:
            print("Failed to load commands dataset:", e)
            return {}

    # ------------------------------------------------------
    # START ASSISTANT
    # ------------------------------------------------------

    def start(self):

        self.running = True

        print("JARVIS AI System Started")

        self.voice_engine.speak("Hello sir. Jarvis system is now online.")

        self.database.log_system_event("Assistant started")

        # Start listening thread
        listener_thread = threading.Thread(target=self.listen_loop)
        listener_thread.daemon = True
        listener_thread.start()

    # ------------------------------------------------------
    # MAIN LISTENING LOOP
    # ------------------------------------------------------

    def listen_loop(self):

        while self.running:

            try:

                command = None

                # Only listen if microphone exists
                if self.listener:
                    command = self.listener.listen()

                if command:

                    print("User:", command)

                    # Log command
                    self.database.log_command(command)

                    response = self.command_processor.process_command(
                        command,
                        self.commands_dataset,
                        self.automation_engine,
                        self.system_monitor
                    )

                    if response:
                        self.voice_engine.speak(response)

            except Exception as e:
                print("Error in listen loop:", e)

    # ------------------------------------------------------
    # STOP ASSISTANT
    # ------------------------------------------------------

    def stop(self):

        self.running = False

        self.voice_engine.speak("Shutting down system")

        self.database.log_system_event("Assistant stopped")

        self.database.close()

        print("Assistant stopped")