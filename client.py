from client_config import PROXY_HOST, PROXY_PORT
from multiprocessing.connection import Client

client = Client((PROXY_HOST, PROXY_PORT))

for _ in range(5):
    client.send("Hello")
    print(client.recv())