import platform
import socket
import uuid


class SysUtils:
    @staticmethod
    def get_hostname() -> str:
        return socket.gethostname()

    @staticmethod
    def get_ip_address() -> str:
        return socket.gethostbyname(socket.gethostname())

    @staticmethod
    def get_mac_address() -> str:
        mac = hex(uuid.getnode())[2:].zfill(12)
        return ":".join([mac[x : x + 2] for x in range(0, 12, 2)])

    @staticmethod
    def get_os_name() -> str:
        return platform.system()

    @staticmethod
    def get_traceid() -> str:
        return str(uuid.uuid4())
