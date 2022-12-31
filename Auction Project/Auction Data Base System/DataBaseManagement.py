from DataBaseFuncions import Clients
from DataBaseFuncions import Products

class DataBaseRegistration(Clients,Products):

    N =  int(input("How many Clients do you wish to register: "))

    for i in range(N):
        Clients.RegisterClient(Clients)


    N = int(input("How many Products do you wish to register: "))
    for i in range(N):
        Products.RegisterProduct(Products)