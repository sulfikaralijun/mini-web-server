# import modul socket
from socket import *
import sys # Untuk mengakhiri program
serverSocket = socket(AF_INET, SOCK_STREAM)
# Siapkan socket server
serverPort = 5252
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

while True:
    #Terima koneksi
    print('Ready to serve')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # Kirim satu baris header HTTP ke socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        # Kirim isi file ke klien
        for i in range (0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Kirim pesan file tidak ditemukan
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send(
                "<h1>404 Not Found</h1>".encode()
        )
        # Tutup socket klien
        connectionSocket.close()
    
serverSocket.close()
sys.exit() # Menghentikan program setelah mengirim data