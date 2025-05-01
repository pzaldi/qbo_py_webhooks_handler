# QuickBooks Webhooks Handler

A Python-based project for handling QuickBooks Online webhooks, verifying their authenticity, and processing events asynchronously.

## Features

- Verifies webhook signatures using HMAC-SHA256.
- Processes QuickBooks webhook events (e.g., Payment creation, updates, and deletions).
- Asynchronous event handling using a worker thread and a queue.
- Flask-based API with health check and webhook endpoints.
- Supports OAuth2 authentication with QuickBooks Online.

## Installation

### Prerequisites

- Python 3.12 or higher
- [QuickBooks Developer Account](https://developer.intuit.com/app/developer/playground)

### Setup

1. Clone the repository

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Copy the `.env` file and replace placeholders with your actual values:
        ```bash
        cp .env.example .env
        ```
    - Update the `.env` file with your QuickBooks credentials:
        ```
        FLASK_ENV=development
        WEBHOOK_VERIFIER_TOKEN=YOUR_WEBHOOK_VERIFIER_TOKEN
        QBO_CLIENT_ID=YOUR_CLIENT_ID
        QBO_CLIENT_SECRET=YOUR_CLIENT_SECRET
        QBO_REDIRECT_URI=http://localhost:5000/callback
        QBO_COMPANY_ID=YOUR_COMPANY_ID
        QBO_REFRESH_TOKEN=YOUR_REFRESH_TOKEN
        ```

5. (Optional) Format the code:
    ```bash
    make format
    ```

6. Run the application:
    ```bash
    make run
    ```

## QuickBooks OAuth2 Setup

To obtain the required credentials for QuickBooks Online:

1. Visit the [QuickBooks Developer Playground](https://developer.intuit.com/app/developer/playground).
2. Use the playground to:
    - Generate your `CLIENT_ID` and `CLIENT_SECRET`.
    - Authorize your app and retrieve the `REFRESH_TOKEN`.
3. Update the `.env` file with these values.

## Usage

1. Start the Flask application:
    ```bash
    make run
    ```

2. Test the health check endpoint:
    ```bash
    curl http://localhost:5000/healthz
    ```

3. Use the `/quickbooks_webhook` endpoint to handle webhook notifications from QuickBooks.

## Contributing

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add feature-name"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or feedback, contact [pablozaldivar@gmail.com](mailto:pablozaldivar@gmail.com).