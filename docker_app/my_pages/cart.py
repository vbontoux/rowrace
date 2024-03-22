import json
import time
import streamlit as st
import numpy as np
from utils.auth import Auth
from config_file import Config
from utils.llm import Llm

# Perform auth and stop if not authenticated
# Also display sidebar
Auth.perform_auth(st, Config.SECRETS_MANAGER_ID)

st.markdown("# Cart")

st.write(
    """Dans cette page vous trouverez le révapitulatif de vos inscriptions et le lien de paiement"""
)

