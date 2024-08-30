import http.server
import socketserver

# Define the port's number where the server will listen
PORT = 8000

# Create a class that will handle the requests
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):

    # Define the method that will handle the GET requests
    def do_GET(self) -> None:
        
        # If the path is '/', then set the path to 'index.html'
        if self.path == '/':
            self.path == "index.html"
        
        # Call the parent class method that will handle the GET request
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create a TCP server that will listen on the specific port
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Server started on port {str(PORT)}")
    # Start the server
    httpd.serve_forever()