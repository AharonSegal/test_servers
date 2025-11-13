import socket

HOST = '127.0.0.1'
PORT = 8000

# Create a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server running on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        data = conn.recv(1024)  # Receive raw request
        print(data.decode())     # You’d have to parse this yourself
        response = "HTTP/1.1 200 OK\n\nHello, raw HTTP!"
        conn.sendall(response.encode())
