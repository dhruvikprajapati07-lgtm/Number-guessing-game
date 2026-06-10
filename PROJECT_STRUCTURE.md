# Project Structure

```
Number guessing game/
├── game.py              # Main entry point
├── config.py            # Game configuration and constants
├── stats.py             # Statistics management
├── utils.py             # Utility functions
├── modes.py             # All game mode implementations
├── __init__.py          # Package init
├── README.md            # Documentation
└── game_stats.json      # Auto-generated statistics file
```

## File Descriptions

- **game.py**: Main game controller with menu system and game loop
- **config.py**: Difficulty levels, game modes, constants, and emoji definitions
- **stats.py**: GameStats class for tracking and saving game statistics
- **utils.py**: Helper functions for hints, validation, scoring, and display formatting
- **modes.py**: All 6 game mode implementations (Classic, Survival, Speed, Multiplayer, Reverse, Endless)
- **__init__.py**: Makes the directory a Python package (empty)

## Benefits of Separated Structure

✅ **Modularity**: Each file has a single responsibility
✅ **Maintainability**: Easy to update specific game modes or configuration
✅ **Readability**: Clear separation of concerns
✅ **Reusability**: Modules can be imported and used independently
✅ **Testing**: Easier to unit test individual components
✅ **Scalability**: Simple to add new game modes or features
