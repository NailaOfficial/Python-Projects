import streamlit as st
import random
import string
import pyperclip
from datetime import datetime
import json

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True, use_uppercase=True):
    characters = ''
    if use_letters:
        characters += string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        return "Please select at least one character type!"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password, website):
    try:
        with open('password_history.json', 'r') as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []
    
    history.append({
        'website': website,
        'password': password,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
    with open('password_history.json', 'w') as f:
        json.dump(history, f)

def main():
    st.set_page_config(page_title="Enhanced Password Generator", page_icon="🔐")
    
    st.title("🔐 Enhanced Password Generator")
    st.markdown("### Generate strong and secure passwords!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        password_length = st.slider("Password Length", 8, 32, 12)
        use_letters = st.checkbox("Include Letters", value=True)
        use_uppercase = st.checkbox("Include Uppercase", value=True)
    
    with col2:
        use_numbers = st.checkbox("Include Numbers", value=True)
        use_symbols = st.checkbox("Include Symbols", value=True)
        website = st.text_input("Website/App Name (Optional)")
    
    if st.button("Generate Password", type="primary"):
        password = generate_password(
            password_length,
            use_letters,
            use_numbers,
            use_symbols,
            use_uppercase
        )
        
        st.success("Generated Password:")
        st.code(password)
        
        col3, col4 = st.columns(2)
        
        with col3:
            if st.button("Copy to Clipboard"):
                pyperclip.copy(password)
                st.toast("Password copied to clipboard!")
        
        with col4:
            if website and st.button("Save Password"):
                save_password(password, website)
                st.toast("Password saved successfully!")
    
    # Password History Section
    st.markdown("---")
    st.subheader("Password History")
    try:
        with open('password_history.json', 'r') as f:
            history = json.load(f)
            if history:
                for entry in history[-5:]:  # Show last 5 entries
                    with st.expander(f"{entry['website']} - {entry['timestamp']}"):
                        st.code(entry['password'])
            else:
                st.info("No password history available")
    except FileNotFoundError:
        st.info("No password history available")

    # Password Strength Tips
    st.markdown("---")
    st.subheader("Password Security Tips")
    st.markdown("""
    - Use a minimum of 12 characters
    - Mix uppercase and lowercase letters
    - Include numbers and special characters
    - Avoid using personal information
    - Use unique passwords for each account
    """)

if __name__ == "__main__":
    main() 