"""
Game Mode Implementations
"""
import time
from config import Difficulty, EMOJI, SPEED_TIME_LIMITS, SCORE_MULTIPLIERS, SCORE_PENALTY_PER_ATTEMPT
from utils import validate_guess, get_feedback, calculate_score, display_header
import random

class GameMode:
    """Base class for game modes"""
    
    def __init__(self, min_range: int, max_range: int, max_attempts: int, difficulty_name: str):
        self.min_range = min_range
        self.max_range = max_range
        self.max_attempts = max_attempts
        self.difficulty_name = difficulty_name
        self.secret_number = None
        self.attempts = 0
        self.hints_used = 0
        self.max_hints = 3
    
    def _generate_secret(self):
        """Generate a secret number"""
        self.secret_number = random.randint(self.min_range, self.max_range)
        self.attempts = 0
        self.hints_used = 0

class ClassicMode(GameMode):
    """Classic mode - Guess the number with feedback"""
    
    def play(self) -> bool:
        """Play classic mode"""
        self._generate_secret()
        
        print(f"\n{EMOJI['success']} Game started! Difficulty: {self.difficulty_name}")
        print(f"{EMOJI['target']} I'm thinking of a number between {self.min_range} and {self.max_range}")
        print(f"{EMOJI['pin']} You have {self.max_attempts} attempts and {self.max_hints} hints")
        print(f"{EMOJI['lightbulb']} Type 'hint' for a hint or 'quit' to exit\n")
        
        while self.attempts < self.max_attempts:
            remaining = self.max_attempts - self.attempts
            user_input = input(f"{EMOJI['pin']} Attempt {self.attempts + 1}/{self.max_attempts}: Guess the number: ").strip().lower()
            
            if user_input == 'quit':
                print(f"{EMOJI['error']} Game ended! The number was {self.secret_number}")
                return False
            
            if user_input == 'hint':
                from utils import get_hint
                print(get_hint(self.secret_number, self.hints_used, self.max_range))
                self.hints_used += 1
                continue
            
            is_valid, guess = validate_guess(user_input, self.min_range, self.max_range)
            if not is_valid:
                continue
            
            self.attempts += 1
            
            if guess == self.secret_number:
                return self.display_win()
            else:
                feedback = get_feedback(guess, self.secret_number)
                print(f"{feedback} ({remaining - 1} attempts left)\n")
        
        print(f"\n{EMOJI['skull']} Game Over! The number was {self.secret_number}")
        return False
    
    def display_win(self) -> bool:
        """Display win message"""
        score = calculate_score(self.difficulty_name, self.attempts, SCORE_MULTIPLIERS, SCORE_PENALTY_PER_ATTEMPT)
        print(f"\n{EMOJI['party_x15']}")
        print(f"{EMOJI['success']} CORRECT! The number was {self.secret_number}")
        print(f"Attempts: {self.attempts}/{self.max_attempts}")
        print(f"Score: {score} {EMOJI['fire']}")
        print(f"{EMOJI['party_x15']}\n")
        return True

class SurvivalMode(GameMode):
    """Survival mode - Win 5 consecutive rounds with increasing difficulty"""
    
    def play(self) -> bool:
        """Play survival mode"""
        rounds = 0
        consecutive_wins = 0
        target_wins = 5
        
        while consecutive_wins < target_wins:
            rounds += 1
            difficulty = min(rounds // 2 + 1, 4)
            
            diff_list = [Difficulty.EASY, Difficulty.MEDIUM, Difficulty.HARD, Difficulty.EXPERT]
            current_diff = diff_list[difficulty - 1]
            
            self.min_range, self.max_range, attempts_per_round = current_diff.value
            self._generate_secret()
            
            print(f"\n{EMOJI['trophy']} Round {rounds} - Difficulty: {current_diff.name} (Win streak: {consecutive_wins})")
            print(f"Guess a number between {self.min_range} and {self.max_range}")
            
            won_round = False
            
            while self.attempts < attempts_per_round:
                user_input = input(f"Guess: ").strip().lower()
                
                if user_input == 'quit':
                    print(f"Game ended with {consecutive_wins} consecutive wins!")
                    return consecutive_wins > 0
                
                is_valid, guess = validate_guess(user_input, self.min_range, self.max_range)
                if not is_valid:
                    continue
                
                self.attempts += 1
                
                if guess == self.secret_number:
                    print(f"{EMOJI['success']} Correct! You got it in {self.attempts} attempt(s)!")
                    consecutive_wins += 1
                    won_round = True
                    break
                else:
                    feedback = get_feedback(guess, self.secret_number)
                    print(feedback)
            
            if not won_round:
                print(f"{EMOJI['error']} Wrong! The number was {self.secret_number}")
                print(f"Game Over! You reached {consecutive_wins} wins!")
                return consecutive_wins > 0
        
        print(f"\n{EMOJI['medal']} Incredible! You won {consecutive_wins} consecutive rounds!")
        return True

class SpeedMode(GameMode):
    """Speed mode - Race against the clock"""
    
    def play(self) -> bool:
        """Play speed mode"""
        self._generate_secret()
        time_limit = SPEED_TIME_LIMITS.get(self.difficulty_name, 60)
        
        print(f"{EMOJI['timer']}  Time Limit: {time_limit} seconds!")
        start_time = time.time()
        
        while self.attempts < self.max_attempts:
            elapsed = int(time.time() - start_time)
            remaining_time = time_limit - elapsed
            
            if remaining_time <= 0:
                print(f"\n{EMOJI['clock']} TIME'S UP! The number was {self.secret_number}")
                return False
            
            remaining = self.max_attempts - self.attempts
            user_input = input(f"{EMOJI['timer']}  {remaining_time}s left | Attempt {self.attempts + 1}/{self.max_attempts}: ").strip().lower()
            
            if user_input == 'quit':
                print(f"{EMOJI['error']} Game ended! The number was {self.secret_number}")
                return False
            
            is_valid, guess = validate_guess(user_input, self.min_range, self.max_range)
            if not is_valid:
                continue
            
            self.attempts += 1
            
            if guess == self.secret_number:
                score = calculate_score(self.difficulty_name, self.attempts, SCORE_MULTIPLIERS, SCORE_PENALTY_PER_ATTEMPT)
                print(f"\n{EMOJI['success']} CORRECT! Time remaining: {remaining_time}s")
                print(f"Score: {score} {EMOJI['fire']}\n")
                return True
            else:
                feedback = get_feedback(guess, self.secret_number)
                print(feedback)
        
        print(f"\n{EMOJI['skull']} Game Over! The number was {self.secret_number}")
        return False

class MultiplayerMode:
    """Multiplayer mode - 2 players compete"""
    
    def play(self, min_range: int, max_range: int, max_attempts: int, difficulty_name: str) -> bool:
        """Play multiplayer mode"""
        display_header("MULTIPLAYER MODE")
        print("Player 1 and Player 2 take turns guessing!")
        print("="*50)
        
        players = ["Player 1", "Player 2"]
        scores = [0, 0]
        rounds = 3
        
        for round_num in range(1, rounds + 1):
            secret_number = random.randint(min_range, max_range)
            attempts = 0
            
            print(f"\n{EMOJI['trophy']} Round {round_num}/{rounds}")
            print(f"Number range: {min_range}-{max_range}")
            
            current_player = 0
            round_won = False
            
            while attempts < max_attempts and not round_won:
                player_name = players[current_player]
                
                user_input = input(f"\n{player_name}'s turn (Attempt {attempts + 1}/{max_attempts}): ").strip().lower()
                
                if user_input == 'quit':
                    print("Game ended!")
                    return False
                
                is_valid, guess = validate_guess(user_input, min_range, max_range)
                if not is_valid:
                    continue
                
                attempts += 1
                
                if guess == secret_number:
                    print(f"{EMOJI['success']} {player_name} WINS! Got it in {attempts} attempts!")
                    scores[current_player] += (max_attempts - attempts + 1)
                    round_won = True
                else:
                    feedback = get_feedback(guess, secret_number)
                    print(feedback)
                
                current_player = 1 - current_player
            
            if not round_won:
                print(f"{EMOJI['error']} Neither player guessed it! (Number was {secret_number})")
        
        print(f"\n{EMOJI['trophy']} FINAL SCORES {EMOJI['trophy']}")
        print(f"Player 1: {scores[0]}")
        print(f"Player 2: {scores[1]}")
        
        if scores[0] > scores[1]:
            print(f"{EMOJI['crown']} Player 1 WINS!")
        elif scores[1] > scores[0]:
            print(f"{EMOJI['crown']} Player 2 WINS!")
        else:
            print(f"{EMOJI['handshake']} It's a TIE!")
        
        return True

class ReverseMode(GameMode):
    """Reverse mode - AI tries to guess your number"""
    
    def play(self) -> bool:
        """Play reverse mode"""
        display_header("REVERSE MODE")
        print("Think of a number and the AI will try to guess it!")
        print(f"Range: {self.min_range} to {self.max_range}")
        print("Respond with: 'higher' (h), 'lower' (l), or 'correct' (c)")
        print("="*50)
        
        low = self.min_range
        high = self.max_range
        ai_attempts = 0
        
        while ai_attempts < self.max_attempts:
            ai_attempts += 1
            guess = (low + high) // 2
            
            print(f"\n{EMOJI['robot']} AI Guess #{ai_attempts}: {guess}")
            response = input("Is it higher, lower, or correct? ").strip().lower()
            
            if response in ['correct', 'c']:
                print(f"{EMOJI['party_x15']}")
                print(f"{EMOJI['success']} AI got your number in {ai_attempts} attempts!")
                print(f"The AI used binary search strategy!")
                print(f"{EMOJI['party_x15']}\n")
                return True
            elif response in ['higher', 'h']:
                low = guess + 1
                remaining = high - low + 1
                print(f"{EMOJI['up']} (Range narrowed to {low}-{high}, ~{remaining} numbers left)")
            elif response in ['lower', 'l']:
                high = guess - 1
                remaining = high - low + 1
                print(f"{EMOJI['down']} (Range narrowed to {low}-{high}, ~{remaining} numbers left)")
            else:
                print(f"{EMOJI['warning']}  Please say 'higher', 'lower', or 'correct'")
                ai_attempts -= 1
                continue
            
            if low > high:
                print(f"\n{EMOJI['error']} Invalid sequence detected!")
                print("You may have given contradictory hints.")
                return False
        
        print(f"\n{EMOJI['error']} AI couldn't guess after {self.max_attempts} attempts!")
        print("The AI was defeated!")
        return False

class EndlessMode(GameMode):
    """Endless mode - Keep building streak until failure"""
    
    def play(self) -> bool:
        """Play endless mode"""
        display_header("ENDLESS MODE")
        print("Keep guessing consecutive numbers correctly!")
        print("Your streak ends when you fail.")
        print("="*50)
        
        streak = 0
        total_score = 0
        
        while True:
            streak += 1
            difficulty = min(streak // 3 + 1, 4)
            
            diff_list = [Difficulty.EASY, Difficulty.MEDIUM, Difficulty.HARD, Difficulty.EXPERT]
            current_diff = diff_list[difficulty - 1]
            
            self.min_range, self.max_range, _ = current_diff.value
            self._generate_secret()
            
            print(f"\n{EMOJI['fire']} Streak #{streak} | Difficulty: {current_diff.name}")
            print(f"Guess a number between {self.min_range} and {self.max_range}")
            
            for attempt in range(1, 5):
                user_input = input(f"Guess {attempt}/4: ").strip().lower()
                
                if user_input == 'quit':
                    print(f"\n🏁 Game Over! Streak: {streak - 1}")
                    return streak > 1
                
                is_valid, guess = validate_guess(user_input, self.min_range, self.max_range)
                if not is_valid:
                    continue
                
                self.attempts += 1
                
                if guess == self.secret_number:
                    score = max(0, 50 - (attempt - 1) * 10)
                    total_score += score
                    print(f"{EMOJI['success']} Correct! +{score} points")
                    break
                else:
                    feedback = get_feedback(guess, self.secret_number)
                    print(feedback)
            else:
                print(f"{EMOJI['error']} Wrong! The number was {self.secret_number}")
                print(f"\n🏁 Your Streak: {streak - 1}")
                print(f"Total Score: {total_score} {EMOJI['fire']}")
                return streak > 1
