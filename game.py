"""
Number Guessing Game - Main Entry Point
A unique number guessing game with multiple game modes, difficulty levels, and statistics tracking.
"""
import random
from config import Difficulty, GAME_MODES, EMOJI, SCORE_MULTIPLIERS, SCORE_PENALTY_PER_ATTEMPT
from stats import GameStats
from modes import ClassicMode, SurvivalMode, SpeedMode, MultiplayerMode, ReverseMode, EndlessMode
from utils import display_header, display_divider, get_yes_no_input

class NumberGuessingGame:
    """Main game controller"""
    
    def __init__(self):
        self.stats = GameStats()
        self.current_mode = None
        self.current_difficulty = None
    
    def display_menu(self):
        """Display main menu and get user choice"""
        display_header("WELCOME TO NUMBER GUESSING GAME")
        print("Choose Game Mode:")
        for key, (_, desc) in GAME_MODES.items():
            emoji_num = f"{key}️⃣" if key != "7" else "7️⃣"
            print(f"{emoji_num}  {desc}")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "7":
            self.stats.display_stats()
            return self.display_menu()
        elif choice not in ["1", "2", "3", "4", "5", "6"]:
            print(f"{EMOJI['error']} Invalid choice!")
            return self.display_menu()
        
        return GAME_MODES[choice][0]
    
    def select_difficulty(self) -> tuple:
        """Select difficulty level and return (min_range, max_range, max_attempts, difficulty_name)"""
        print("\nChoose Difficulty:")
        print("1️⃣  Easy   (1-50, 10 attempts)")
        print("2️⃣  Medium (1-100, 7 attempts)")
        print("3️⃣  Hard   (1-200, 5 attempts)")
        print("4️⃣  Expert (1-1000, 4 attempts)")
        
        diff_choice = input("\nEnter your choice (1-4): ").strip()
        
        diff_map = {
            "1": Difficulty.EASY,
            "2": Difficulty.MEDIUM,
            "3": Difficulty.HARD,
            "4": Difficulty.EXPERT
        }
        
        if diff_choice not in diff_map:
            print(f"{EMOJI['error']} Invalid choice!")
            return self.select_difficulty()
        
        difficulty = diff_map[diff_choice]
        min_range, max_range, max_attempts = difficulty.value
        self.current_difficulty = difficulty.name
        
        return min_range, max_range, max_attempts, difficulty.name
    
    def play_game(self, mode: str) -> bool:
        """Play the selected game mode"""
        
        # Multiplayer mode doesn't need difficulty selection (uses it for range)
        if mode == "multiplayer":
            min_range, max_range, max_attempts, difficulty_name = self.select_difficulty()
            game = MultiplayerMode()
            result = game.play(min_range, max_range, max_attempts, difficulty_name)
            self.stats.record_game(difficulty_name, mode, result, 0)
            return result
        
        # Reverse mode
        if mode == "reverse":
            min_range, max_range, max_attempts, difficulty_name = self.select_difficulty()
            game = ReverseMode(min_range, max_range, max_attempts, difficulty_name)
            result = game.play()
            self.stats.record_game(difficulty_name, mode, result, 0)
            return result
        
        # All other modes
        min_range, max_range, max_attempts, difficulty_name = self.select_difficulty()
        score = 0
        
        if mode == "classic":
            game = ClassicMode(min_range, max_range, max_attempts, difficulty_name)
            result = game.play()
            score = max(0, SCORE_MULTIPLIERS.get(difficulty_name, 100) - (game.attempts * SCORE_PENALTY_PER_ATTEMPT.get(difficulty_name, 5)))
        
        elif mode == "survival":
            game = SurvivalMode(min_range, max_range, max_attempts, difficulty_name)
            result = game.play()
            score = 500 if result else 0
        
        elif mode == "speed":
            game = SpeedMode(min_range, max_range, max_attempts, difficulty_name)
            result = game.play()
            score = max(0, SCORE_MULTIPLIERS.get(difficulty_name, 100) - (game.attempts * SCORE_PENALTY_PER_ATTEMPT.get(difficulty_name, 5)))
        
        elif mode == "endless":
            game = EndlessMode(min_range, max_range, max_attempts, difficulty_name)
            result = game.play()
            score = 0
        
        else:
            return False
        
        self.stats.record_game(difficulty_name, mode, result, score)
        return result
    
    def main_loop(self):
        """Main game loop"""
        while True:
            mode = self.display_menu()
            
            if mode:
                self.play_game(mode)
            
            play_again = input("\nPlay again? (yes/no): ").strip().lower()
            if play_again not in ['yes', 'y']:
                print(f"\n{EMOJI['wave']} Thanks for playing! See you next time!")
                
                # Show final stats
                best_diff = self.stats.get_best_difficulty()
                best_mode = self.stats.get_best_mode()
                
                if best_diff != "UNKNOWN":
                    print(f"\n{EMOJI['trophy']} Your Best Difficulty: {best_diff}")
                if best_mode != "UNKNOWN":
                    print(f"{EMOJI['game']} Your Favorite Mode: {best_mode.upper()}")
                
                break

def main():
    """Entry point"""
    game = NumberGuessingGame()
    game.main_loop()

if __name__ == "__main__":
    main()
