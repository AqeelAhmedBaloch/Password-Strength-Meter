import streamlit as st
import random
import string
import html

# Page configuration
st.set_page_config(
    page_title="Password Generator",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Add CSS styles directly
st.markdown("""
<style>
    .stButton > button {
        width: 100%;
        background-color: #1e88e5;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-size: 1.1em;
    }
    .stButton > button:hover {
        background-color: #1976d2;
        border-color: #1976d2;
    }
    .password-display {
        margin: 2rem 0;
        padding: 1rem;
        border-radius: 5px;
        background-color: #f0f2f6;
    }
    .info-msg {
        text-align: center;
        margin: 1rem 0;
    }
    div.stMarkdown p {
        text-align: center;
    }
    div.stSlider {
        padding: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters # include all Letters (a-z, A-Z)

    if use_digits:
        characters += string.digits # Add Numbers (0-9) if Selected

    if use_special:
        characters += string.punctuation # Add Special characters
    return ''.join(random.choice(characters) for _ in range(length))

# Update title with new color
st.markdown("<h1 style='text-align: center; color: #60efff;'>🔒 Password Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em;'>Create secure and strong passwords instantly!</p>", unsafe_allow_html=True)

# Create two columns for options
col1, col2 = st.columns(2)

with col1:
    length = st.slider("Password Length", min_value=6, max_value=32, value=12)

with col2:
    use_digits = st.checkbox("Include Numbers (0-9)", value=True)
    use_special = st.checkbox("Include Special Characters (!@#$)", value=True)

# Wrap button in columns for centering
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("🎲 Generate Strong Password"):
        password = generate_password(length, use_digits, use_special)
        
        # Display password in a wider box
        # st.markdown("<div class='password-display'>", unsafe_allow_html=True)
        st.subheader("Your Generated Password:")
        st.code(password, language=None)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Center the info message
        with st.container():
            # st.markdown("<div class='info-msg'>", unsafe_allow_html=True)
            st.info("💡 Tip: Click the copy button in the top-right corner of the code box above to copy your password!")
            st.markdown("</div>", unsafe_allow_html=True)

# Password strength info
# st.markdown("---")
# st.markdown("""
#     <h4 style='color: #1e88e5;'>Password Strength Tips:</h4>
#     * Use at least 32 characters
#     * Mix uppercase and lowercase letters
#     * Include numbers and special characters
#     * Avoid personal information
# """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Created with ❤️ by Aqeel Ahmed Baloch</p>",
    unsafe_allow_html=True
)