# 🎮 Number Guessing Game - Python Edition

A unique, feature-rich number guessing game with multiple modes, difficulty levels, hints system, and statistics tracking. Built with clean, modular Python code.

## 🌟 Features

### 6 Unique Game Modes
1. **Classic Mode** - Traditional number guessing with feedback
2. **Survival Mode** - Win 5 consecutive rounds at increasing difficulty
3. **Speed Mode** - Race against the clock to guess faster
4. **Multiplayer Mode** - 2 players compete in 3 rounds
5. **Reverse Mode** - AI uses binary search to guess YOUR number
6. **Endless Mode** - Build the longest streak possible

### 4 Difficulty Levels
- 🟢 **Easy**: 1-50, 10 attempts
- 🟡 **Medium**: 1-100, 7 attempts  
- 🔴 **Hard**: 1-200, 5 attempts
- 🔥 **Expert**: 1-1000, 4 attempts

### Advanced Features
✅ **Smart Hint System** (3 hints per game)
- Odd/Even indicator
- Range hints
- Digit sum information

✅ **Dynamic Scoring** - Points based on difficulty and speed
✅ **Persistent Statistics** - Auto-saved game history and performance metrics
✅ **Beautiful UI** - Emoji indicators and clear feedback
✅ **Modular Code** - 5 separate Python files for clean architecture

## 🚀 Quick Start

```bash
python game.py
```

## 📂 Project Structure

```
├── game.py              # Main entry point
├── config.py            # Configuration & constants
├── stats.py             # Statistics management
├── utils.py             # Helper functions
├── modes.py             # Game mode implementations
├── __init__.py          # Package initialization
└── README.md            # This file
```

See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for more details.

## 📖 How to Play

**Basic Workflow:**
1. Choose a game mode from the menu
2. Select your difficulty level
3. Follow the mode-specific rules
4. Try to get the highest score!

**Mode Descriptions:**

**Classic Mode** - The traditional guessing game
- Guess the number before attempts run out
- Get "Too HIGH" or "Too LOW" feedback
- Use hints strategically (max 3 per game)

**Survival Mode** - Progressive challenge
- Win 5 consecutive rounds
- Difficulty increases after every 2 wins
- No hints in this mode

**Speed Mode** - Against the clock
- Time limits: Easy (60s) → Expert (20s)
- Faster wins = bonus points
- Beat the clock to win

**Multiplayer Mode** - Head-to-head competition
- 2 players take turns guessing
- 3 rounds per match
- Highest points wins

**Reverse Mode** - Outsmart the AI
- You think of a number
- AI uses binary search to guess
- Try to stump the algorithm

**Endless Mode** - Never-ending streak
- Each correct guess increases difficulty
- Difficulty caps at Expert
- One wrong guess ends your run

## 💡 Special Commands

While playing, you can type:
- `hint` - Use one of your hint tokens
- `quit` - Exit the current game

## 📊 Statistics

From the main menu, select option 7 to view:
- Total games played
- Win rate percentage
- Best attempt record
- Best score achieved
- Performance by difficulty level
- Performance by game mode

## 🏆 Achievement Ideas

- **Speed Racer**: Win Speed Mode on Expert with 10+ seconds left
- **Perfect Survivor**: Win Survival Mode with all 5 rounds
- **Multiplayer Champion**: Win all 3 rounds against a friend
- **AI Defeated**: Stump the AI in Reverse Mode
- **Endless Legend**: Build a 10+ streak in Endless Mode
- **Expert Master**: Win 5+ games on Expert difficulty

## 🎯 Game Strategy Tips

1. **Classic Mode** - Save hints for when the range narrows significantly
2. **Survival Mode** - Play conservatively; one loss ends everything
3. **Speed Mode** - Make educated guesses to save time
4. **Multiplayer** - Learn your opponent's strategy
5. **Reverse Mode** - Give consistent feedback to confuse or challenge the AI
6. **Endless Mode** - Balance speed with accuracy

## 📋 Requirements

- Python 3.7+
- No external dependencies required

## 🎨 Customization

Edit `config.py` to:
- Change difficulty ranges and attempt counts
- Modify score multipliers
- Add new emoji indicators
- Adjust time limits for Speed Mode

## 📝 File Descriptions

- **game.py**: Main game controller with menu system and game loop
- **config.py**: Difficulty levels, game modes, constants, and emojis
- **stats.py**: GameStats class for tracking and persistence
- **utils.py**: Helper functions for validation, hints, and formatting
- **modes.py**: All 6 game mode implementations

## 🤝 Architecture Benefits

- **Modular**: Each component has a single responsibility
- **Maintainable**: Easy to update specific modes or settings
- **Testable**: Individual functions can be unit tested
- **Scalable**: Simple to add new modes or features
- **Readable**: Clear separation of concerns

## 💾 Save Data

Game statistics are automatically saved to `game_stats.json`. This file contains:
- Total games and wins
- Performance by difficulty
- Performance by game mode
- Personal best records
- Last played timestamp

Simply delete this file to reset all statistics.

## 🎮 Enjoy the Game!

Have fun playing all 6 unique modes and try to beat your personal best! 🎉
