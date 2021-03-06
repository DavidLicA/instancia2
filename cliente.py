import socket
import threading
import sys
import pickle

host ="192.168.10.165"
port = 9000

class Cliente():
    def __init__(self, host=host, port=port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((str(host), int(port)))

        msg_recv = threading.Thread(target=self.data_msg)

        msg_recv.daemon = True
        msg_recv.start()

        while True:
            msg = input('-->')
            if msg != 'exit':
                self.send_msg(msg)
            else:
                self.sock.close()
                sys.exit()

    def data_msg(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    print(pickle.loads(data))
            except:
                pass
    def send_msg(self,msg):
        self.sock.send(pickle.dumps(msg))

c= Cliente()