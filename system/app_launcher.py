import os
import subprocess
import logging


class AppLauncher:
    """
    AppLauncher handles opening applications
    installed on the system.
    """

    def __init__(self):

        logging.info("Initializing Application Launcher")

        # Known application commands
        self.app_map = {

            "chrome": "start chrome",
            "google chrome": "start chrome",

            "vscode": "code",
            "visual studio code": "code",

            "notepad": "notepad",

            "calculator": "calc",

            "cmd": "start cmd",

            "powershell": "start powershell",

            "task manager": "taskmgr",

        }

    # --------------------------------------------------
    # OPEN APPLICATION
    # --------------------------------------------------

    def open_application(self, app_name: str):
        """
        Launch application by name.
        """

        if not app_name:
            return False

        app_name = app_name.lower()

        try:

            if app_name in self.app_map:

                command = self.app_map[app_name]

                subprocess.Popen(command, shell=True)

                logging.info(f"Launching application: {app_name}")

                return True

            else:

                logging.warning(f"Unknown application: {app_name}")

                return False

        except Exception as e:

            logging.error(f"Application launch failed: {e}")

            return False

    # --------------------------------------------------
    # OPEN FILE
    # --------------------------------------------------

    def open_file(self, path: str):
        """
        Open a file with default application.
        """

        try:

            os.startfile(path)

            logging.info(f"Opening file: {path}")

            return True

        except Exception as e:

            logging.error(f"File open error: {e}")

            return False

    # --------------------------------------------------
    # OPEN FOLDER
    # --------------------------------------------------

    def open_folder(self, path: str):
        """
        Open folder in file explorer.
        """

        try:

            os.startfile(path)

            logging.info(f"Opening folder: {path}")

            return True

        except Exception as e:

            logging.error(f"Folder open error: {e}")

            return False

    # --------------------------------------------------
    # REGISTER NEW APPLICATION
    # --------------------------------------------------

    def register_application(self, name: str, command: str):
        """
        Add new application to launcher.
        """

        try:

            self.app_map[name.lower()] = command

            logging.info(f"Application registered: {name}")

        except Exception as e:

            logging.error(f"Failed to register application: {e}")