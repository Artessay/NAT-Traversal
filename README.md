# NAT Traversal

A simple project for NAT traversal written in Python.

NAT traversal is usefule when a client could not access a server that is in the inner network directly, but both the client and the server could access another server in a public network.

You could run `server.py` in the server machine that is in inner network. Run `middle.py` in the public server and run `client.py` in your client machine. 

Remember to change the IP in `client_config.example.py` to the IP of your public server, and rename it to `client_config.py`.