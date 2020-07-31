import socket, time

def Main():
    host = socket.gethostbyname(socket.gethostname())
    print(f"Your IP: {host}")
    port = 6412
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    print("Server Started")
    
    print("Let's connect to another server")
    new_server = input("Please enter the IP of another server: ")
    new_port = int(input("Please enter a port: "))
    
    server = (new_server, new_port)
    try:
        s.connect((new_server, new_port))
        print("Connection succeeded")
    except:
        print("Connection failed")
        exit(0)
    
    error = False
    print("Please enter your message: ")
    message = input("-> ")
    while not error:
        try:
            if message != "":
                start = time.time()
                s.send(message.encode("utf-8"))
            else:
                message = input("-> ")
                continue
                
            data = s.recv(1024)
            finish = time.time()
            data_decoded = data.decode("utf-8")
            server_time = data_decoded.rsplit(None, 1)[-1]
            
            spl_data_decoded = data_decoded.split()
            remove_last_item = spl_data_decoded[:-1]
            list_to_str_data = ''.join([str(elem) for elem in remove_last_item])
                 
            print("\nFrom server: " + list_to_str_data)
            result = finish - start
            time_to_server = float(server_time) - start
            
            print("Time to server: " + str(time_to_server) + " seconds.")
            print("Full program time: " + str(result) + " seconds.")
            message = input("-> ")
            
        except:
            error = True
            
    s.close()
    
if __name__== "__main__":
    Main()