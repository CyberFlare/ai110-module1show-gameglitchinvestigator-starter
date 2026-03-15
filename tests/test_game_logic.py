from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# BUG FIX TESTS

# Bug: invalid guesses were recorded in history
# Fix: parse_guess returns ok=False so the app skips adding them to history
def test_parse_guess_empty_string_not_ok():
    ok, value, _ = parse_guess("")
    assert ok == False
    assert value is None

def test_parse_guess_none_not_ok():
    ok, value, _ = parse_guess(None)
    assert ok == False
    assert value is None

def test_parse_guess_non_number_not_ok():
    ok, value, _ = parse_guess("abc")
    assert ok == False
    assert value is None

def test_parse_guess_valid_returns_int():
    ok, value, err = parse_guess("42")
    assert ok == True
    assert value == 42
    assert err is None

