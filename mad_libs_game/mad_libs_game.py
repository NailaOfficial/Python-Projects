import streamlit as st
import random

def main():
    st.set_page_config(
        page_title="Mad Libs Game",
        page_icon="📝",
        layout="centered"
    )

    st.title("🎮 Mad Libs Story Generator")
    st.markdown("### Create your own funny story!")

    # Different story templates
    stories = {
        "Adventure": {
            "template": "Once upon a time, a {adj1} {noun1} decided to go on an adventure. They packed their {adj2} {noun2} and headed to the {adj3} {noun3}. Along the way, they met a {adj4} {noun4} who was {verb1} very {adverb1}.",
            "inputs": ["adjective", "noun", "adjective", "noun", "adjective", "noun", "adjective", "noun", "verb", "adverb"]
        },
        "Space Journey": {
            "template": "In the year 3000, a {adj1} {noun1} discovered a {adj2} {noun2} floating in space. The {noun1} decided to {verb1} {adverb1} towards the mysterious {noun3}.",
            "inputs": ["adjective", "noun", "adjective", "noun", "verb", "adverb", "noun"]
        }
    }

    # Story selection
    selected_story = st.selectbox("Choose your story theme:", list(stories.keys()))
    
    # Initialize user inputs dictionary
    user_inputs = {}
    
    # Create input fields based on selected story
    st.markdown("### Enter your words:")
    cols = st.columns(2)
    for i, input_type in enumerate(stories[selected_story]["inputs"]):
        with cols[i % 2]:
            key = f"{input_type}_{i}"
            user_inputs[key] = st.text_input(f"Enter a {input_type}:", key=key)

    # Generate story button
    if st.button("Generate Story! 🎲", type="primary"):
        if all(user_inputs.values()):  # Check if all inputs are filled
            # Create the story
            story = stories[selected_story]["template"]
            
            # Replace placeholders with user inputs
            for i, (key, value) in enumerate(user_inputs.items()):
                placeholder = "{" + f"{key.split('_')[0]}{i//2 + 1}" + "}"
                story = story.replace(placeholder, value)

            # Display the story in a nice box
            st.markdown("### Your Story:")
            st.success(story)
            
            # Add some fun animations/effects
            st.balloons()
        else:
            st.error("Please fill in all the words to generate your story!")

    # Add footer
    st.markdown("---")
    st.markdown("Made with ❤️ using Streamlit")

if __name__ == "__main__":
    main() 