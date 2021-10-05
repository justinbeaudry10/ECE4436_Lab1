from socket import *
import ssl
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'
serverPort = 465

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket = ssl.wrap_socket(clientSocket)
clientSocket.connect((mailserver, serverPort))
recv = clientSocket.recv(1024).decode()
print('Connecting to server: ' + recv)
if recv[:3] != '220':
    print('220 reply not received from server.')


# Send HELO command and print server response.
heloCommand = 'HELO localhost\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print('HELO command: ' + recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Authenticate
username = "jjmac10112001@gmail.com"
password = "newpassword1!"
base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
clientSocket.send(authMsg)
recv_auth = clientSocket.recv(1024)
print(recv_auth.decode())

# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: <jjmac10112001@gmail.com>\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024)
recv2 = recv2.decode()
print('Mail From command: ' + recv2)


# Send RCPT TO command and print server response.
rcptTo = "RCPT TO: <justinbeaudry10@gmail.com>\r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024)
recv3 = recv3.decode()
print('RCPT To command: ' + recv3)


# Send DATA command and print server response.
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024)
recv4 = recv4.decode()
print('DATA command: ' + recv4)


# Send message data.
clientSocket.send(msg.encode())

# Message ends with a single period
clientSocket.send(endmsg.encode())

# Send QUIT command and get server response.
quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv5 = clientSocket.recv(1024)
recv5 = recv5.decode()
print(recv5)

clientSocket.close()