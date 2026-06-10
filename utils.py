"""
Utility Functions for the Number Guessing Game
"""
from config import EMOJI, MAX_HINTS

def get_hint(secret_number: int, hints_used: int, max_range: int) -> str:
    """Generate a helpful hint based on attempts"""
    if hints_used >= MAX_HINTS:
        return f"{EMOJI['error']} No more hints available!"
    
    hints = [
        f"{EMOJI['lightbulb']} The number is {'even' if secret_number % 2 == 0 else 'odd'}",
        f"{EMOJI['lightbulb']} The number is {'less' if secret_number < (max_range / 2) else 'greater'} than {max_range // 2}",
        f"{EMOJI['lightbulb']} The sum of digits: {sum(int(d) for d in str(secret_number))}"
    ]
    return hints[hints_used]

def validate_guess(guess_str: str, min_range: int, max_range: int) -> tuple[bool, int | None]:
    """Validate and convert user input to integer guess"""
    try:
        guess = int(guess_str)
        if guess < min_range or guess > max_range:
            print(f"{EMOJI['warning']}  Enter a number between {min_range} and {max_range}")
            return False, None
        return True, guess
    except ValueError:
        print(f"{EMOJI['error']} Enter a valid number!")
        return False, None

def get_feedback(guess: int, secret: int) -> str:
    """Get feedback on the guess"""
    if guess < secret:
        return f"{EMOJI['up']} Too LOW!"
    elif guess > secret:
        return f"{EMOJI['down']} Too HIGH!"
    else:
        return f"{EMOJI['success']} CORRECT!"

def calculate_score(difficulty: str, attempts: int, multipliers: dict, penalties: dict) -> int:
    """Calculate score based on difficulty and attempts"""
    base = multipliers.get(difficulty, 100)
    penalty = penalties.get(difficulty, 5)
    return max(0, base - (attempts * penalty))

def display_header(title: str):
    """Display a formatted header"""
    print("\n" + "="*50)
    print(f"{EMOJI['game']} {title}".center(50))
    print("="*50)

def display_divider():
    """Display a divider line"""
    print("="*50)

def get_yes_no_input(prompt: str) -> bool:
    """Get yes/no response from user"""
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print(f"{EMOJI['error']} Please enter 'yes' or 'no'")

def format_attempts_display(current: int, total: int) -> str:
    """Format attempts display with remaining count"""
    remaining = total - current
    return f"{current}/{total} ({remaining} left)"

def get_difficulty_name(min_val: int, max_val: int) -> str:
    """Get difficulty name based on range"""
    if max_val == 50:
        return "EASY"
    elif max_val == 100:
        return "MEDIUM"
    elif max_val == 200:
        return "HARD"
    elif max_val == 1000:
        return "EXPERT"
    return "UNKNOWN"

def format_time_display(seconds: int) -> str:
    """Format time for display"""
    if seconds < 0:
        return "0s"
    return f"{seconds}s"

def print_success_message(message: str):
    """Print a success message"""
    print(f"{EMOJI['success']} {message}")

def print_error_message(message: str):
    """Print an error message"""
    print(f"{EMOJI['error']} {message}")

def print_info_message(message: str):
    """Print an info message"""
    print(f"{EMOJI['lightbulb']} {message}")
