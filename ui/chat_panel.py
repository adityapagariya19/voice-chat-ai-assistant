from PyQt6.QtWidgets import (
    QWidget,
    QTextEdit,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLabel
)

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from core.command_processor import CommandProcessor
from automation.automation_engine import AutomationEngine
from system.resource_monitor import ResourceMonitor


class ChatPanel(QWidget):

    def __init__(self):

        super().__init__()

        # Initialize assistant modules
        self.processor = CommandProcessor()
        self.automation = AutomationEngine()
        self.system_monitor = ResourceMonitor()

        # Temporary commands dataset
        self.commands_dataset = {
            "open_youtube": ["open youtube", "youtube"],
            "open_google": ["open google", "google"]
        }

        self.init_ui()

    # -------------------------
    # UI
    # -------------------------

    def init_ui(self):

        layout = QVBoxLayout()

        title = QLabel("AI CHAT INTERFACE")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Orbitron", 20))

        layout.addWidget(title)

        # Chat history
        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)

        layout.addWidget(self.chat_history)

        # Input
        input_layout = QHBoxLayout()

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type command...")

        send_button = QPushButton("Send")
        send_button.clicked.connect(self.send_message)

        input_layout.addWidget(self.input_field)
        input_layout.addWidget(send_button)

        layout.addLayout(input_layout)

        self.setLayout(layout)

    # -------------------------
    # SEND MESSAGE
    # -------------------------

    def send_message(self):

        command = self.input_field.text()

        if not command:
            return

        self.chat_history.append(f"User: {command}")

        response = self.processor.process_command(
            command,
            self.commands_dataset,
            self.automation,
            self.system_monitor
        )

        if response:
            self.chat_history.append(f"JARVIS: {response}")

        self.input_field.clear()