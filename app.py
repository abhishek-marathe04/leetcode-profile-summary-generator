import streamlit as st
from streamlit.components.v1 import html

from main import leetcode_agent_using_zero_shot_react

st.title('Leetcode Profile Summary')

st.subheader('Generate a summary of leetcode profile')

# Define sample prompts
sample_prompts = {
    'Fetch Profile Details':'"Get Profile Details": "Get the profile details of username letsmailabhishekmarathe"',
    'Fetch Programing Langauge Stats':'"Get Programing Language Stats": "Get the Programing Language Stats of username letsmailabhishekmarathe"'
}

# Streamlit UI
st.subheader("Sample Prompts")

st.write("Here are some sample prompts you can use. Copy and paste them manually into the input box below:")

# Display each sample prompt with a label
for prompt_name, prompt_text in sample_prompts.items():
    st.markdown(f"#### {prompt_name}")
    st.code(prompt_text, language="plaintext")  # Nicely formatted, easy to copy

# Input for LinkedIn profile content
users_query = st.text_area("Copy any Sample Prompt or Use your own query here:", height=100)

# Using Stateful button
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button('Generate Summary', on_click=click_button)

# Generate summary on button click
if st.session_state.clicked:
    if users_query.strip():
        with st.spinner("Generating summary..."):
            try:
                summary = leetcode_agent_using_zero_shot_react(query=users_query)
                st.success("Summary Generated!")
                st.markdown(summary)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter query to generate a summary.")
