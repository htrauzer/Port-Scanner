# Port Scanner

This is a functional tool designed to demonstrate the fundamental differences between TCP and UDP communication. It was built as a learning project to explore socket programming and port discovery in Python.

## Project Structure

The project is split into three parts to allow for local testing without needing an external server:

`main.py`: The scanning engine that handles user input and port iteration.

`tcp.py`: A simple TCP listener to simulate an open service.

`udp.py`: A simple UDP listener to simulate an open service.

## Setup & Testing ## 
To test the scanner on your local machine, run the listeners in separate terminal windows to create "targets":

1. Start the TCP target:
    `python tcp.py`

2. Start the UDP target:
    `python udp.py`

3. Run the scanner (in a new window):
    `python main.py 127.0.0.1 -p 8080 -t`
    `python main.py 127.0.0.1 -p 8080 -u`

## Usage Examples

The scanner accepts a single target IP, a port or range, and a protocol flag.

### TCP Scanning

Checks for a successful three-way handshake.

```python
# Scan a single port
python main.py 127.0.0.1 -p 8080 -t

# Scan a range of ports
python main.py 127.0.0.1 -p 8000-8010 -tt
```

### UDP Scanning

Sends a datagram to the target port to check for a response.

```python
# Scan a single port
python main.py 127.0.0.1 -p 8080 -u

# Scan a range of ports
python main.py 127.0.0.1 -p 5000-5050 -u
```
## Technical Details

Socket Module: Uses Python's built-in socket library for low-level network interface.
  
Error Handling: Implements basic timeout logic to prevent the scanner from hanging on filtered or closed ports.
 
Input Parsing: Uses argparse to handle command-line arguments and string slicing to process port ranges (e.g., 80-443).


