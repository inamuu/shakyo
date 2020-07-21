import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999
server = socket.socket(socker.AF_INT, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))
server.listen(5)
print "[*] Listening on %s:%d" % (bind_ip, bind_port)

def handle_client(client_socker):
  request = client_socket.resv(1024)
  print "[*] Recived: %s" % request

  client_socket.send("ACK!")
  client_socker.close()

while True:
  client, addr + server.accept()
  print "[*] Accepted connection from %s:%d" % (addr[0], addr[1])

  client_handler = threading.Thread(target=handle_client, args=(client,))
  client_handler.start()
