import socket

# Create socket and connect
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# Change the request to the correct file
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

# Receive and decode response
response = b''
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    response += data

mysock.close()

# Decode and print headers
decoded_response = response.decode()
headers, _, _ = decoded_response.partition('\r\n\r\n')
print(headers)
