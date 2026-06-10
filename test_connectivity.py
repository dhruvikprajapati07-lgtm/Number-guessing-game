#!/usr/bin/env python3
"""
Connectivity Test - Verify all modules are properly connected
"""

def test_imports():
    """Test that all imports work"""
    print("=" * 60)
    print("CONNECTIVITY TEST - Verifying all modules")
    print("=" * 60)
    
    tests_passed = 0
    tests_failed = 0
    
    # Test config imports
    try:
        from config import Difficulty, GAME_MODES, EMOJI, SCORE_MULTIPLIERS
        from config import SCORE_PENALTY_PER_ATTEMPT, STATS_FILE, MAX_HINTS, SPEED_TIME_LIMITS
        print("✅ config.py - All exports OK")
        tests_passed += 1
    except Exception as e:
        print(f"❌ config.py - FAILED: {e}")
        tests_failed += 1
    
    # Test utils imports
    try:
        from utils import display_header, display_divider, get_yes_no_input
        from utils import get_hint, validate_guess, get_feedback, calculate_score
        print("✅ utils.py - All exports OK")
        tests_passed += 1
    except Exception as e:
        print(f"❌ utils.py - FAILED: {e}")
        tests_failed += 1
    
    # Test stats imports
    try:
        from stats import GameStats
        print("✅ stats.py - All exports OK")
        tests_passed += 1
    except Exception as e:
        print(f"❌ stats.py - FAILED: {e}")
        tests_failed += 1
    
    # Test modes imports
    try:
        from modes import ClassicMode, SurvivalMode, SpeedMode
        from modes import MultiplayerMode, ReverseMode, EndlessMode
        print("✅ modes.py - All exports OK")
        tests_passed += 1
    except Exception as e:
        print(f"❌ modes.py - FAILED: {e}")
        tests_failed += 1
    
    # Test game imports
    try:
        from game import NumberGuessingGame, main
        print("✅ game.py - All exports OK")
        tests_passed += 1
    except Exception as e:
        print(f"❌ game.py - FAILED: {e}")
        tests_failed += 1
    
    # Test __init__.py imports
    try:
        from __init__ import NumberGuessingGame as NGG, main as main_func
        print("✅ __init__.py - All exports OK")
        tests_passed += 1
    except Exception as e:
        print(f"❌ __init__.py - FAILED: {e}")
        tests_failed += 1
    
    print("\n" + "=" * 60)
    print("INSTANTIATION TEST - Verify object creation")
    print("=" * 60)
    
    # Test GameStats instantiation
    try:
        from stats import GameStats
        stats = GameStats()
        assert stats.stats is not None
        assert 'games_played' in stats.stats
        print("✅ GameStats - Instantiation OK")
        tests_passed += 1
    except Exception as e:
        print(f"❌ GameStats - FAILED: {e}")
        tests_failed += 1
    
    # Test game instantiation
    try:
        from game import NumberGuessingGame
        game = NumberGuessingGame()
        assert game.stats is not None
        assert game.current_mode is None
        print("✅ NumberGuessingGame - Instantiation OK")
        tests_passed += 1
    except Exception as e:
        print(f"❌ NumberGuessingGame - FAILED: {e}")
        tests_failed += 1
    
    # Test ClassicMode instantiation
    try:
        from modes import ClassicMode
        mode = ClassicMode(1, 50, 10, "EASY")
        assert mode.min_range == 1
        assert mode.max_range == 50
        assert mode.max_attempts == 10
        print("✅ ClassicMode - Instantiation OK")
        tests_passed += 1
    except Exception as e:
        print(f"❌ ClassicMode - FAILED: {e}")
        tests_failed += 1
    
    print("\n" + "=" * 60)
    print("DEPENDENCY GRAPH")
    print("=" * 60)
    print("""
    config.py (No dependencies)
        ↓
    ├── utils.py (imports: config)
    ├── stats.py (imports: config)
    └── modes.py (imports: config, utils)
        ↓
    game.py (imports: config, stats, modes, utils)
        ↓
    __init__.py (imports: game)
    """)
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {tests_passed} passed, {tests_failed} failed")
    print("=" * 60)
    
    if tests_failed == 0:
        print("\n✅ ALL TESTS PASSED - Files are properly connected!")
        return True
    else:
        print(f"\n❌ {tests_failed} TEST(S) FAILED - Please fix the errors above")
        return False

if __name__ == "__main__":
    success = test_imports()
    exit(0 if success else 1)
