from middle_config import PROXY_HOST, PROXY_PORT, SERVER_HOST, SERVER_PORT

def handle_clinet(client_socket, server_socket):
    while True:
        try:
            client_message = client_socket.recv()
            print("Client received", client_message)
            server_socket.send("Echo => " + client_message)
            
            server_message = server_socket.recv()
            print("Server received", server_message)
            client_socket.send("Echo => " + server_message)
        except EOFError:
            break
    print("Connection closed")
    client_socket.close()

def run_once():
    from multiprocessing.connection import Listener
    middle_socket = Listener((PROXY_HOST, PROXY_PORT))
    print("Server is running on port", PROXY_PORT)
    
    from multiprocessing.connection import Client
    server_socket = Client((SERVER_HOST, SERVER_PORT))
    print("Client is running on port", SERVER_PORT)
    
    try:
        client_socket = middle_socket.accept()
        print("Got connection from", middle_socket.last_accepted)
        
        handle_clinet(client_socket, server_socket)
    except KeyboardInterrupt:
        print("Server is shutting down")
    middle_socket.close()
    server_socket.close()

if __name__ == "__main__":
    run_once()