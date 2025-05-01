import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Config:
    """
    Base configuration class.
    """
    DEBUG = False
    TESTING = False
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()
    QBO_ENVIRONMENT = os.environ.get('QBO_ENVIRONMENT', 'sandbox').lower() # Default to sandbox

    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    REDIRECT_URI = os.environ.get('REDIRECT_URI')
    COMPANY_ID = os.environ.get('COMPANY_ID')
    REFRESH_TOKEN = os.environ.get('REFRESH_TOKEN')


class DevelopmentConfig(Config):
    """
    Configuration for development environment.
    """
    DEBUG = True
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG').upper()
    WEBHOOK_VERIFIER_TOKEN = os.environ.get('WEBHOOK_VERIFIER_TOKEN')
    QBO_ENVIRONMENT = os.environ.get('QBO_ENVIRONMENT', 'sandbox').lower()

class ProductionConfig(Config):
    """
    Configuration for production environment.
    """
    WEBHOOK_VERIFIER_TOKEN = os.environ.get('WEBHOOK_VERIFIER_TOKEN') #  Important:  Set this in your production environment.
    QBO_ENVIRONMENT = os.environ.get('QBO_ENVIRONMENT', 'production').lower()
    
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    REDIRECT_URI = os.environ.get('REDIRECT_URI')
    COMPANY_ID = os.environ.get('COMPANY_ID')
    REFRESH_TOKEN = os.environ.get('REFRESH_TOKEN')

def get_config():
    """
    Returns the appropriate configuration class based on the environment.
    """
    env = os.environ.get('FLASK_ENV', 'development').lower()  #  Default to 'development'
    if env == 'production':
        return ProductionConfig
    elif env == 'development':
        return DevelopmentConfig
    #elif env == 'testing':
        #return TestingConfig #Add a testing config if needed
    else:
        return DevelopmentConfig  #  Default