
# PeerBridge - Peer-to-Peer Process Manager

To use 
```bash
pip install peerbridge
```

## Project Details

The Peer-to-Peer (P2P) Process Manager is a Python-based **Command Line Project** designed to facilitate secure file transfer between two peers over a network. The system allows one peer to initiate a file transfer and another to receive it, ensuring security through HMAC-based authentication and encrypted zip file transfers.

## Motivation

The motivation behind the Peer-to-Peer Process Manager was to create a simple yet secure method of transferring files between two devices. Whether for sharing data between colleagues, syncing files across devices, or securely transmitting sensitive information, this tool provides a straightforward solution.

### Key Features:
- **Secret**: You would need a secret word with your friend, otherwise it won't work. Secrecy is the utmost virtue we value 
- **File Compression and Encryption**: Compresses directories or files into zip archives and encrypts them with a password for secure transmission.
- **Secure Authentication**: Uses HMAC (Hash-based Message Authentication Code) to authenticate peers, ensuring that only authorized users can initiate or receive file transfers.
- **Flexible Transfer**: Supports both directory and single-file transfers, with the option to send multiple files in sequence.
- **Automatic Port Reuse**: Implements socket options to allow the server to reuse ports immediately, reducing the likelihood of encountering port conflicts.


### Why P2P?

Peer-to-peer file transfer allows for direct communication between devices without relying on a centralized server. This method increases speed and efficiency while reducing potential points of failure or bottlenecks. Additionally, P2P networks are more resilient, as they do not rely on a single server that could be a target for attacks or system failures.

## Installation

To run the Peer-to-Peer Process Manager on your machine, follow these steps:

### Prerequisites

1. **Python 3.x**: Ensure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/).
2. **pip**: Make sure you have `pip` installed to manage Python packages.

### Step 1: Installing

Clone the project repository from GitHub (replace `your-repository-url` with the actual URL of your repository):

```bash
pip install peerbridge
```

### Step 2: Run the Program

To start the program, navigate to the project directory and run in terminal:

```bash
peerbridge
```
or

Navigate to the project directory and in call it:

```bash
peerbridge.main()
```

### Configuration:

- **IP address**: You should know the ip of the person you want it connect.
- **Port Configuration**: You have to select the port, 8080 is a common choice.


## Troubleshooting

### Common Issues:

- **Port Already in Use**: If you encounter an error stating that the port is already in use, ensure that no other processes are using the specified port, or configure the script to use a different port.
- **Authentication Failed**: If authentication fails, double-check the secret key being used by both peers. The secret key must match exactly on both sides.
- **File Transfer Errors**: Ensure that the file paths and directories specified in the script exist and have the correct permissions for reading and writing.

### Additional Help:

If you run into issues not covered here, consult the error messages provided by the script, and ensure that all dependencies are installed correctly.

## Future Enhancements

Potential future improvements to the project could include:
- **Dynamic Path Configuration**: Allowing users to specify paths dynamically during runtime instead of using hardcoded values.
- **GUI Interface**: Creating a graphical user interface (GUI) to make the tool more user-friendly.
- **Additional Security Features**: Implementing more advanced encryption methods or multi-factor authentication for enhanced security.
- **Cross-Platform Compatibility**: Ensuring the tool works seamlessly across different operating systems (Windows, macOS, Linux).

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

Contributions to the project are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request with your enhancements or bug fixes.

---

**Thank you for using the Peer-to-Peer Process Manager!**  
Feel free to reach out for any questions or support related to this project.
