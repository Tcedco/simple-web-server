import http.server
import socketserver
import urllib.parse
import os

# Define the port's number where the server will listen
PORT = 8000

# Create a class that will handle the requests
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):

    # Define the method that will handle the GET requests
    def do_GET(self) -> None:
        print(f"Received GET request for {self.path}")

        # If the path is '/', then set the path to 'index.html'
        if self.path == '/':
            self.path = "index.html"
        
        elif self.path.startswith("/greet"):
            query_components = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            name = query_components.get("name", ["Stranger"])[0]
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            response = f"""
            <!DOCTYPE html>
            <html>
                <body>
                    <h1>Hello, {name}!</h1>
                    <a href="/">Go back</a>
                </body>
            </html>
            """
            self.wfile.write(response.encode("utf-8"))
            print(f"Greeted {name}")
            return
        
        elif self.path.startswith("/static/"):
            if os.path.exists(self.path[1:]):
                return super().do_GET()

            else:
                self.send_error(404, "File Not found")
                return

        else:
            self.send_error(404, "Page Not found")
            return
        
        # Call the parent class method that will handle the GET request
        return super().do_GET()
    
    def do_POST(self) -> None:
        print(f"Received POST request")

        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        print(f"Raw POST data: {post_data}")

        post_data = urllib.parse.parse_qs(post_data.decode("utf-8"))
        print(f"Parsed POST data: {post_data}")

        # Extracting data from the form
        name = post_data.get("name", [''])[0]
        print(f"Name extracted from the form: {name}")

        # Create a response
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        response = f"""
        <!DOCTYPE html>
        <html>
            <body>
                <h1>Hello, {name}!</h1>
                <a href="/">Go back</a>
            </body>
        </html>
        """
        self.wfile.write(response.encode("utf-8"))
        print("Response sent to client")

# Create a TCP server that will listen on the specific port
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Server started on port {str(PORT)}")
    
    # Try to keep the server running

    try:
        # Keep the server running
        httpd.serve_forever()

    except KeyboardInterrupt:
        # If the user presses Ctrl+C, then stop the server
        print("\nShutting down the server...")
        httpd.shutdown()