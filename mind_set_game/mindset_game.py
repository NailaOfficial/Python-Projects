import streamlit as st
import random
import time
from PIL import Image
import numpy as np
import base64
from pygame import mixer
import streamlit.components.v1 as components

# Initialize pygame mixer for sounds
mixer.init()

def load_sounds():
    if 'sounds_loaded' not in st.session_state:
        # Comment out actual sound loading for web deployment
        st.session_state.sounds = {
            'button_0': None,
            'button_1': None,
            'button_2': None,
            'button_3': None,
            'success': None,
            'game_over': None
        }
        st.session_state.sounds_loaded = True

def add_animation_css():
    st.markdown("""
        <style>
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        
        @keyframes shake {
            0% { transform: translate(0, 0); }
            25% { transform: translate(-5px, 0); }
            75% { transform: translate(5px, 0); }
            100% { transform: translate(0, 0); }
        }
        
        .button-active {
            animation: pulse 0.5s ease-in-out;
        }
        
        .game-over {
            animation: shake 0.5s ease-in-out;
        }
        
        .success-flash {
            animation: success-flash 1s ease-in-out;
        }
        
        .stButton>button {
            width: 100%;
            height: 100px;
            margin: 5px;
            font-size: 24px;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 0 15px rgba(0,0,0,0.2);
        }
        
        .score-container {
            padding: 20px;
            border-radius: 10px;
            background: linear-gradient(45deg, #1e3799, #0c2461);
            color: white;
            text-align: center;
            margin: 10px 0;
        }
        </style>
    """, unsafe_allow_html=True)

def play_button_animation(button_id):
    js_code = f"""
        <script>
        const button = document.querySelector('[data-button-id="{button_id}"]');
        button.classList.add('button-active');
        setTimeout(() => button.classList.remove('button-active'), 500);
        </script>
    """
    components.html(js_code, height=0)

def initialize_session_state():
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'high_score' not in st.session_state:
        st.session_state.high_score = 0
    if 'game_active' not in st.session_state:
        st.session_state.game_active = False
    if 'sequence' not in st.session_state:
        st.session_state.sequence = []
    if 'user_sequence' not in st.session_state:
        st.session_state.user_sequence = []
    if 'level' not in st.session_state:
        st.session_state.level = 1
    if 'animation_state' not in st.session_state:
        st.session_state.animation_state = None

def create_game_board():
    st.title("🧠 Mind Set - Memory Game")
    st.markdown("""
    <div class="game-header">
        <h3>Rules:</h3>
        <ol>
            <li>Watch the sequence of highlighted boxes</li>
            <li>Repeat the sequence by clicking the boxes</li>
            <li>Each correct sequence increases your score</li>
            <li>Make a mistake and the game ends!</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="score-container">
                <h3>Current Score</h3>
                <h2>{}</h2>
            </div>
        """.format(st.session_state.score), unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="score-container">
                <h3>High Score</h3>
                <h2>{}</h2>
            </div>
        """.format(st.session_state.high_score), unsafe_allow_html=True)

def check_sequence(user_input):
    play_button_animation(user_input)
    # Remove sound playing
    # st.session_state.sounds[f'button_{user_input}'].play()
    
    if len(st.session_state.user_sequence) <= len(st.session_state.sequence):
        st.session_state.user_sequence.append(user_input)
        
        for i in range(len(st.session_state.user_sequence)):
            if st.session_state.user_sequence[i] != st.session_state.sequence[i]:
                # st.session_state.sounds['game_over'].play()
                game_over()
                return False
                
        if len(st.session_state.user_sequence) == len(st.session_state.sequence):
            # st.session_state.sounds['success'].play()
            st.session_state.score += 10
            st.session_state.level += 1
            if st.session_state.score > st.session_state.high_score:
                st.session_state.high_score = st.session_state.score
            st.session_state.user_sequence = []
            st.experimental_rerun()
            
    return True

def game_over():
    st.session_state.game_active = False
    st.markdown("""
        <div class="game-over">
            <h2>Game Over!</h2>
            <h3>Final Score: {}</h3>
        </div>
    """.format(st.session_state.score), unsafe_allow_html=True)
    if st.button("Play Again"):
        reset_game()
        st.experimental_rerun()

def reset_game():
    st.session_state.score = 0
    st.session_state.sequence = []
    st.session_state.user_sequence = []
    st.session_state.level = 1

def generate_sequence():
    sequence = st.session_state.sequence.copy()
    sequence.append(random.randint(0, 3))
    return sequence

def main():
    add_animation_css()
    load_sounds()
    initialize_session_state()
    create_game_board()

    if not st.session_state.game_active:
        if st.button("Start Game", key="start"):
            st.session_state.game_active = True
            reset_game()
            st.experimental_rerun()
    else:
        st.markdown(f"<h2 class='level-header'>Level {st.session_state.level}</h2>", unsafe_allow_html=True)
        
        # Create animated game grid
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔵", key="0", help="Blue Button"):
                check_sequence(0)
            if st.button("🔴", key="1", help="Red Button"):
                check_sequence(1)
        with col2:
            if st.button("🟡", key="2", help="Yellow Button"):
                check_sequence(2)
            if st.button("🟢", key="3", help="Green Button"):
                check_sequence(3)

        if len(st.session_state.sequence) == 0:
            st.session_state.sequence = generate_sequence()
            
        # Animated sequence display
        sequence_display = "<div class='sequence-display'><h3>Watch the sequence:</h3>"
        for i in st.session_state.sequence:
            if i == 0:
                sequence_display += "<span class='button-flash blue'>🔵</span> "
            elif i == 1:
                sequence_display += "<span class='button-flash red'>🔴</span> "
            elif i == 2:
                sequence_display += "<span class='button-flash yellow'>🟡</span> "
            else:
                sequence_display += "<span class='button-flash green'>🟢</span> "
        sequence_display += "</div>"
        st.markdown(sequence_display, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 