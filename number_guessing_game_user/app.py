import streamlit as st
import random
import time

# Page configuration
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎲",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
    }
    .success-text {
        color: #28a745;
        font-size: 20px;
    }
    .failure-text {
        color: #dc3545;
        font-size: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize game state
if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'high_score' not in st.session_state:
    st.session_state.high_score = float('inf')

# Title and description
st.title("🎮 Number Guessing Game")
st.markdown("### Can you guess the number between 1 and 100?")

# Game difficulty
difficulty = st.select_slider(
    "Select Difficulty",
    options=["Easy", "Medium", "Hard"],
    value="Medium"
)

max_attempts = {"Easy": 10, "Medium": 7, "Hard": 5}[difficulty]

# Input for guess
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Submit button
if st.button("Submit Guess"):
    st.session_state.attempts += 1
    
    if guess == st.session_state.random_number:
        st.balloons()
        st.markdown(f'<p class="success-text">🎉 Congratulations! You found the number in {st.session_state.attempts} attempts!</p>', unsafe_allow_html=True)
        if st.session_state.attempts < st.session_state.high_score:
            st.session_state.high_score = st.session_state.attempts
            st.success("New High Score! 🏆")
        st.session_state.game_over = True
        
    elif st.session_state.attempts >= max_attempts:
        st.markdown(f'<p class="failure-text">Game Over! The number was {st.session_state.random_number}</p>', unsafe_allow_html=True)
        st.session_state.game_over = True
        
    else:
        if guess < st.session_state.random_number:
            st.warning(f"Try a higher number! Attempts left: {max_attempts - st.session_state.attempts}")
        else:
            st.warning(f"Try a lower number! Attempts left: {max_attempts - st.session_state.attempts}")

# Display high score
if st.session_state.high_score != float('inf'):
    st.sidebar.markdown(f"### 🏆 High Score: {st.session_state.high_score} attempts")

# Reset game button
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.random_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.experimental_rerun()

# Game statistics in sidebar
st.sidebar.markdown("### 📊 Game Statistics")
st.sidebar.markdown(f"Current Attempts: {st.session_state.attempts}")
st.sidebar.markdown(f"Maximum Attempts: {max_attempts}")
st.sidebar.markdown(f"Difficulty: {difficulty}")

# Instructions in sidebar
st.sidebar.markdown("""
### 📝 How to Play
1. Choose your difficulty level
2. Enter a number between 1 and 100
3. Click 'Submit Guess'
4. Follow the hints to find the number
5. Try to beat your high score!
""") 