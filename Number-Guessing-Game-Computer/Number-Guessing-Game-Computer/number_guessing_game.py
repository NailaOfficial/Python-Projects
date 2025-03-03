import streamlit as st
import random
import time

def initialize_session_state():
    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False
    if 'high_score' not in st.session_state:
        st.session_state.high_score = float('inf')

def reset_game():
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

def main():
    st.set_page_config(
        page_title="Number Guessing Game",
        page_icon="🎮",
        layout="centered"
    )
    
    initialize_session_state()
    
    st.title("🎮 Number Guessing Game")
    st.markdown("""
    ### Rules:
    - Computer has chosen a number between 1 and 100
    - Try to guess it in minimum attempts
    - After each guess, you'll get hints if the number is higher or lower
    """)
    
    # Game Interface
    if not st.session_state.game_over:
        guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
        
        if st.button("Submit Guess"):
            st.session_state.attempts += 1
            
            if guess == st.session_state.secret_number:
                st.balloons()
                st.success(f"🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts!")
                
                if st.session_state.attempts < st.session_state.high_score:
                    st.session_state.high_score = st.session_state.attempts
                    st.success("🏆 New High Score!")
                
                st.session_state.game_over = True
                
            elif guess < st.session_state.secret_number:
                st.warning("⬆️ Try a higher number!")
            else:
                st.warning("⬇️ Try a lower number!")
                
            st.info(f"Attempts so far: {st.session_state.attempts}")
    
    # Display high score
    if st.session_state.high_score != float('inf'):
        st.sidebar.success(f"🏆 Best Score: {st.session_state.high_score} attempts")
    
    # Reset game button
    if st.button("New Game"):
        reset_game()

if __name__ == "__main__":
    main() 