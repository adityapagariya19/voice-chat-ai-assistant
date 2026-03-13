import os


# -------------------------------------------------------
# BASE PROJECT DIRECTORY
# -------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# -------------------------------------------------------
# ASSETS
# -------------------------------------------------------

ASSETS_DIR = os.path.join(BASE_DIR, "assets")

IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
ICONS_DIR = os.path.join(ASSETS_DIR, "icons")
SOUNDS_DIR = os.path.join(ASSETS_DIR, "sounds")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")


# -------------------------------------------------------
# IMAGE FILES
# -------------------------------------------------------

DASHBOARD_BACKGROUND = os.path.join(IMAGES_DIR, "dashboard_bg.png")

HUD_OUTER_RING = os.path.join(IMAGES_DIR, "hud_outer.png")
HUD_MIDDLE_RING = os.path.join(IMAGES_DIR, "hud_middle.png")
HUD_INNER_RING = os.path.join(IMAGES_DIR, "hud_inner.png")

VOICE_WAVE_IMAGE = os.path.join(IMAGES_DIR, "voice_wave.png")


# -------------------------------------------------------
# ICON FILES
# -------------------------------------------------------

ICON_MIC = os.path.join(ICONS_DIR, "mic.png")
ICON_ASSISTANT = os.path.join(ICONS_DIR, "assistant.png")
ICON_SETTINGS = os.path.join(ICONS_DIR, "settings.png")
ICON_CPU = os.path.join(ICONS_DIR, "cpu.png")
ICON_CHAT = os.path.join(ICONS_DIR, "chat.png")
ICON_AUTOMATION = os.path.join(ICONS_DIR, "automation.png")


# -------------------------------------------------------
# SOUND FILES
# -------------------------------------------------------

SOUND_STARTUP = os.path.join(SOUNDS_DIR, "startup.wav")
SOUND_LISTENING = os.path.join(SOUNDS_DIR, "listening.wav")
SOUND_COMMAND = os.path.join(SOUNDS_DIR, "command.wav")
SOUND_NOTIFICATION = os.path.join(SOUNDS_DIR, "notification.wav")


# -------------------------------------------------------
# FONT FILE
# -------------------------------------------------------

FONT_ORBITRON = os.path.join(FONTS_DIR, "orbitron.ttf")


# -------------------------------------------------------
# DATASET PATHS
# -------------------------------------------------------

DATASETS_DIR = os.path.join(BASE_DIR, "datasets")

COMMANDS_DATASET = os.path.join(DATASETS_DIR, "commands.json")
AUTOMATION_DATASET = os.path.join(DATASETS_DIR, "automation_tasks.json")
CONVERSATION_DATASET = os.path.join(DATASETS_DIR, "conversations.json")


# -------------------------------------------------------
# DATABASE
# -------------------------------------------------------

DATABASE_DIR = os.path.join(BASE_DIR, "database")

DATABASE_FILE = os.path.join(DATABASE_DIR, "jarvis.db")

SCHEMA_FILE = os.path.join(DATABASE_DIR, "schema.sql")


# -------------------------------------------------------
# VOICE SETTINGS
# -------------------------------------------------------

VOICE_RATE = 160
VOICE_VOLUME = 1.0


# -------------------------------------------------------
# SYSTEM SETTINGS
# -------------------------------------------------------

WAKE_WORD = "jarvis"

LISTEN_TIMEOUT = 5

COMMAND_COOLDOWN = 1


# -------------------------------------------------------
# UI SETTINGS
# -------------------------------------------------------

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

UI_THEME = "dark"


# -------------------------------------------------------
# COLORS (FUTURISTIC HUD STYLE)
# -------------------------------------------------------

COLOR_BACKGROUND = "#0b0c10"
COLOR_PRIMARY = "#00eaff"
COLOR_SECONDARY = "#66fcf1"
COLOR_ACCENT = "#1f2833"
COLOR_TEXT = "#ffffff"


# -------------------------------------------------------
# LOGGING
# -------------------------------------------------------

LOG_LEVEL = "INFO"


# -------------------------------------------------------
# DEBUG MODE
# -------------------------------------------------------

DEBUG = True