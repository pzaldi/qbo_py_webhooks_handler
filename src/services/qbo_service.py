# src/services/qbo_service.py
import logging
import os
from quickbooks import QuickBooks
from intuitlib.client import AuthClient

logger = logging.getLogger(__name__)

_qb_client = None  # Module-level variable to store the QuickBooks client instance

def get_quickbooks_client():
    """
    Retrieves the QuickBooks client instance.  If it doesn't exist, it initializes it.
    This ensures that the client is only initialized once per application.

    Returns:
        QuickBooks: The QuickBooks client instance.
        Raises: Exception:  If configuration is missing or the client fails to initialize.
    """
    global _qb_client  # Access the module-level variable

    if _qb_client is None:
        try:
            # connect to QuickBooks using environment variables
            # IMPORTANT:  Make sure to set these environment variables in your environment
            auth_client = AuthClient(
                client_id=os.environ.get('QBO_CLIENT_ID'),
                client_secret=os.environ.get('QBO_CLIENT_SECRET'),
                environment=os.environ.get('QBO_ENVIRONMENT'),
                redirect_uri=os.environ.get('QBO_REDIRECT_URI'),
            )

            _qb_client = QuickBooks(
                auth_client=auth_client,
                refresh_token=os.environ.get('QBO_REFRESH_TOKEN'),
                company_id=os.environ.get('QBO_COMPANY_ID'),
            )
            logger.info("Initialized QuickBooks client")  # Log initialization

        except Exception as e:
            logger.error(f"Failed to initialize QuickBooks client: {e}", exc_info=True)
            #  IMPORTANT:  Raise the exception again so that the caller knows initialization failed.
            #  A common pattern is to create a custom exception class for this.
            raise  # Re-raise the caught exception

    return _qb_client
