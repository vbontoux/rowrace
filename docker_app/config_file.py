import os

class Config:
    # Stack name
    # Change this value if you want to create a new instance of the stack
    STACK_NAME = os.getenv("ROWRACE_STACK_NAME", default="rowrace")
    
    # MODE
    ROWRACE_LOCAL_MODE = False if os.getenv("ROWRACE_LOCAL_MODE", default="FALSE") != "TRUE" else True

    # Put your own custom value here to prevent ALB to accept requests from
    # other clients that CloudFront. You can choose any random string.
    CUSTOM_HEADER_VALUE = "rowrace_31415926535"    
    
    # ID of Secrets Manager containing cognito parameters
    # When you delete a secret, you cannot create another one immediately
    # with the same name. Change this value if you destroy your stack and need
    # to recreate it with the same STACK_NAME.
    SECRETS_MANAGER_ID = f"{STACK_NAME}ParamCognitoSecret31415926535"