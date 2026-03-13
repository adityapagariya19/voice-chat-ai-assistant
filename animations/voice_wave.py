import random
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import Qt


class VoiceWave(QWidget):
    """
    Animated voice waveform used during listening
    and speaking states.
    """

    def __init__(self):

        super().__init__()

        self.bars = [0] * 30
        self.active = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_wave)
        self.timer.start(60)

        self.setMinimumHeight(120)

    # --------------------------------------------------
    # START ANIMATION
    # --------------------------------------------------

    def start(self):
        self.active = True

    # --------------------------------------------------
    # STOP ANIMATION
    # --------------------------------------------------

    def stop(self):
        self.active = False
        self.bars = [0] * 30
        self.update()

    # --------------------------------------------------
    # UPDATE WAVE
    # --------------------------------------------------

    def update_wave(self):

        if self.active:

            self.bars = [random.randint(10, 100) for _ in range(30)]

        else:

            self.bars = [max(0, b - 5) for b in self.bars]

        self.update()

    # --------------------------------------------------
    # DRAW WAVE
    # --------------------------------------------------

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        width = self.width()
        height = self.height()

        bar_width = width / len(self.bars)

        pen = QPen(QColor(0, 200, 255))
        pen.setWidth(3)

        painter.setPen(pen)

        for i, value in enumerate(self.bars):

            x = int(i * bar_width)

            y1 = int(height / 2 - value / 2)
            y2 = int(height / 2 + value / 2)

            painter.drawLine(x, y1, x, y2)