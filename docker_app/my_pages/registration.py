import streamlit as st
from utils.auth import Auth
from config_file import Config

# Perform auth and stop if not authenticated
# Also display sidebar
Auth.perform_auth(st, Config.SECRETS_MANAGER_ID)

# Add title on the page
st.title("Formulaire d'inscriptions des bateaux")

st.write("""This demo application is a simple chat with Claude,
    a foundation model from Anthropic running on Amazon Bedrock.""")
