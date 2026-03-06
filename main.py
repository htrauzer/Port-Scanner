import argparse 
import socket

class PortScanner:
    def __init__(self, ip, timeout=1):
        self.ip = ip
        self.timeout = timeout

    def scan_udp_port(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.settimeout(self.timeout)
                s.sendto(b'resp', (self.ip, port))
                try:
                    data, _ = s.recvfrom(4096)
                    return self._report(port, "UDP", True, data)
                except socket.timeout:
                    return self._report(port, "UDP", False)
                except socket.error as e:
                    return self._report(port, "UDP", False, error=e)
        except socket.error as e:
            return self._report(port, "UDP", False, error=e)

    def scan_tcp_port(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(self.timeout)
                result = s.connect_ex((self.ip, port))
                return self._report(port, "TCP", result == 0)
        except socket.error as e:
            return self._report(port, "TCP", False, error=e)

    def _report(self, port, protocol, is_open, data=None, error=None):
        status = "open" if is_open else "closed"
        message = f"Port {port} ({protocol}) is {status}."
        if data:
            message += f" Received data: {data}"
        if error:
            message += f" Error: {error}"
        print(message)
        return port, is_open

def parse_port_range(port_range):
    if "-" in port_range:
        start_port, end_port = map(int, port_range.split("-"))
        return range(start_port, end_port + 1)
    else:
        return [int(port_range)]

def main():
    parser = argparse.ArgumentParser(description="TinyScanner - Simple Port Scanner")
    parser.add_argument("host", type=str, help="Host to scan")
    parser.add_argument("-p", "--ports", type=str, help="Range of ports to scan")
    parser.add_argument("-u", "--udp", action="store_true", help="UDP scan")
    parser.add_argument("-t", "--tcp", action="store_true", help="TCP scan")
    args = parser.parse_args()

    scanner = PortScanner(args.host)
    ports = parse_port_range(args.ports)

    for port in ports:
        if args.udp:
            scanner.scan_udp_port(port)
        else:
            scanner.scan_tcp_port(port)


if __name__ == "__main__":
    main()

