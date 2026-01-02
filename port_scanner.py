import socket
import sys




def port_scan(IP, starting_port, ending_port):
    try:
        for port in range(starting_port, ending_port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.1)

            result = s.connect_ex((IP, port))
            if result ==0: 
                print("Port {} is open".format(port))
                print(socket.getservbyport(port))
            s.close()

    except KeyboardInterrupt:
        print("\n Exiting")
        sys.exit()
    except socket.error:
        print("\n Server not responding")
        sys.exit()


def main():
    print("*" * 50)
    print("PORT SCANNER WILL SCAN FROM 1 to 1000")
    print("Enter IP to scan ports:")
    IP = input()
    print(f"IP Address: {IP}")
    port_scan(IP, 1, 100, 1)

if __name__ == "__main__":
    main()