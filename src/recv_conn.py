import socket
from configparser import ConfigParser
from src.helpers import send_str, get_input
from src.authentication import authenticate
from src.console.console import main as start_console

parser = ConfigParser()
parser.read('/etc/tempura/tempura.conf')

HOST = parser['common']['db_host']
PORT = int(parser['common']['db_port'])
NOLOGIN = parser['DEFAULT']['nologin']

def recv_conn() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('[~] Listening...')
        conn, addr = s.accept()
        with conn:
            send_str(conn, '[*] Successful connection to TempuraDB\n')
            print(f'[*] Connected to {addr[0]} on port {addr[1]}')
            # if not data is the condition to check if the connection was closed by client (^C)
            if NOLOGIN != 'yes':
                authenticate(conn) # the code after this line will execute only on successful authentication
                start_console(conn) # start the main TempuraDB console
            else:
                send_str(conn, 'Access granted.\n')

                
