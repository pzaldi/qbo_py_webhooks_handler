import datetime
import logging
from queue import Queue

from quickbooks.objects import Payment
from src.services.qbo_service import get_quickbooks_client # Import the QuickBooks client to start interacting with the API

logger = logging.getLogger(__name__)


def handle_payment_created(entity_id, last_updated, event_data, event_queue: Queue):
    """Handles the creation of a Payment."""
    logger.info(f"Created Payment with ID: {entity_id}, Last Updated: {last_updated}")
    #  Handle Payment create logic here
    event_info = {'event_type': 'Create_Payment', 'entity_id': entity_id, 'event_data': event_data}
    event_queue.put(event_info)


def handle_payment_updated(entity_id, last_updated, event_data, event_queue: Queue):
    """Handles the update of a Payment."""
    logger.info(f"Updated Payment with ID: {entity_id}, Last Updated: {last_updated}")
    #  Handle Payment update logic here
    event_info = {'event_type': 'Update_Payment', 'entity_id': entity_id, 'event_data': event_data}
    event_queue.put(event_info)


def handle_payment_deleted(entity_id, last_updated, event_data, event_queue: Queue):
    """Handles the deletion of a Payment."""
    logger.info(f"Deleted Payment with ID: {entity_id}, Last Updated: {last_updated}")
    #  Handle Payment deletion logic here
    event_info = {'event_type': 'Delete_Payment', 'entity_id': entity_id, 'event_data': event_data}
    event_queue.put(event_info)