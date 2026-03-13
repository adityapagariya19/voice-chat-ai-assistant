from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont

from system.resource_monitor import ResourceMonitor


class Dashboard(QWidget):
    """
    Futuristic dashboard showing system status.
    """

    def __init__(self):

        super().__init__()

        self.monitor = ResourceMonitor()

        self.init_ui()

        self.start_monitoring()

    # --------------------------------------------------
    # UI SETUP
    # --------------------------------------------------

    def init_ui(self):

        main_layout = QVBoxLayout()

        # Title
        title = QLabel("SYSTEM DASHBOARD")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        font = QFont()
        font.setPointSize(26)
        font.setBold(True)

        title.setFont(font)

        main_layout.addWidget(title)

        # Stats Layout
        stats_layout = QHBoxLayout()

        # CPU Label
        self.cpu_label = QLabel("CPU: 0%")
        self.cpu_label.setFont(QFont("Orbitron", 20))

        # RAM Label
        self.ram_label = QLabel("RAM: 0%")
        self.ram_label.setFont(QFont("Orbitron", 20))

        # Disk Label
        self.disk_label = QLabel("DISK: 0%")
        self.disk_label.setFont(QFont("Orbitron", 20))

        stats_layout.addWidget(self.cpu_label)
        stats_layout.addWidget(self.ram_label)
        stats_layout.addWidget(self.disk_label)

        main_layout.addLayout(stats_layout)

        # System Info
        self.info_label = QLabel("System Monitoring Active")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.info_label.setFont(QFont("Orbitron", 16))

        main_layout.addWidget(self.info_label)

        main_layout.addStretch()

        self.setLayout(main_layout)

    # --------------------------------------------------
    # START MONITOR
    # --------------------------------------------------

    def start_monitoring(self):

        self.timer = QTimer()

        self.timer.timeout.connect(self.update_stats)

        self.timer.start(2000)

    # --------------------------------------------------
    # UPDATE SYSTEM STATS
    # --------------------------------------------------

    def update_stats(self):

        cpu = self.monitor.get_cpu()

        ram = self.monitor.get_ram()

        disk = self.monitor.get_disk()

        self.cpu_label.setText(f"CPU: {cpu}%")

        self.ram_label.setText(f"RAM: {ram}%")

        self.disk_label.setText(f"DISK: {disk}%")