import socket, time

def Main():
    host = socket.gethostbyname(socket.gethostname())
    print(f"Your IP: {host}")
    port = int(input("Please enter a port: "))
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(1)
    
    print("Server Started")
    c, addr = s.accept()
    print("Connected from " + str(addr))
    
    error = False
    while not error:
        try:
            data = c.recv(1024)
            
            message_came = time.time()
            data_decoded = data.decode("utf-8")
            full_data = data_decoded + " " + str(message_came)
            bytes_full_data = bytes(full_data, 'utf-8')
                       
            print("\nFrom client: " + data_decoded)
            c.send(bytes_full_data)
        except:	
            print("\nServer Stopped")
            error = True
            
    s.close()
    
if __name__== "__main__":
    Main()