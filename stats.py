"""
Game Statistics Manager
"""
import json
import os
from datetime import datetime
from typing import Dict
from config import STATS_FILE, EMOJI

class GameStats:
    """Handles game statistics tracking and persistence"""
    
    def __init__(self, stats_file: str = STATS_FILE):
        self.stats_file = stats_file
        self.stats = self._load_stats()
    
    def _load_stats(self) -> Dict:
        """Load statistics from file or create default stats"""
        if os.path.exists(self.stats_file):
            try:
                with open(self.stats_file, 'r') as f:
                    return json.load(f)
            except:
                return self._default_stats()
        return self._default_stats()
    
    def _default_stats(self) -> Dict:
        """Create default statistics structure"""
        return {
            "games_played": 0,
            "games_won": 0,
            "total_attempts": 0,
            "best_attempt": float('inf'),
            "best_score": 0,
            "by_difficulty": {
                "EASY": {"wins": 0, "plays": 0},
                "MEDIUM": {"wins": 0, "plays": 0},
                "HARD": {"wins": 0, "plays": 0},
                "EXPERT": {"wins": 0, "plays": 0}
            },
            "by_mode": {
                "classic": {"wins": 0, "plays": 0},
                "survival": {"wins": 0, "plays": 0},
                "speed": {"wins": 0, "plays": 0},
                "multiplayer": {"wins": 0, "plays": 0},
                "reverse": {"wins": 0, "plays": 0},
                "endless": {"wins": 0, "plays": 0}
            },
            "last_played": None
        }
    
    def save_stats(self):
        """Save statistics to file"""
        with open(self.stats_file, 'w') as f:
            json.dump(self.stats, f, indent=2)
    
    def record_game(self, difficulty: str, mode: str, won: bool, attempts: int, score: int):
        """Record a game result"""
        self.stats["games_played"] += 1
        self.stats["total_attempts"] += attempts
        self.stats["last_played"] = datetime.now().isoformat()
        
        if won:
            self.stats["games_won"] += 1
            self.stats["best_attempt"] = min(self.stats["best_attempt"], attempts)
            self.stats["best_score"] = max(self.stats["best_score"], score)
            self.stats["by_difficulty"][difficulty]["wins"] += 1
            self.stats["by_mode"][mode]["wins"] += 1
        
        self.stats["by_difficulty"][difficulty]["plays"] += 1
        self.stats["by_mode"][mode]["plays"] += 1
        self.save_stats()
    
    def display_stats(self):
        """Display comprehensive game statistics"""
        print("\n" + "="*50)
        print(f"{EMOJI['stats']} YOUR GAME STATISTICS")
        print("="*50)
        
        if self.stats["games_played"] == 0:
            print("No games played yet! Start playing to build your stats.")
            return
        
        win_rate = (self.stats["games_won"] / self.stats["games_played"]) * 100
        avg_attempts = self.stats["total_attempts"] / self.stats["games_played"]
        
        print(f"Total Games: {self.stats['games_played']}")
        print(f"Games Won: {self.stats['games_won']} ({win_rate:.1f}%)")
        print(f"Best Attempt: {self.stats['best_attempt'] if self.stats['best_attempt'] != float('inf') else 'N/A'}")
        print(f"Best Score: {self.stats['best_score']}")
        print(f"Average Attempts: {avg_attempts:.1f}")
        
        print(f"\n{EMOJI['trophy']} By Difficulty:")
        for diff, data in self.stats["by_difficulty"].items():
            if data["plays"] > 0:
                win_rate = (data["wins"] / data["plays"]) * 100
                print(f"  {diff}: {data['wins']}/{data['plays']} ({win_rate:.0f}%)")
        
        print(f"\n{EMOJI['game']} By Game Mode:")
        for mode, data in self.stats["by_mode"].items():
            if data["plays"] > 0:
                win_rate = (data["wins"] / data["plays"]) * 100
                print(f"  {mode.upper()}: {data['wins']}/{data['plays']} ({win_rate:.0f}%)")
        
        print("="*50 + "\n")
    
    def get_best_difficulty(self) -> str:
        """Get the difficulty level with highest win rate"""
        best_diff = None
        best_rate = 0
        
        for diff, data in self.stats["by_difficulty"].items():
            if data["plays"] > 0:
                rate = data["wins"] / data["plays"]
                if rate > best_rate:
                    best_rate = rate
                    best_diff = diff
        
        return best_diff or "UNKNOWN"
    
    def get_best_mode(self) -> str:
        """Get the game mode with highest win rate"""
        best_mode = None
        best_rate = 0
        
        for mode, data in self.stats["by_mode"].items():
            if data["plays"] > 0:
                rate = data["wins"] / data["plays"]
                if rate > best_rate:
                    best_rate = rate
                    best_mode = mode
        
        return best_mode or "UNKNOWN"
