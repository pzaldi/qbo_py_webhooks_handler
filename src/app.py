import os
from flask import Flask
from threading import Thread
from queue import Empty
import logging

from src.queue_manager import event_queue  # Import the event queue
from src.routes import webhook_route  # Import the webhook route
from src.routes import health_check_route # Import the health_check route
from config.config import get_config  # Import the configuration function

# Initialize Flask application
app = Flask(__name__)

# Get the configuration
config = get_config()
app.config.from_object(config)

# Set up logging
logging.basicConfig(level=app.config['LOG_LEVEL'],  # Use LOG_LEVEL from config
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

#  Import the process_event function from the services module
from src.services.event_processor import process_webhook_event

def worker():
    """
    This function runs in a separate thread and processes events from the queue.
    """
    while True:
        try:
            event_data = event_queue.get(timeout=5)  #  Timeout after 5 seconds
            process_webhook_event(event_data, event_queue)  # Call the process_event
            event_queue.task_done()
        except Empty:
            pass  #  Timeout: Check if the server is shutting down
        except Exception as e:
            logger.error(f"Worker thread error: {e}", exc_info=True)
            #  Consider error handling here as well

#  Start the worker thread
event_processor_thread = Thread(target=worker, daemon=True)
event_processor_thread.start()

# Register routes (Blueprints)
app.register_blueprint(webhook_route.webhook_bp)  # Register the webhook blueprint
app.register_blueprint(health_check_route.health_check_bp) # Register the health_check blueprint

if __name__ == '__main__':
    #  Run the Flask app.  The configuration is now loaded.
    app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'], ssl_context=('adhoc')) #for production use self-signed cert ssl_context=('cert.pem', 'key.pem')
