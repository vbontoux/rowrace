import streamlit as st
from utils.auth import Auth
from logic.simple_chat import SimpleChat
from config_file import Config

# Perform auth and stop if not authenticated
# Also display sidebar
Auth.perform_auth(st, Config.SECRETS_MANAGER_ID)

# Add title on the page
st.title("Chat with Claude")

st.write("""This demo application is a simple chat with Claude,
    a foundation model from Anthropic running on Amazon Bedrock.""")

# Create object containing business logic
if "simple_chat" not in st.session_state:
    st.session_state.simple_chat = SimpleChat() 

chat_with_doc = st.session_state.simple_chat

st.divider()

# Initialize chat history
if "simple_chat_messages" not in st.session_state:
    st.session_state.simple_chat_messages = []

col1, col2, col3 = st.columns(3)

with col3:
    clear_chat_button = st.button("New conversation")

# Reset history when new conversation button is clicked
if clear_chat_button:
    st.session_state.simple_chat_messages = []
    chat_with_doc.reset_chat()
    st.rerun()

# Display chat messages from history on app rerun
for message in st.session_state.simple_chat_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# React to user input
if prompt := st.chat_input("Your input"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.simple_chat_messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        response = chat_with_doc.answer_question(prompt, message_placeholder)
        message_placeholder.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.simple_chat_messages.append({"role": "assistant", "content": response})
