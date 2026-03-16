import random
import streamlit as st
from logic_utils import check_guess, parse_guess

def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100




def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * (attempt_number-1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High" or outcome == "Too Low":
        return current_score - 5

    return current_score

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

# FIX: reset game state when difficulty changes with Claude Code
if "secret" not in st.session_state or st.session_state.get("difficulty") != difficulty:
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.history_results = []
    st.session_state.difficulty = difficulty

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

if "history_results" not in st.session_state:
    st.session_state.history_results = []

st.subheader("Make a guess")

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.history = []
    st.session_state.history_results = []
    st.session_state.status = "playing"
    st.session_state.score = 0
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.balloons()
        st.success(
            f"You won! The secret was {st.session_state.secret}. "
            f"Final score: {st.session_state.score}"
        )
    else:
        st.error(
            f"Out of attempts! The secret was {st.session_state.secret}. "
            f"Score: {st.session_state.score}"
        )
    if st.session_state.history:
        st.subheader("Guess History")
        rows = [
            {"#": i + 1, "Guess": g, "Result": r}
            for i, (g, r) in enumerate(zip(st.session_state.history, st.session_state.history_results))
        ]
        st.table(rows)
    st.stop()

if submit:
    

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        # FIX: invalid guesses no longer recorded in history with Claude Code
        st.error(err)
    elif guess_int < low or guess_int > high:
        # FIX: out-of-range guesses rejected and don't count as attempts with Claude Code
        st.error(f"Please enter a number between {low} and {high}.")
    else:
        st.session_state.attempts += 1
        st.session_state.history.append(guess_int)

        secret = st.session_state.secret

        outcome, message = check_guess(guess_int, secret)
        st.session_state.history_results.append(outcome)

        distance = abs(guess_int - secret)
        range_size = high - low
        pct = distance / range_size if range_size > 0 else 1
        if distance <= 2:
            proximity = "🔥 Burning hot!"
        elif pct < 0.10:
            proximity = "♨️ Getting warm"
        elif pct < 0.25:
            proximity = "🌡️ Lukewarm"
        elif pct < 0.50:
            proximity = "❄️ Cold"
        else:
            proximity = "🧊 Freezing!"

        # FIX: store hint in session state so it persists through st.rerun() with Claude Code
        st.session_state.last_hint = message if show_hint else None
        st.session_state.last_proximity = proximity if show_hint and outcome != "Win" else None

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.session_state.status = "won"
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
        # FIX: rerun immediately so history updates without waiting for next guess with Claude Code
        st.rerun()

if st.session_state.get("last_hint"):
    st.warning(st.session_state.last_hint)
if st.session_state.get("last_proximity"):
    st.info(st.session_state.last_proximity)

if st.session_state.history:
    st.subheader("Guess History")
    rows = [
        {"#": i + 1, "Guess": g, "Result": r}
        for i, (g, r) in enumerate(zip(st.session_state.history, st.session_state.history_results))
    ]
    st.table(rows)

st.divider()

st.caption("Built by an AI that claims this code is production-ready.")
