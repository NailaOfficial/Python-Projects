import streamlit as st
import random
import json
from pathlib import Path

# Word categories with hints
WORD_CATEGORIES = {
    "Animals": {
        "lion": "King of the jungle",
        "elephant": "Largest land mammal",
        "giraffe": "Longest neck",
    },
    "Fruits": {
        "mango": "King of fruits",
        "apple": "Keeps the doctor away",
        "banana": "Monkey's favorite",
    },
    "Countries": {
        "pakistan": "Land of the pure",
        "japan": "Land of rising sun",
        "egypt": "Home of pyramids",
    }
}

def initialize_game_state():
    if 'word' not in st.session_state:
        st.session_state.word = ""
        st.session_state.guessed_letters = set()
        st.session_state.attempts = 6
        st.session_state.score = 0
        st.session_state.hint_used = False

def get_display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def main():
    st.title("🎮 Unique Hangman Game")
    
    initialize_game_state()
    
    # Category selection
    category = st.selectbox("Choose a category:", list(WORD_CATEGORIES.keys()))
    
    if st.button("New Game") or not st.session_state.word:
        st.session_state.word = random.choice(list(WORD_CATEGORIES[category].keys()))
        st.session_state.guessed_letters = set()
        st.session_state.attempts = 6
        st.session_state.hint_used = False

    # Game display
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Game Status")
        st.write(f"Attempts left: {st.session_state.attempts}")
        st.write(f"Score: {st.session_state.score}")
        
        # Hint button
        if not st.session_state.hint_used:
            if st.button("Get Hint"):
                st.write(f"Hint: {WORD_CATEGORIES[category][st.session_state.word]}")
                st.session_state.hint_used = True
                st.session_state.attempts -= 1

    with col2:
        st.subheader("Word to Guess")
        display_word = get_display_word(st.session_state.word, st.session_state.guessed_letters)
        st.write(display_word)

    # Letter input
    letter = st.text_input("Enter a letter:", max_chars=1).lower()
    if letter and letter.isalpha():
        if letter not in st.session_state.guessed_letters:
            st.session_state.guessed_letters.add(letter)
            if letter not in st.session_state.word:
                st.session_state.attempts -= 1
        
    # Game over conditions
    if st.session_state.attempts <= 0:
        st.error(f"Game Over! The word was: {st.session_state.word}")
        if st.button("Play Again"):
            initialize_game_state()
    
    if all(letter in st.session_state.guessed_letters for letter in st.session_state.word):
        st.success("Congratulations! You won! 🎉")
        st.session_state.score += 10
        if st.button("Play Again"):
            initialize_game_state()

    # Display guessed letters
    st.write("Guessed letters:", ", ".join(sorted(st.session_state.guessed_letters)))

if __name__ == "__main__":
    main() 