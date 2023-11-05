# NAT Traversal

A simple project for NAT traversal written in Python.

NAT traversal is useful when a client could not access a server that is in the inner network directly, but both the client and the server could access another server in a public network.

You could run `server.py` on the server machine that is in the inner network. Run `middle.py` on the public server and run `client.py` on your client machine. 

Remember to change the IP in `client_config.example.py` to the IP of your public server, and rename it to `client_config.py`.

The easiest way to realize NAT traversal is to use the `ssh -R` command. But that is not stable enough. You could use `Auto SSH` for help. The command is shown below.

```shell
autossh -M <watch_port> -f -R <public_port>:localhost:<inner_port> -NT -g <username>@<address>
```