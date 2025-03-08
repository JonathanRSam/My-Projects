from EstoreFunctions import *
print("+===============================+\n|      ------ .----. --.        |\n|         |   |    | |  \       |\n|         |   |----| |   |      |\n|         |   |    | |  /       |\n|      ---'   '    ' --'        |\n| \x1B[3mTHE ONLINE ELECTRONICS STORE\x1B[0m  |\n|                               |\n+-------------------------------+\n|    \x1B[3mDone By\x1B[0m:                   |\n|       Jonathan, Advaith, Dany |\n+===============================+\n")
start=input("       Press Enter To Begin")
print("\nDo you wish to access The store as:")
print("1. Customer")
print("2. Employee/Admin")
ans=int(input("Enter your choice: "))
if ans==2:
    if Login():
        while True:
            print("\nMAIN MENU")
            print("1. View Items of a Category")
            print("2. Add a new item")
            print("3. Modify details of an existing item")
            print("4. Delete an existing item")
            print("5. View Purchase Log")
            print("6. Exit")
            ch=int(input("Enter your choice: "))
            if ch==1:
                browcat(1)
            elif ch==2:
                Add()
            elif ch==3:
                Modify()
            elif ch==4:
                Delete()
            elif ch==5:
                purlog()
            elif ch==6:
                print("Program Over")
                break
            else:
                print("Invalid Choice! Please Try again")

elif ans==1:
    DOTD()
    while True:
        print("\nMAIN MENU")
        print("1. Browse Categories")
        print("2. Sort Items in a Category")
        print("3. Search for item/ Filter Items")
        print("4. Buy an Item")
        print("5. View Your Cart")
        print("6. Finish Shopping")
        ch=int(input("Enter your choice: "))
        if ch==1:
            browcat(0)
        elif ch==2:
            Sort()
        elif ch==3:
            Search()
        elif ch==4:
            Buy()
        elif ch==5:
            MyCart()
        elif ch==6:
            if len(mycart)!=0:
                Y=input("Purchase Items before leaving? (Y/N): ")
                if Y.lower()=="y":
                    MyCart()
                else:
                    print("Thanks for visiting. Program Over")
                    break
            else:
                print("Thanks for visiting. Program Over")
                break
        else:
            print("Invalid Option! Please Try again")
else:
    print("Sorry thats not a valid Option")
            
