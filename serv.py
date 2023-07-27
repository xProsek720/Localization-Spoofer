from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import os

def run_https_server():
    server_address = ('0.0.0.0', 443)  # Replace 'localhost' with your server's domain name or IP address
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

    # Load SSL certificate and private key files
    certfile = os.path.join(os.getcwd(), 'cert.crt')  # Replace with the name of your certificate file
    keyfile = os.path.join(os.getcwd(), 'key.key')   # Replace with the name of your private key file

    httpd.socket = ssl.wrap_socket(httpd.socket, certfile=certfile, keyfile=keyfile, server_side=True)

    print('HTTPS server started on https://0.0.0.0:443/')
    httpd.serve_forever()

if __name__ == '__main__':
    run_https_server()