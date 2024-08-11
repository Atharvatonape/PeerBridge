import random
import zipfile
import subprocess
import pyminizip
import shutil, os

def verify_path_os(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            return False
        elif os.path.isdir(path):
            return False
    else:
        print("Path does not exist, enter again")
        return True

def convert_zip_send(connection):
        # Determine the script's directory
        path_exists = True

        while path_exists:
            directory_to_zip = input("Enter the directory/file to zip: ")
            path_exists = verify_path_os(directory_to_zip)

        script_directory = os.path.dirname(os.path.abspath(__file__))

        if os.path.isdir(directory_to_zip):
            # Create a zip file from the directory
            print(f'Zipping directory {directory_to_zip}...')
            base_name = os.path.basename(directory_to_zip)
            output_zip = f"{base_name}.zip"
            shutil.make_archive(base_name, 'zip', directory_to_zip)

            # Get the password from the user
            password = input('Enter the password for the zip file you want: ')

            # Encrypt the zip file
            encrypted_zip = f"encrypted_{output_zip}"
            pyminizip.compress(output_zip, None, encrypted_zip, password, 5)
            print(f"The zip file has been encrypted and saved as {encrypted_zip}.")

            # Copy the encrypted zip file to the script's directory
            destination_path = os.path.join(script_directory, encrypted_zip)
            shutil.copy2(encrypted_zip, destination_path)
            print(f"Encrypted zip file copied to {destination_path}.")
            done = send_file(connection, destination_path)

            # Cleanup: remove the unencrypted and encrypted zip files
            os.remove(output_zip)
            os.remove(encrypted_zip)
            return done

        elif os.path.isfile(directory_to_zip):
            # If it's a single file
            base_name = os.path.basename(directory_to_zip)
            output_zip = f"{base_name}.zip"

            # Get the password from the user
            password = input('Enter the password for the zip file you want: ')
            compression_level = 5  # Set compression level (0-9)

            # Compress and encrypt the file
            pyminizip.compress(directory_to_zip, None, output_zip, password, compression_level)
            print(f'Added and encrypted {base_name} to the zip file.')

            # Copy the encrypted zip file to the script's directory
            destination_path = os.path.join(script_directory, output_zip)
            shutil.copy2(output_zip, destination_path)
            print(f"Encrypted zip file copied to {destination_path}.")
            done = send_file(connection, destination_path)

            # Cleanup: remove the encrypted zip file
            os.remove(output_zip)
            return done

def send_file(connection, file_path):
    # Send the file name and size to the peer
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    print("Sending the file name and size to the peer")
    connection.send(f'{file_name}|{file_size}'.encode())

    # Wait for the peer to acknowledge the file info
    ack = connection.recv(1024).decode()
    if ack == 'ACK':
        print(f'Starting file transfer of {file_name}...')
        chunk_size = 1024 * 1024
        # Send the file in chunks
        with open(file_path, 'rb') as file:
            while chunk := file.read(chunk_size):  # 1024 bytes per chunk
                connection.send(chunk)

        print(f'File {file_name} sent successfully.')
        done = connection.recv(1024).decode()
        # print(done)
        if done == 'DONE':
            more = input('Do you want to send one more file?')
            if more.lower() == 'y':
                connection.send(b'MORE')
                convert_zip_send(connection)
                return True
            else:
                connection.send(b'No')
                return False
        else:
            return False
    else:
        print('Failed to receive acknowledgment from peer.')

def receive_file(connection):
    file_info = connection.recv(1024).decode()

    try:
        # Wait to receive complete file information

        print(f"Received file info: {file_info}")

        if '|' not in file_info:
            print("Invalid file info format received. Expected 'filename|filesize'.")
            connection.send(b'NAK')
            return False
        file_name, file_size = file_info.split('|')
        file_size = int(file_size)

        # Prompt user for file acceptance
        match = input(f"Do you want to accept the file {file_name} of size {file_size} bytes? (y/n) ")
        if match.lower() == "y":
            path = '/Users/A200298519/Desktop/MVP/test'
            full_path = os.path.join(path, file_name)
            connection.send(b'ACK')

            with open(full_path, 'wb') as file:
                remaining = file_size
                while remaining > 0:
                    chunk_size = min(1024 * 1024, remaining)  # 1 MB or remaining size
                    chunk = connection.recv(chunk_size)
                    if not chunk:
                        raise ConnectionError("Connection closed prematurely")
                    file.write(chunk)
                    remaining -= len(chunk)

            print(f'File {file_name} received successfully.')
            connection.send(b'DONE')
            print("There might be more files coming")
            more = connection.recv(1024)
            if more == b'MORE':
                print("More files are coming")
                receive_file(connection)
            else:
                print("No more files")
                return True
        else:
            connection.send(b'NAK')
            print("File transfer rejected.")
            return True

    except Exception as e:
        print(f'An error occurred while receiving the file: {e}')
        return False



