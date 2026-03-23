from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
s.send(str.encode('Hello, world'))
data = s.recv(1024)
print (bytes.decode(data))
s.close()
[ec2-user@ip-172-31-67-45 ~]$ cat new_client.py 
from socket import *
from constCS import *
import time

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

print("Calculadora RPC")
print("Comandos:")
print("ADD a b | SUB a b | MUL a b | DIV a b | POW a b | SQRT a")

while True:
    msg = input("\nDigite: ")
    if msg.lower() == "sair":
        break

    inicio = time.time()

    s.send(msg.encode())
    data = s.recv(4096)

    fim = time.time()
    tempo_total = fim - inicio

    print("Resultado:", data.decode())
    print(f"Tempo: {tempo_total:.6f}s")

s.close()
