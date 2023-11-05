from server_config import SERVER_HOST, SERVER_PORT
import multiprocessing

def handle_clinet(client_socket):
    while True:
        try:
            message = client_socket.recv()
            print("Received", message)
            client_socket.send("Echo => " + message)
        except EOFError:
            break
    print("Connection closed")
    client_socket.close()

def run_server():
    from multiprocessing.connection import Listener
    server_socket = Listener((SERVER_HOST, SERVER_PORT))
    print("Server is running on port", SERVER_PORT)
    
    pool = multiprocessing.Pool(12)
    try:
        while True:
            client_socket = server_socket.accept()
            print("Got connection from", server_socket.last_accepted)
            
            pool.apply_async(handle_clinet, (client_socket, ))
    except KeyboardInterrupt:
        print("Server is shutting down")
        pool.close()
    pool.join()
    server_socket.close()

def run_once():
    from multiprocessing.connection import Listener
    server_socket = Listener((SERVER_HOST, SERVER_PORT))
    print("Server is running on port", SERVER_PORT)
    
    try:
        client_socket = server_socket.accept()
        print("Got connection from", server_socket.last_accepted)
        
        handle_clinet(client_socket)
    except KeyboardInterrupt:
        print("Server is shutting down")
    server_socket.close()

if __name__ == "__main__":
    run_once()