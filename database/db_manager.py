import sqlite3
import os
from config import DATABASE_FILE, SCHEMA_FILE


class DatabaseManager:
    """
    Central database manager for the JARVIS system.
    Handles initialization, schema loading, and data operations.
    """

    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connect()
        self.initialize_database()

    # -------------------------------------------------------
    # CONNECT DATABASE
    # -------------------------------------------------------

    def connect(self):
        """Create database connection."""
        self.connection = sqlite3.connect(DATABASE_FILE)
        self.cursor = self.connection.cursor()

    # -------------------------------------------------------
    # INITIALIZE DATABASE
    # -------------------------------------------------------

    def initialize_database(self):
        """Load schema.sql and create tables if not present."""
        if not os.path.exists(DATABASE_FILE):
            print("Creating database...")

        with open(SCHEMA_FILE, "r") as f:
            schema = f.read()

        self.cursor.executescript(schema)
        self.connection.commit()

    # -------------------------------------------------------
    # COMMAND LOGGING
    # -------------------------------------------------------

    def log_command(self, command_text):
        """Save executed command."""
        query = """
        INSERT INTO commands (command)
        VALUES (?)
        """
        self.cursor.execute(query, (command_text,))
        self.connection.commit()

    def get_command_history(self, limit=20):
        """Return recent command history."""
        query = """
        SELECT command, timestamp
        FROM commands
        ORDER BY timestamp DESC
        LIMIT ?
        """
        self.cursor.execute(query, (limit,))
        return self.cursor.fetchall()

    # -------------------------------------------------------
    # NOTES
    # -------------------------------------------------------

    def add_note(self, title, content):
        query = """
        INSERT INTO notes (title, content)
        VALUES (?, ?)
        """
        self.cursor.execute(query, (title, content))
        self.connection.commit()

    def get_notes(self):
        query = """
        SELECT id, title, content, created_at
        FROM notes
        ORDER BY created_at DESC
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    # -------------------------------------------------------
    # REMINDERS
    # -------------------------------------------------------

    def add_reminder(self, task, remind_time):
        query = """
        INSERT INTO reminders (task, remind_time)
        VALUES (?, ?)
        """
        self.cursor.execute(query, (task, remind_time))
        self.connection.commit()

    def get_reminders(self):
        query = """
        SELECT id, task, remind_time
        FROM reminders
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    # -------------------------------------------------------
    # SYSTEM LOGS
    # -------------------------------------------------------

    def log_system_event(self, message):
        query = """
        INSERT INTO system_logs (log)
        VALUES (?)
        """
        self.cursor.execute(query, (message,))
        self.connection.commit()

    def get_logs(self, limit=50):
        query = """
        SELECT log, timestamp
        FROM system_logs
        ORDER BY timestamp DESC
        LIMIT ?
        """
        self.cursor.execute(query, (limit,))
        return self.cursor.fetchall()

    # -------------------------------------------------------
    # CLOSE CONNECTION
    # -------------------------------------------------------

    def close(self):
        if self.connection:
            self.connection.close()