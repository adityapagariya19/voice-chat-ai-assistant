import sys
import logging

from PyQt6.QtWidgets import QApplication

from core.assistant_core import AssistantCore
from ui.main_window import MainWindow


# --------------------------------------------------
# LOGGING
# --------------------------------------------------

def setup_logging():

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )


# --------------------------------------------------
# MAIN FUNCTION
# --------------------------------------------------

def main():

    setup_logging()

    logging.info("Starting JARVIS AI System")

    # Initialize assistant core
    assistant = AssistantCore()

    assistant.start()

    # Start UI
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())


# --------------------------------------------------
# ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":
    main()