# pip install Faker
import socket
from faker import Faker

ip = input("input ip:")
serverIP = socket.gethostbyname(ip)
portlist =[5000, 5500]

for port in portlist:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(s)

fake = Faker()

email = fake.email()
print(email)
