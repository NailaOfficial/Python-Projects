import streamlit as st
import random

def main():
    st.title("Rock Paper Scissors Game")
    st.write("Choose your move!")

    # Create buttons for user choice
    user_choice = st.radio("", ["Rock", "Paper", "Scissors"])
    
    # Add play button
    if st.button("Play"):
        # Computer's choice
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        
        # Show choices
        st.write(f"Your choice: {user_choice}")
        st.write(f"Computer's choice: {computer_choice}")
        
        # Determine winner
        if user_choice == computer_choice:
            st.write("It's a tie! 🤝")
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            st.write("You win! 🎉")
        else:
            st.write("Computer wins! 🤖")

if __name__ == "__main__":
    main() 