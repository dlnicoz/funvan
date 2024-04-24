import itertools

class LoadBalancer:
    def __init__(self, servers):
        self.servers = itertools.cycle(servers)

    def get_server(self):
        return next(self.servers)

if __name__ == '__main__':
    servers = ['server1', 'server2', 'server3']
    lb = LoadBalancer(servers)
    for i in range(10):
        print(f"Request {i} handled by {lb.get_server()}")
