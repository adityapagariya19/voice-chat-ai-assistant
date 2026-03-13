from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QPushButton
)

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon

from config import ICON_MIC


class VoiceInterface(QWidget):
    """
    Voice interface panel for interacting with JARVIS using speech.
    """

    def __init__(self):

        super().__init__()

        self.init_ui()

    # --------------------------------------------------
    # UI SETUP
    # --------------------------------------------------

    def init_ui(self):

        main_layout = QVBoxLayout()

        # Title
        title = QLabel("VOICE COMMAND INTERFACE")

        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title.setFont(QFont("Orbitron", 24))

        main_layout.addWidget(title)

        # Listening Status
        self.status_label = QLabel("Status: Idle")

        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.status_label.setFont(QFont("Orbitron", 16))

        main_layout.addWidget(self.status_label)

        # Recognized Command
        self.command_label = QLabel("Command: None")

        self.command_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.command_label.setFont(QFont("Orbitron", 16))

        main_layout.addWidget(self.command_label)

        # Assistant Response
        self.response_label = QLabel("Response: Waiting")

        self.response_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.response_label.setFont(QFont("Orbitron", 16))

        main_layout.addWidget(self.response_label)

        # Microphone Button
        self.mic_button = QPushButton()

        self.mic_button.setIcon(QIcon(ICON_MIC))

        self.mic_button.setIconSize(self.mic_button.sizeHint())

        self.mic_button.setFixedSize(100, 100)

        self.mic_button.clicked.connect(self.toggle_listening)

        main_layout.addWidget(self.mic_button, alignment=Qt.AlignmentFlag.AlignCenter)

        main_layout.addStretch()

        self.setLayout(main_layout)

    # --------------------------------------------------
    # TOGGLE LISTENING
    # --------------------------------------------------

    def toggle_listening(self):

        if self.status_label.text() == "Status: Idle":

            self.status_label.setText("Status: Listening...")

        else:

            self.status_label.setText("Status: Idle")

    # --------------------------------------------------
    # UPDATE COMMAND
    # --------------------------------------------------

    def update_command(self, command):

        self.command_label.setText(f"Command: {command}")

    # --------------------------------------------------
    # UPDATE RESPONSE
    # --------------------------------------------------

    def update_response(self, response):

        self.response_label.setText(f"Response: {response}")