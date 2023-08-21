import socket
import bcrypt


pw = 'pw123'
hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
given = input("Input the password to begin connection to client:  ")

#socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host and port
host = '127.0.0.1'
port = 9002
#bind
#set up to take connections
if bcrypt.checkpw(given.encode(), hash):
  s.bind((host, port))
  s.listen()
  conn, addr = s.accept()
  print(f'Connection recieved from {addr}')
  print(conn)
else: 
  print("Access Denied")

