import sys
import logging

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QStackedWidget
)

from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt

from config import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    COLOR_BACKGROUND,
    COLOR_PRIMARY,
    COLOR_TEXT,
    FONT_ORBITRON,
    ICON_ASSISTANT,
    ICON_SETTINGS,
    ICON_CHAT,
    ICON_CPU
)

from ui.dashboard import Dashboard
from ui.voice_interface import VoiceInterface
from ui.chat_panel import ChatPanel
from ui.settings_panel import SettingsPanel


class MainWindow(QMainWindow):
    """
    Main application window for the JARVIS interface.
    """

    def __init__(self):

        super().__init__()

        logging.info("Launching Main Window")

        self.setWindowTitle("JARVIS AI Assistant")

        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.setStyleSheet(
            f"""
            QMainWindow {{
                background-color: {COLOR_BACKGROUND};
                color: {COLOR_TEXT};
            }}
            """
        )

        self.init_ui()

    # --------------------------------------------------
    # UI INITIALIZATION
    # --------------------------------------------------

    def init_ui(self):

        # Central container
        container = QWidget()

        main_layout = QHBoxLayout()

        # Sidebar
        sidebar = self.create_sidebar()

        # Content area
        self.stack = QStackedWidget()

        self.dashboard = Dashboard()
        self.voice_panel = VoiceInterface()
        self.chat_panel = ChatPanel()
        self.settings_panel = SettingsPanel()

        self.stack.addWidget(self.dashboard)
        self.stack.addWidget(self.voice_panel)
        self.stack.addWidget(self.chat_panel)
        self.stack.addWidget(self.settings_panel)

        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.stack)

        container.setLayout(main_layout)

        self.setCentralWidget(container)

    # --------------------------------------------------
    # SIDEBAR
    # --------------------------------------------------

    def create_sidebar(self):

        sidebar = QWidget()

        layout = QVBoxLayout()

        # Title
        title = QLabel("JARVIS")

        font = QFont()
        font.setPointSize(20)

        title.setFont(font)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title)

        # Buttons

        btn_dashboard = QPushButton("Dashboard")
        btn_voice = QPushButton("Voice")
        btn_chat = QPushButton("Chat")
        btn_settings = QPushButton("Settings")

        btn_dashboard.clicked.connect(
            lambda: self.stack.setCurrentIndex(0)
        )

        btn_voice.clicked.connect(
            lambda: self.stack.setCurrentIndex(1)
        )

        btn_chat.clicked.connect(
            lambda: self.stack.setCurrentIndex(2)
        )

        btn_settings.clicked.connect(
            lambda: self.stack.setCurrentIndex(3)
        )

        layout.addWidget(btn_dashboard)
        layout.addWidget(btn_voice)
        layout.addWidget(btn_chat)
        layout.addWidget(btn_settings)

        layout.addStretch()

        sidebar.setLayout(layout)

        sidebar.setFixedWidth(200)

        sidebar.setStyleSheet(
            f"""
            background-color: {COLOR_PRIMARY};
            color: black;
            """
        )

        return sidebar


# --------------------------------------------------
# APPLICATION ENTRY
# --------------------------------------------------

def launch_app():

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())