# Helper functions

def send_str(conn_socket: object, string: str) -> None: # sends string (UTF-8 encoding) through the conn_socket socket
    conn_socket.sendall(string.encode('utf-8'))

def get_input(conn_socket: object, prompt: str, buffer_size : int = 1024) -> str:
    send_str(conn_socket, prompt)
    input_ = conn_socket.recv(buffer_size)
    input_ = decode_bytes(input_)
    return input_

def decode_bytes(bytes_: bytes) -> str:
    return bytes_.decode('utf-8').replace('\n', '')
