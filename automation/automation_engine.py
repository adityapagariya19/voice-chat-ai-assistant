import json
import logging
import time

from config import AUTOMATION_DATASET
from system.app_launcher import AppLauncher


class AutomationEngine:
    """
    AutomationEngine executes multi-step automation workflows
    defined in datasets/automation_tasks.json
    """

    def __init__(self):

        logging.info("Initializing Automation Engine")

        self.launcher = AppLauncher()

        self.tasks = self.load_tasks()

    # --------------------------------------------------
    # LOAD AUTOMATION DATASET
    # --------------------------------------------------

    def load_tasks(self):

        try:

            with open(AUTOMATION_DATASET, "r") as f:

                tasks = json.load(f)

                logging.info("Automation dataset loaded")

                return tasks

        except Exception as e:

            logging.error(f"Failed to load automation dataset: {e}")

            return {}

    # --------------------------------------------------
    # EXECUTE AUTOMATION
    # --------------------------------------------------

    def run_task(self, task_name):

        task_name = task_name.lower()

        if task_name not in self.tasks:

            logging.warning(f"Automation task not found: {task_name}")

            return False

        steps = self.tasks[task_name]

        logging.info(f"Executing automation task: {task_name}")

        for step in steps:

            self.execute_step(step)

            time.sleep(1)

        return True

    # --------------------------------------------------
    # EXECUTE SINGLE STEP
    # --------------------------------------------------

    def execute_step(self, step):

        step = step.lower()

        try:

            if "open chrome" in step:
                self.launcher.open_application("chrome")

            elif "open vscode" in step:
                self.launcher.open_application("vscode")

            elif "open notepad" in step:
                self.launcher.open_application("notepad")

            elif "open calculator" in step:
                self.launcher.open_application("calculator")

            elif "open cmd" in step:
                self.launcher.open_application("cmd")

            else:

                logging.warning(f"Unknown automation step: {step}")

        except Exception as e:

            logging.error(f"Automation step failed: {e}")

    # --------------------------------------------------
    # LIST TASKS
    # --------------------------------------------------

    def list_tasks(self):

        return list(self.tasks.keys())