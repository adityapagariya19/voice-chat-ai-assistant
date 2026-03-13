import os
import subprocess
import logging


class SystemController:
    """
    SystemController manages system power operations
    such as shutdown, restart, sleep, and lock.
    """

    def __init__(self):

        logging.info("Initializing System Controller")

    # --------------------------------------------------
    # SHUTDOWN COMPUTER
    # --------------------------------------------------

    def shutdown(self, delay=0):
        """
        Shutdown the computer after delay seconds.
        """

        try:

            command = f"shutdown /s /t {delay}"

            subprocess.Popen(command, shell=True)

            logging.info("System shutdown initiated")

            return True

        except Exception as e:

            logging.error(f"Shutdown failed: {e}")

            return False

    # --------------------------------------------------
    # RESTART COMPUTER
    # --------------------------------------------------

    def restart(self, delay=0):
        """
        Restart the computer after delay seconds.
        """

        try:

            command = f"shutdown /r /t {delay}"

            subprocess.Popen(command, shell=True)

            logging.info("System restart initiated")

            return True

        except Exception as e:

            logging.error(f"Restart failed: {e}")

            return False

    # --------------------------------------------------
    # CANCEL SHUTDOWN
    # --------------------------------------------------

    def cancel_shutdown(self):
        """
        Cancel scheduled shutdown or restart.
        """

        try:

            subprocess.Popen("shutdown /a", shell=True)

            logging.info("Shutdown cancelled")

            return True

        except Exception as e:

            logging.error(f"Cancel shutdown failed: {e}")

            return False

    # --------------------------------------------------
    # LOCK COMPUTER
    # --------------------------------------------------

    def lock(self):
        """
        Lock the workstation.
        """

        try:

            subprocess.Popen(
                "rundll32.exe user32.dll,LockWorkStation",
                shell=True
            )

            logging.info("System locked")

            return True

        except Exception as e:

            logging.error(f"Lock failed: {e}")

            return False

    # --------------------------------------------------
    # SLEEP MODE
    # --------------------------------------------------

    def sleep(self):
        """
        Put computer into sleep mode.
        """

        try:

            subprocess.Popen(
                "rundll32.exe powrprof.dll,SetSuspendState 0,1,0",
                shell=True
            )

            logging.info("System sleep initiated")

            return True

        except Exception as e:

            logging.error(f"Sleep failed: {e}")

            return False

    # --------------------------------------------------
    # LOG OUT USER
    # --------------------------------------------------

    def logout(self):
        """
        Log out current user.
        """

        try:

            subprocess.Popen("shutdown /l", shell=True)

            logging.info("User logout initiated")

            return True

        except Exception as e:

            logging.error(f"Logout failed: {e}")

            return False