"""
Custom modification of: https://github.com/rakRandom/python-host-finder
"""


import socket
import threading


class HostFinder():
    def __init__(self) -> None:
        self.__result: list[str] = list()

    def check_host(self, ip: str, port: int) -> None:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            error = sock.connect_ex((ip, port))
            if error == 0:
                self.__result.append(f"{ip}:{port}")
            sock.close()
        except:
            pass

    def get_base_ip(self) -> str:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        ip_parts = local_ip.split('.')
        base_ip = '.'.join(ip_parts[:-1])
        return base_ip

    def scan_network(self, ports) -> list[str]:
        self.__result = list()
        base_ip = self.get_base_ip()
        threads = []

        for i in range(1, 255):
            ip = f"{base_ip}.{i}"
            for port in ports:
                t = threading.Thread(target=self.check_host, args=(ip, port))
                threads.append(t)
                t.start()
        
        for t in threads:
            t.join()
        
        return self.__result
