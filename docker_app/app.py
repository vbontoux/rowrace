import streamlit as st
from utils.auth import Auth
from config_file import Config

# Perform auth and stop if not authenticated
# Also display sidebar
Auth.perform_auth(st, Config.SECRETS_MANAGER_ID)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    This website is a compilation of GenAI demos, built with Streamlit and
    deployed with AWS CDK.
    
    
    **👈 Select a demo from the sidebar** to see some examples.
    These demos use Amazon Bedrock, an easy to use service to access
    foundation models through an API.
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Ask a question your AWS Solutions Architect
"""
)