from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import Qt
import math


class HudRings(QWidget):
    """
    Animated rotating HUD rings similar to JARVIS interface.
    """

    def __init__(self):

        super().__init__()

        self.angle_outer = 0
        self.angle_middle = 0
        self.angle_inner = 0

        # Timer for animation
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(30)

        self.setMinimumSize(300, 300)

    # --------------------------------------------------
    # UPDATE ANIMATION
    # --------------------------------------------------

    def update_animation(self):

        self.angle_outer += 1
        self.angle_middle -= 2
        self.angle_inner += 3

        self.update()

    # --------------------------------------------------
    # PAINT EVENT
    # --------------------------------------------------

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        center_x = self.width() / 2
        center_y = self.height() / 2

        # Outer Ring
        painter.setPen(QPen(QColor(0, 200, 255), 3))
        self.draw_ring(painter, center_x, center_y, 120, self.angle_outer)

        # Middle Ring
        painter.setPen(QPen(QColor(0, 150, 255), 2))
        self.draw_ring(painter, center_x, center_y, 90, self.angle_middle)

        # Inner Ring
        painter.setPen(QPen(QColor(0, 255, 200), 2))
        self.draw_ring(painter, center_x, center_y, 60, self.angle_inner)

    # --------------------------------------------------
    # DRAW RING
    # --------------------------------------------------

    def draw_ring(self, painter, cx, cy, radius, angle):

        segments = 12

        for i in range(segments):

            start_angle = angle + i * (360 / segments)

            rad = math.radians(start_angle)

            x1 = cx + radius * math.cos(rad)
            y1 = cy + radius * math.sin(rad)

            rad2 = math.radians(start_angle + 10)

            x2 = cx + radius * math.cos(rad2)
            y2 = cy + radius * math.sin(rad2)

            painter.drawLine(int(x1), int(y1), int(x2), int(y2))