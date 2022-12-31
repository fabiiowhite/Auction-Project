class Clients:

    def __init__(self,Name,Budget):
        self.Name = Name
        self.Budget = Budget

    def List(self):
         return self.Name ,self.Budget

    def RegisterClient(self):
        DataBase = open("DataBase_Clients.txt", "a")

        for i in range(1):
            print("-----------------------")
            ObjectName = input("ClientID: ")
            ClientID = ObjectName
            ObjectName = Clients(input("Client name: "), input("Client budget: "))
            print("-----------------------")
            DataBase.write(ObjectName.List().__str__()+"\n")

            print("")
            print("         Client added!")
            print("")

        DataBase.close()


class Products:

    def __init__(self,Product,Value):
        self.Product = Product
        self.Value = Value

    def List(self):
         return self.Product ,self.Value

    def RegisterProduct(self):
        DataBase = open("DataBase_Products.txt", "a")

        for i in range(1):
            print("-----------------------")
            ObjectName = input("Product ID: ")
            ClientID = ObjectName
            ObjectName = Products(input("Product Name: "), input("Product Value: "))
            print("-----------------------")
            DataBase.write(ObjectName.List().__str__()+"\n")

            print("")
            print("         Product added!")
            print("")

        DataBase.close()

