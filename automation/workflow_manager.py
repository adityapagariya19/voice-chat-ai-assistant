import json
import logging
import threading
import time

from config import AUTOMATION_DATASET
from automation.automation_engine import AutomationEngine


class WorkflowManager:
    """
    WorkflowManager handles creation, scheduling,
    and management of automation workflows.
    """

    def __init__(self):

        logging.info("Initializing Workflow Manager")

        self.engine = AutomationEngine()

        self.workflows = self.load_workflows()

        self.scheduled_tasks = []

    # --------------------------------------------------
    # LOAD WORKFLOWS
    # --------------------------------------------------

    def load_workflows(self):

        try:

            with open(AUTOMATION_DATASET, "r") as f:

                data = json.load(f)

                return data

        except Exception as e:

            logging.error(f"Workflow load error: {e}")

            return {}

    # --------------------------------------------------
    # SAVE WORKFLOWS
    # --------------------------------------------------

    def save_workflows(self):

        try:

            with open(AUTOMATION_DATASET, "w") as f:

                json.dump(self.workflows, f, indent=4)

        except Exception as e:

            logging.error(f"Workflow save error: {e}")

    # --------------------------------------------------
    # CREATE WORKFLOW
    # --------------------------------------------------

    def create_workflow(self, name, steps):

        name = name.lower()

        if name in self.workflows:

            logging.warning("Workflow already exists")

            return False

        self.workflows[name] = steps

        self.save_workflows()

        logging.info(f"Workflow created: {name}")

        return True

    # --------------------------------------------------
    # DELETE WORKFLOW
    # --------------------------------------------------

    def delete_workflow(self, name):

        name = name.lower()

        if name not in self.workflows:

            return False

        del self.workflows[name]

        self.save_workflows()

        logging.info(f"Workflow deleted: {name}")

        return True

    # --------------------------------------------------
    # LIST WORKFLOWS
    # --------------------------------------------------

    def list_workflows(self):

        return list(self.workflows.keys())

    # --------------------------------------------------
    # RUN WORKFLOW
    # --------------------------------------------------

    def run_workflow(self, name):

        name = name.lower()

        if name not in self.workflows:

            logging.warning("Workflow not found")

            return False

        return self.engine.run_task(name)

    # --------------------------------------------------
    # SCHEDULE WORKFLOW
    # --------------------------------------------------

    def schedule_workflow(self, name, delay_seconds):

        def task():

            time.sleep(delay_seconds)

            self.run_workflow(name)

        thread = threading.Thread(target=task)

        thread.daemon = True

        thread.start()

        self.scheduled_tasks.append(thread)

        logging.info(f"Workflow scheduled: {name}")

        return True