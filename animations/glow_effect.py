from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import Qt


class GlowWidget(QWidget):
    """
    Widget with glowing neon border effect.
    """

    def __init__(self, color=(0, 200, 255), thickness=3):

        super().__init__()

        self.glow_color = QColor(*color)

        self.thickness = thickness

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    # --------------------------------------------------
    # PAINT EVENT
    # --------------------------------------------------

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Glow layers
        for i in range(1, 6):

            pen = QPen(self.glow_color)

            pen.setWidth(self.thickness + i * 2)

            pen.setColor(QColor(
                self.glow_color.red(),
                self.glow_color.green(),
                self.glow_color.blue(),
                30
            ))

            painter.setPen(pen)

            painter.drawRect(self.rect())

        # Main border
        pen = QPen(self.glow_color)

        pen.setWidth(self.thickness)

        painter.setPen(pen)

        painter.drawRect(self.rect())