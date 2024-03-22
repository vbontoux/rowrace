import streamlit as st
from utils.auth import Auth
from config_file import Config

# Perform auth and stop if not authenticated
# Also display sidebar
Auth.perform_auth(st, Config.SECRETS_MANAGER_ID)

st.write("# Bienvenu sur le site d'inscription ! 👋")

st.sidebar.success("Selectionnez une page")

st.markdown(
    """
    Ce site vous permet de vous inscrire à une course.
    
    **👈 Sélectionnez la page d'inscription pour commencer à enregistrer vos bateaux.**
   
"""
)