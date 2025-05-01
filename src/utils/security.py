import hashlib
import hmac
import logging
import base64
from flask import current_app

logger = logging.getLogger(__name__)


def verify_signature(signature, payload):
    """
    Verifies the signature of the webhook notification to ensure it's from Intuit.

    Args:
        signature (str): The signature sent in the Intuit-Signature header.
        payload (bytes): The raw payload (request body) of the webhook notification.

    Returns:
        bool: True if the signature is valid, False otherwise.
    """
    try:
        verifier_token = current_app.config['WEBHOOK_VERIFIER_TOKEN']
        key = verifier_token.encode('utf-8')
        # Use the same digestmod as Intuit (SHA256)
        expected_signature = hmac.new(key, payload, hashlib.sha256).digest()
        # Encode the expected signature as a base64 string, like Intuit does.
        expected_signature_b64 = base64.b64encode(expected_signature).decode('utf-8')

        # Debugging
        logger.debug(f"Received signature:    {signature}")
        logger.debug(f"Expected signature:  {expected_signature_b64}")

        return hmac.compare_digest(signature, expected_signature_b64)  # Secure comparison
    except Exception as e:
        logger.error(f"Signature verification error: {e}", exc_info=True)
        return False
