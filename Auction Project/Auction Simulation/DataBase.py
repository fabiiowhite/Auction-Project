
ProductList=["Socks","Shoes"]

Clients = ["Junior","Tristan"]

def ClientsDB():

    DataBase_Clients = open("DataBase_Clients.txt", "a")
    print("")
    print("Input the Client List")
    for i in range(3):
        print("Client",i+1,":")
        Write = input()
        DataBase_Clients.write(Write+"\n")
    DataBase_Clients.close()

def ProductsDB():
    DataBase_Products = open("DataBase_Products.txt", "a")
    print("")
    print("Input the Product List")
    for i in range(3):
        print("Product",i+1,":")
        Write = input()
        DataBase_Products.write(Write+"\n")
    DataBase_Products.close()

def BudgetDB():
    DataBase_Budget = open("DataBase_Budget.txt", "a")
    print("")
    print("Input the Budget List")
    for i in range(3):
        print("Budget for Client ",i+1,":")
        Write = input()
        DataBase_Budget.write(Write+"\n")
    DataBase_Budget.close()

