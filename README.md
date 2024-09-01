# Simple Web Server in Python

This project implements a basic web server in Python that handles `GET` and `POST` requests. It serves a custom HTML page and responds to form submissions with personalized messages.

## Features

- Serves a static HTML page (`index.html`).
- Handles `POST` requests to personalize responses.
- Displays a simple greeting based on user input.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/simple-web-server.git
   cd simple-web-server
   ```

2. Run the server:
   ```bash
   python server.py
   ```

3. Open your browser and navigate to `http://localhost:8000`.

## How It Works

- The server serves `index.html` for GET requests.
- For `POST` requests, it extracts form data and responds with a personalized message.

## Files

- `server.py`: The main server script.
- `index.html`: The HTML page served by the server.
