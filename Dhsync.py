from utils.secret import get_secret, get_keys
import socket
import getpass
import hmac
import hashlib

SECRET_KEY = '6600861'

# def initialization():
#     print("Dhsync initialization \n")
#     keys = get_keys()
#     ans =str(input("Do you want to Communicate with another user? Press the number \n 1) To initaite \n 2) To recieve "))
#     match ans:
#         case 1:
#             initiate_process("192.168.1.179", 5000)
#         case 2:
#             authenticate_peer()
#         case _:
#             initialization()
#     print(keys)

def initiate_process(peer_ip, peer_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((peer_ip, peer_port))

    # Get user credentials (e.g., password)
    message = getpass.getpass('Enter your password: ').encode()

    # Authenticate the peer
    if authenticate_peer(client_socket, message):
        print('Authenticated and connected to peer.')
        # Continue with the process (send/receive messages)
    else:
        print('Authentication failed. Closing connection.')
    client_socket.close()

def authenticate_peer(connection, message):
    # Send the message
    connection.send(message)
    # Calculate and send the HMAC
    message_hmac = hmac.new(SECRET_KEY, message, hashlib.sha256).digest()
    connection.send(message_hmac)

    # Receive authentication response
    response = connection.recv(1024)
    print(response.decode())

    return response.decode() == 'Authentication successful'

def receive_process(local_port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', local_port))
    server_socket.listen(1)

    print('Waiting for connection...')
    connection, address = server_socket.accept()
    print(f'Connected by {address}')

    if authenticate_connection(connection):
        print('Peer authenticated.')
        # Continue with the process (send/receive messages)
    else:
        print('Authentication failed. Closing connection.')
        connection.close()

def authenticate_connection(connection):
    # Expect the peer to send a message for authentication
    message = connection.recv(1024)
    # Expect the peer to send a HMAC of the message
    peer_hmac = connection.recv(1024)
    # Calculate HMAC on this side
    server_hmac = hmac.new(SECRET_KEY, message, hashlib.sha256).digest()

    if hmac.compare_digest(server_hmac, peer_hmac):
        connection.send(b'Authentication successful')
        return True
    else:
        connection.send(b'Authentication failed')
        return False

def main():
    print("Welcome to the peer-to-peer process manager.")
    choice = input("Do you want to initiate (i) or receive (r) a process? (i/r): ").strip().lower()
    if choice == 'i':
        peer_ip = input("Enter the IP address of the peer: ").strip()
        peer_port = int(input("Enter the port of the peer: ").strip())
        initiate_process(peer_ip, peer_port)
    elif choice == 'r':
        local_port = int(input("Enter the port to listen on: ").strip())
        receive_process(local_port)
    else:
        print("Invalid choice. Please enter 'i' to initiate or 'r' to receive.")

if __name__ == "__main__":
    main()