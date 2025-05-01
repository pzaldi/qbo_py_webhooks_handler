from flask import Blueprint, request, abort, jsonify
import logging
from src.utils.security import verify_signature  # Import the verify_signature function
from src.queue_manager import event_queue  # Import the event queue


logger = logging.getLogger(__name__)

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/quickbooks_webhook', methods=['POST'])
def handle_webhook():
    """
    This route handles incoming webhook notifications from QuickBooks.
    It verifies the signature, parses the payload, and adds the event to the queue
    for asynchronous processing.
    """
    signature = request.headers.get('Intuit-Signature')
    payload = request.data  # Get the raw request body (bytes)

    if not signature:
        logger.error("Missing Intuit-Signature header")
        abort(400, 'Missing Intuit-Signature header')  # Bad Request

    if not payload:
        logger.error("Missing payload")
        abort(400, 'Missing payload')

    if not verify_signature(signature, payload):
        logger.warning("Invalid signature")
        abort(401, 'Invalid signature')  # Unauthorized

    try:
        event_data = request.get_json()  # Parse JSON payload
        logger.info("Received valid webhook notification")
        event_queue.put(event_data)  # Add to the queue for processing
        return jsonify({'status': 'ok'}), 200  # Quick response
    except Exception as e:
        logger.error(f"Error handling webhook: {e}", exc_info=True)
        abort(500, 'Internal server error')  # Internal Server Error