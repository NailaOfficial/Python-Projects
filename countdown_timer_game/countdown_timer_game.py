import streamlit as st
import time
from datetime import datetime
import random

def main():
    st.set_page_config(
        page_title="⏱️ Countdown Timer Game",
        page_icon="⏱️",
        layout="centered"
    )
    
    st.title("⏱️ Countdown Timer Challenge")
    st.markdown("""
    ### 🎮 Game Rules:
    1. Timer will count down from a random time
    2. Try to stop it exactly at **00:00**
    3. The closer you get, the more points you earn!
    """)
    
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'high_score' not in st.session_state:
        st.session_state.high_score = 0
    if 'game_active' not in st.session_state:
        st.session_state.game_active = False
    if 'target_time' not in st.session_state:
        st.session_state.target_time = 0
    if 'start_time' not in st.session_state:
        st.session_state.start_time = 0
        
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Score", st.session_state.score)
    with col2:
        st.metric("High Score", st.session_state.high_score)
        
    if not st.session_state.game_active:
        if st.button("🎮 Start New Game"):
            st.session_state.target_time = random.randint(3, 10)
            st.session_state.start_time = time.time()
            st.session_state.game_active = True
            st.experimental_rerun()
            
    else:
        elapsed_time = time.time() - st.session_state.start_time
        remaining_time = max(st.session_state.target_time - elapsed_time, 0)
        
        progress = 1 - (remaining_time / st.session_state.target_time)
        st.progress(progress)
        
        st.markdown(f"### ⏳ Time Remaining: {remaining_time:.2f}s")
        
        if st.button("🛑 STOP!", type="primary"):
            accuracy = abs(remaining_time)
            points = max(100 - int(accuracy * 100), 0)
            st.session_state.score += points
            st.session_state.high_score = max(st.session_state.high_score, st.session_state.score)
            
            if accuracy < 0.1:
                st.balloons()
                st.success(f"🎯 Great timing! You earned {points} points!")
            elif accuracy < 0.5:
                st.success(f"👍 Good try! You earned {points} points!")
            else:
                st.warning(f"😅 Keep practicing! You earned {points} points!")
                
            st.session_state.game_active = False
            st.experimental_rerun()
            
        if st.button("🔄 Reset Game"):
            st.session_state.score = 0
            st.session_state.game_active = False
            st.experimental_rerun()

if __name__ == "__main__":
    main() 