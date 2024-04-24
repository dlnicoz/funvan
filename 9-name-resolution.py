import socket

print("Advait Chandorkar; BEB-224 / DC - Exp 9\n")

def get_ip_address(url):
    try:
        host_ip = socket.gethostbyname(url)
        print("Hostname:", url)
        print("IP:", host_ip)
    except socket.gaierror:
        print("Unable to get hostname and IP")

if __name__ == '__main__':
    url = "www.lamborghini.com"
    get_ip_address(url)