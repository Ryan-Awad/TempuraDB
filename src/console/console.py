from src.helpers import send_str, get_input

def main(conn: object) -> None:
    send_str(conn, "\n[*] Welcome to the TempuraDB console\n\n")
    while True:
        query = get_input(conn, '>>> ')
        if query == 'exit':
            break