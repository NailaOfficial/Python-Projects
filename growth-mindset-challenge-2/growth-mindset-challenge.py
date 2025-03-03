import streamlit as st
import random

# Page Configurations
st.set_page_config(page_title="Growth Mindset Challenge", layout="centered")

# Daily Growth Mindset Challenges
challenges = [
    "Take 10 minutes to reflect on a past failure and what you learned from it.",
    "Write down 3 things you are grateful for today.",
    "Try something new that you’ve never done before.",
    "Step out of your comfort zone and talk to someone new.",
    "Learn a new skill or improve an existing one for at least 30 minutes today.",
    "Read an article or watch a video about someone who overcame great challenges.",
    "Write a positive affirmation and repeat it throughout the day.",
    "Spend 5 minutes visualizing your future success.",
    "Give someone a genuine compliment today.",
    "Challenge yourself to stay positive in a tough situation."
]

# Motivational Quotes
quotes = [
    "Your only limit is your mind.",
    "Growth is never by mere chance; it is the result of forces working together.",
    "Don't fear failure. Fear being in the exact same place next year as you are today.",
    "Success is not the key to happiness. Happiness is the key to success.",
    "Everything you’ve ever wanted is on the other side of fear.",
    "You don’t have to be great to start, but you have to start to be great."
]

# UI Design
st.title("🌱 Growth Mindset Challenge")
st.subheader("Embrace the Journey to Self-Improvement")
st.write("Every day is an opportunity to grow and push beyond your limits.")

# Generate a random challenge and quote
challenge = random.choice(challenges)
quote = random.choice(quotes)

# Display Challenge
st.markdown("### 🔥 Today's Growth Challenge")
st.info(challenge)

# Display Motivational Quote
st.markdown("### 💡 Today's Motivational Quote")
st.success(quote)

# User Progress Tracker
st.markdown("### 📅 Track Your Progress")
progress = st.text_area("Write about how you completed today's challenge and what you learned.")
if st.button("Save Progress"):
    st.success("Your progress has been saved! Keep growing!")

# Footer
st.markdown("---")
st.write("💡 Keep challenging yourself every day and see the transformation in your mindset!")
