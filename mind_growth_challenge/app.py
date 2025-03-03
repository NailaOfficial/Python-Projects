import streamlit as st
import random
from words import word_list
import string

def get_word():
    return random.choice(word_list).upper()

def initialize_game_state():
    if 'word' not in st.session_state:
        st.session_state.word = get_word()
        st.session_state.guessed_letters = set()
        st.session_state.tries = 6
        st.session_state.score = 0

def display_hangman(tries):
    stages = [  # Final state: head, body, both arms, both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |      
           |      
           |      
           -
        """,
        """
           --------
           |      |
           |      
           |      
           |      
           |      
           -
        """
    ]
    # Make sure tries is within valid range
    index = max(0, min(6, 6 - tries))
    return stages[index]

def main():
    st.title("🎮 Unique Hangman Game")
    st.write("Can you guess the word before the hangman is complete? 🤔")
    
    initialize_game_state()
    
    # Game Info
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Tries Left", st.session_state.tries)
    with col2:
        st.metric("Score", st.session_state.score)
    with col3:
        if st.button("New Game"):
            st.session_state.word = get_word()
            st.session_state.guessed_letters = set()
            st.session_state.tries = 6
            st.rerun()
    
    # Display word
    word_display = ""
    for letter in st.session_state.word:
        if letter in st.session_state.guessed_letters:
            word_display += letter + " "
        else:
            word_display += "_ "
    
    st.write("\n")
    st.markdown(f"<h1 style='text-align: center;'>{word_display}</h1>", unsafe_allow_html=True)
    
    # Display hangman
    st.text(display_hangman(st.session_state.tries))
    
    # Letter input
    col1, col2 = st.columns([3, 1])
    with col1:
        # Create buttons for each letter
        for i, letter in enumerate(string.ascii_uppercase):
            if i % 7 == 0:
                cols = st.columns(7)
            disabled = letter in st.session_state.guessed_letters
            if cols[i % 7].button(letter, disabled=disabled, key=letter):
                if letter not in st.session_state.word:
                    st.session_state.tries -= 1
                st.session_state.guessed_letters.add(letter)
                
                # Check win condition
                if all(letter in st.session_state.guessed_letters for letter in st.session_state.word):
                    st.session_state.score += 1
                    st.success("🎉 Congratulations! You won! The word was: " + st.session_state.word)
                    st.balloons()
                
                # Check lose condition
                if st.session_state.tries < 0:  # Changed from <= 0 to < 0
                    st.session_state.tries = 0  # Ensure tries doesn't go below 0
                    st.error("😢 Game Over! The word was: " + st.session_state.word)
                
                st.rerun()

if __name__ == "__main__":
    main() 