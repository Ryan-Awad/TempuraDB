from configparser import ConfigParser
from src.helpers import get_input, send_str

def authenticate(conn_socket: object) -> None:
    while True:
        username = get_input(conn_socket, 'Username: ')
        password = get_input(conn_socket, 'Password: ')
        logged_in = login(username, password)
        if logged_in:
            break
        send_str(conn_socket, 'Invalid credentials.\n\n')

def login(entered_user: str, entered_pass: str) -> bool:
    parser = ConfigParser()
    parser.read('/etc/tempura/tempura.conf')
    username = parser['common']['db_user']
    password = parser['common']['db_pass']
    return entered_user == username and entered_pass == password
