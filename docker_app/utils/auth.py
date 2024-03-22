import boto3
import json
from streamlit_cognito_auth import CognitoAuthenticator
from st_pages import Page, show_pages, hide_pages
from utils.page_list import list_of_pages
from config_file import Config

class Auth:

    @staticmethod
    def _get_authenticator(secret_id):
        """
        Get Cognito parameters from Secrets Manager and
        returns a CognitoAuthenticator object.
        """
        # Get Cognito parameters from Secrets Manager
        secretsmanager_client = boto3.client("secretsmanager")
        response = secretsmanager_client.get_secret_value(
            SecretId=secret_id,
        )
        secret_string = json.loads(response['SecretString'])
        pool_id = secret_string['pool_id']
        app_client_id = secret_string['app_client_id']
        app_client_secret = secret_string['app_client_secret']

        # Initialise CognitoAuthenticator
        authenticator = CognitoAuthenticator(
            pool_id=pool_id,
            app_client_id=app_client_id,
            app_client_secret=app_client_secret,
        )

        return authenticator
        
    @staticmethod
    def perform_auth(st, secrets_manager_id):
        '''
        Perform authentication and stop the app if not logged in.
        Params:
            st: Streamlit app object.
            secrets_manager_id: AWS Secrets Manager secret ID.
        Returns:
            None.
        '''
        
        # Initialise CognitoAuthenticator
        if not Config.ROWRACE_LOCAL_MODE:
          authenticator = Auth._get_authenticator(secrets_manager_id)
          
          # Authenticate user, and stop here if not logged in
          is_logged_in = authenticator.login()
          
          def logout():
              authenticator.logout()
          
          if not is_logged_in:
              hide_pages([elt[1] for elt in list_of_pages])
              st.stop()

          with st.sidebar:
              st.text(f"Welcome,\n{authenticator.get_username()}")
              st.button("Logout", "logout_btn", on_click=logout)

          # Specify what pages should be shown in the sidebar, and what their titles and icons
          # should be
          show_pages(
              [Page(*elt) for elt in list_of_pages]
          )
        else:
          is_logged_in = True
          st.sidebar.text("Welcome, \ntest")
          show_pages(
              [Page(*elt) for elt in list_of_pages]
          )

        return is_logged_in
        
