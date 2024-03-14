import socket

_200 = 'HTTP/1.0 200 OK\r\n'.encode('utf-8')
_200 += 'Content-type: text/html\r\n\r\n'.encode('utf-8')
_200 += '<h1>Hello, World!</h1>'.encode('utf-8')

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 8000))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            # print(f'{addr} is connecting')
            with conn:
                conn.recv(1024)
                conn.sendall(_200)
