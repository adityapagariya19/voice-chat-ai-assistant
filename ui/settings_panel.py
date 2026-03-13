from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QSlider,
    QPushButton,
    QLineEdit
)

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class SettingsPanel(QWidget):
    """
    Settings panel for configuring JARVIS assistant.
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
        title = QLabel("SYSTEM SETTINGS")

        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title.setFont(QFont("Orbitron", 22))

        main_layout.addWidget(title)

        # -------------------------------
        # Voice Speed
        # -------------------------------

        speed_layout = QHBoxLayout()

        speed_label = QLabel("Voice Speed")

        speed_label.setFont(QFont("Orbitron", 14))

        self.speed_slider = QSlider(Qt.Orientation.Horizontal)

        self.speed_slider.setMinimum(100)
        self.speed_slider.setMaximum(300)
        self.speed_slider.setValue(180)

        speed_layout.addWidget(speed_label)
        speed_layout.addWidget(self.speed_slider)

        main_layout.addLayout(speed_layout)

        # -------------------------------
        # Voice Volume
        # -------------------------------

        volume_layout = QHBoxLayout()

        volume_label = QLabel("Voice Volume")

        volume_label.setFont(QFont("Orbitron", 14))

        self.volume_slider = QSlider(Qt.Orientation.Horizontal)

        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(80)

        volume_layout.addWidget(volume_label)
        volume_layout.addWidget(self.volume_slider)

        main_layout.addLayout(volume_layout)

        # -------------------------------
        # Wake Word
        # -------------------------------

        wake_layout = QHBoxLayout()

        wake_label = QLabel("Wake Word")

        wake_label.setFont(QFont("Orbitron", 14))

        self.wake_input = QLineEdit()

        self.wake_input.setPlaceholderText("jarvis")

        wake_layout.addWidget(wake_label)
        wake_layout.addWidget(self.wake_input)

        main_layout.addLayout(wake_layout)

        # -------------------------------
        # Save Button
        # -------------------------------

        save_button = QPushButton("Save Settings")

        save_button.clicked.connect(self.save_settings)

        main_layout.addWidget(save_button)

        main_layout.addStretch()

        self.setLayout(main_layout)

    # --------------------------------------------------
    # SAVE SETTINGS
    # --------------------------------------------------

    def save_settings(self):

        speed = self.speed_slider.value()

        volume = self.volume_slider.value()

        wake_word = self.wake_input.text()

        print("Settings saved:")
        print("Voice Speed:", speed)
        print("Voice Volume:", volume)
        print("Wake Word:", wake_word)