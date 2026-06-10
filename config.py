"""
Game Configuration and Constants
"""
from enum import Enum

class Difficulty(Enum):
    """Game difficulty levels with range and attempts"""
    EASY = (1, 50, 10)      # range, attempts
    MEDIUM = (1, 100, 7)
    HARD = (1, 200, 5)
    EXPERT = (1, 1000, 4)

# Game constants
GAME_MODES = {
    "1": ("classic", "Classic Mode (Guess a number)"),
    "2": ("survival", "Survival Mode (Increasing difficulty)"),
    "3": ("speed", "Speed Mode (Race against time)"),
    "4": ("multiplayer", "Multiplayer Mode (2 players compete)"),
    "5": ("reverse", "Reverse Mode (AI guesses your number)"),
    "6": ("endless", "Endless Mode (Max streak challenge)"),
    "7": ("stats", "View Statistics")
}

STATS_FILE = "game_stats.json"
MAX_HINTS = 3
SURVIVAL_ROUNDS_TO_WIN = 5
MULTIPLAYER_ROUNDS = 3
ENDLESS_STREAK_TARGET = 5

# Speed mode time limits (seconds)
SPEED_TIME_LIMITS = {
    "EASY": 60,
    "MEDIUM": 45,
    "HARD": 30,
    "EXPERT": 20
}

# Score multipliers
SCORE_MULTIPLIERS = {
    "EASY": 100,
    "MEDIUM": 150,
    "HARD": 200,
    "EXPERT": 300
}

SCORE_PENALTY_PER_ATTEMPT = {
    "EASY": 5,
    "MEDIUM": 10,
    "HARD": 20,
    "EXPERT": 40
}

# Emoji indicators
EMOJI = {
    "success": "✅",
    "error": "❌",
    "warning": "⚠️",
    "fire": "🔥",
    "trophy": "🏆",
    "medal": "🏅",
    "crown": "👑",
    "handshake": "🤝",
    "wave": "👋",
    "game": "🎮",
    "target": "🎯",
    "pin": "📌",
    "lightbulb": "💡",
    "timer": "⏱️",
    "clock": "⏰",
    "skull": "💀",
    "up": "📈",
    "down": "📉",
    "robot": "🤖",
    "party": "🎉",
    "fire_x2": "🔥" * 2,
    "party_x15": "🎉" * 15,
    "stats": "📊"
}
