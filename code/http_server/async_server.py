import select
import socket

_200 = 'HTTP/1.0 200 OK\r\n'.encode('utf-8')
_200 += 'Content-type: text/html\r\n\r\n'.encode('utf-8')
_200 += '<h1>Hello, World!</h1>'.encode('utf-8')


def server(server_address):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(server_address)
    server.listen(5)
    while True:
        yield 'read', server
        client_sock, addr = server.accept()
        tasks.append(respond(client_sock))


def respond(sock):
    yield 'read', sock
    sock.recv(1024)
    with sock:
        yield 'write', sock
        sock.sendall(_200)


def event_loop():
    while True:
        while not tasks:
            # No active tasks to run, wait for I/O
            can_read, can_write, _ = select.select(read_waiting, write_waiting, [])
            # Socket ready for reading
            for s in can_read:
                tasks.append(read_waiting.pop(s))
            # Socket ready for writing
            for s in can_write:
                tasks.append(write_waiting.pop(s))

        while tasks:
            task = tasks.pop(0)
            try:
                why, what = next(task)
                if why == 'read':
                    read_waiting[what] = task
                elif why == 'write':
                    write_waiting[what] = task
            except StopIteration:
                print("Task Done")


if __name__ == "__main__":
    tasks = []
    read_waiting = {}
    write_waiting = {}
    tasks.append(server(('localhost', 8000)))
    event_loop()
