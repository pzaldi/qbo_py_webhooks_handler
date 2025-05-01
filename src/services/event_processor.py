import logging
from queue import Queue

from src.services.handlers import payment_handler

logger = logging.getLogger(__name__)

#  Use a dictionary to map operation and name combinations to handler functions.
_EVENT_HANDLERS = {
    ('Create', 'Payment'): payment_handler.handle_payment_created,
    ('Update', 'Payment'): payment_handler.handle_payment_updated,
    ('Delete', 'Payment'): payment_handler.handle_payment_deleted,
}


def process_webhook_event(event_data, event_queue: Queue):
    """
    Processes the QuickBooks webhook event data, extracts relevant information,
    and puts the event data into a queue for asynchronous processing.  This
    function uses a dictionary to dispatch to specific handler functions
    based on the operation and name.

    Args:
        event_data (dict): The JSON payload from the QuickBooks webhook.
        event_queue (Queue): The queue to put the event data into.
    """
    event_notifications = event_data.get('eventNotifications', [])
    for event_notification in event_notifications:
        data_change_event = event_notification.get('dataChangeEvent')
        if data_change_event:
            entities = data_change_event.get('entities', [])
            for entity in entities:
                # Extract relevant information from the entity
                # and dispatch to the appropriate handler function.
                # This assumes the entity has 'operation', 'name', 'id', and 'lastUpdated' fields.
                # Adjust the keys based on the actual structure of your entity.
                # For example: 
                operation = entity.get('operation')
                name = entity.get('name')
                entity_id = entity.get('id')
                last_updated = entity.get('lastUpdated')
                event_data = entity

                handler_key = (operation, name)
                # Check if the handler exists for the operation and name
                # If not, log a warning and put the event data into the queue
                handler = _EVENT_HANDLERS.get(handler_key)
                if handler:
                    handler(entity_id, last_updated, event_data, event_queue)  # Pass the queue
                else:
                    logger.warning(f"Unhandled operation: {operation}, name: {name}, Entity ID: {entity_id}")
                    event_queue.put({'event_type': 'Unknown', 'entity_id': entity_id, 'event_data': event_data})