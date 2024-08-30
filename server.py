import http.server
import socketserver

# Define the port's number where the server will listen
PORT = 8000

# Create a request handler that will serve the files from the current directory
Handler = http.server.SimpleHTTPRequestHandler

# Create a TCP server that will listen on the specific port
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server started at localhost: {str(PORT)}")
    # Start the server
    httpd.serve_forever()