def Rules():

    print("\n\n---------------WELCOME TO THE AUCTION----------------")
    print("\n\n-----------------------RULES-------------------------")
    print("\nThere are two options, which are RAISE and PASS.")
    print("")
    print("1. If you wish to RAISE, you will have to throw in a ")
    print("   higher price than the other Clients.")
    print("2. If you wish to PASS, that means you will pass your")
    print("   turn and let the other Clients take their chances.")
    print("")
    print("                     GOOD LUCK!                      ")
    print("")
    print("-----------------------------------------------------")
    print("")

Rules()

print("")
print("-----------------------------------------")
print("              AUCTIONER INFO             ")
print("-----------------------------------------")
print("")

Quant = int(input("Input the number of Clients: "))
Product = input("Input the name of the product: ")
Value = int(input("Input the starting price: "))
ProductList=[]
ProductList.append(Product)

print("")
print("-----------------------------------------")
print("              CLIENT SIGN-UP            ")
print("-----------------------------------------")
print("")

Clients = []
for i in range(Quant):
    print("")
    print("-----------------------------------------")
    SignUp = input("Clint ID-00"+(i+1).__str__()+": ")
    Clients.append(SignUp)
    print("")
    print("-----------------------------------------")
    print("         Registration Complete!")
    print("-----------------------------------------")


Sold = 1
Auctioning = 0
Options = ["RAISE","raise","Raise","PASS","pass","Pass"]
Option = ""
Round = 0
Price = 0
Winner = ["Empty"]
Raises = 0
Passes = 0

while Sold > 0:
    OptionError = 0
    Raises = 0
    Passes = 0
    for i in range(len(Clients)):
        print("")
        print("The current price for the "+Product+" is of ",Value,"$")
        print("")
        Option = input("Mr/Mrs "+Clients[i]+" Going once, Twice ... ")

        if Option in Options:
            if Option == Options[0] or Option == Options[1] or Option == Options[2]:
                print("")
                Price = int(input("Throw your auction! -- "))
                if Price > Value:
                   Value = Price
                   print("------------------------------------------------")
                   print("Mr/Mrs " + Clients[i] + " raises the price to ",Value,"$")
                   print("------------------------------------------------")
                   Winner[0] = Clients[i]
                   Raises = Raises + 1
                elif Price == Value or Price < Value :
                   print("The RAISE was invalid, so we automatically PASS Mr/Mrs "+Clients[i])
                   Price = 0
                   Passes = Passes + 1
            else:
               print("")
               print("----------------------------------------")
               print("Mr/Mrs "+Clients[i]+" goes for the pass!")
               print("----------------------------------------")
               Passes = Passes + 1
        else:
            while OptionError != 1:
                print("")
                print("Ouuuhh, that was foul play Mr/Mrs "+Clients[i]+" , pay attention!")
                print("")
                Option = input("Mr/Mrs " + Clients[i] + "Going once, Twice ... ")
                if Option in Options:
                    if Option == Options[0] or Option == Options[1] or Option == Options[2]:
                        print("")
                        Price = int(input("Throw your auction! -- "))
                        if Price > Value:
                            Value = Price
                            print("------------------------------------------------")
                            print("Mr/Mrs " + Clients[i] + " raises the price to ", Value, "$")
                            print("------------------------------------------------")
                            Winner[0] = Clients[i]
                            Raises = Raises + 1
                        elif Price == Value or Price < Value:
                            print("The RAISE was invalid, so we automatically PASS Mr/Mrs " + Clients[i])
                            Price = 0
                            Passes = Passes + 1
                    else:
                       print("")
                       print("----------------------------------------")
                       print("Mr/Mrs " + Clients[i] + " goes for the pass!")
                       print("----------------------------------------")
                       Passes = Passes + 1
                       OptionError = OptionError + 1
                else:
                       OptionError = OptionError + 0
    print("")
    Round = Round + 1
    print("---------- And thats it for Round ", Round  ,"--------------")
    print("")
    if Passes > Raises:
        Sold = Sold - 1

print("")
print("---------------------------------------")
print(Product + " has been sold for ",Value,"$ to Mr/Mrs " + Winner.__str__().strip("['']") + " !")
print("---------------------------------------")
print("")

