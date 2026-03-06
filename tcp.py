import socket

class TCPServer:
    def __init__(self, host='127.0.0.1', port=8080):
        self.host = host
        self.port = port

    def start_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()

            print(f"TCP Server listening on {self.host}:{self.port}")

            while True:
                conn, addr = s.accept() 
                with conn:
                    print(f"Connected by {addr}")
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        print(f"Received data: {data.decode()}")
                        conn.sendall(data)  # Echo back the received data
                print("Connection closed")

def main():
    server = TCPServer()  
    server.start_server()


if __name__ == "__main__":
    main()
