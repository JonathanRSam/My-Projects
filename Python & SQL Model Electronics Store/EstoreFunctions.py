def Login():
    D={"Jonathan":"JSam","Dany":"DMJ","Advaith":"Adv"}
    username=input("Enter username: ")
    password=input("Enter password: ")
    if username not in D:
        print("Not a valid user")
    elif username=="admin":
        if D[username]==password:
            print("D")
    elif D[username]==password:
            print("Login successful")
            return True
    else:
        print("Invalid login")
        return False
    
    
    
    
def Modify():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',password="Jrs@030105",database='EStore')
    mycursor=mycon.cursor()
    
    j=0
    itno=input("Enter Item number of the required product: ")
    if itno[-1]=="A":
        cat="smartphone"
    elif itno[-1]=="B":
        cat="tv"
    elif itno[-1]=="C":
        cat="laptop"
    elif itno[-1]=="D":
        cat="keyboard"
    elif itno[-1]=="E":
        cat="mouse"
    else:
        j=1
    if j==0:
        sql="select item_no,brand,quantity,price from {} where item_no='{}';".format(cat,itno)
        mycursor.execute(sql)
        mydata=mycursor.fetchall()
        if mycursor.rowcount==0:
            print("Invalid Item Number")
        else:
            print("\n%1s%8s%1s%12s%1s%15s%1s%15s%1s"%("|","Item No","|","Brand","|","Quantity","|","Unit Price","|"))
            for x in mydata:
                print("%1s%8s%1s%12s%1s%15s%1s%15s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|"))
            print("\nModifying the Table: ")
            print("1. Price")
            print("2. Quantity")
            ch=int(input("Enter which one you would like to modify: "))
            if ch==1:
                p=float(input("Enter the new price of the product: "))
                sql="update {} set price={} where item_no='{}'".format(cat,p,itno)
                mycursor.execute(sql)
                mycon.commit()
                print("Product details modified successfully!")
            elif ch==2:
                q=int(input("Enter the new quantity of the product: "))
                sql="update {} set quantity={} where item_no='{}'".format(cat,q,itno)
                mycursor.execute(sql)
                mycon.commit()
                print("Product details modified successfully!")
            else:
                print("Invalid Option")
    else:
        print("Invalid Item number")
        


def ItemNo(cat):
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',password="Jrs@030105",database='EStore')
    mycursor=mycon.cursor()
    sql="select * from {}".format(cat)
    mycursor.execute(sql)
    mydata=mycursor.fetchall()
    t=mydata[-1][0]
    i=int(t[2])
    i+=1
    itno=t[0:2]+str(i)+t[3]
    return itno




def Add():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',password="Jrs@030105",database='EStore')
    mycursor=mycon.cursor()
    
    print("CATEGORIES:")
    print("-Smartphone")
    print("-TV")
    print("-Laptop")
    print("-Keyboard")
    print("-Mouse")
    cat=input("Name which category you wish to add a product to: ")
    if cat.lower() in ["smartphone","tv","laptop","keyboard","mouse"]:
        if cat.lower()=="smartphone":
            itno=ItemNo(cat)
            print("\nEnter required details to add product number",itno,)
            brand=input("Enter brand: ")
            size=float(input("Enter screen size(inches): "))
            camera=int(input("Enter camera quality(MP): "))
            storage=int(input("Enter storage(GB): "))
            OS=input("Enter Operating System: ")
            popularity=int(input("Enter popularity (1-3): "))
            price=float(input("Enter price: "))
            quantity=int(input("Enter quantity: "))
            sql="Insert into smartphone values('{}','{}',{},{},{},'{}',{},{},{})".format(itno,brand,size,camera,storage,OS,popularity,price,quantity)
            mycursor.execute(sql)
            mycon.commit()
            print("Product Added Successfully!")
                    
        elif cat.lower()=="tv":
            itno=ItemNo(cat)
            print("\nEnter required details to add product number",itno,)
            brand=input("Enter brand: ")
            size=int(input("Enter display size(inches): "))
            type=input("Enter display type: ")
            port=int(input("Enter number of ports: "))
            res=input("Enter resolution: ")
            popularity=int(input("Enter popularity (1-3): "))
            price=float(input("Enter price: "))
            quantity=int(input("Enter quantity: "))
            sql="Insert into TV Values('{}','{}',{},'{}',{},'{}',{},{},{})".format(itno,brand,size,type,port,res,popularity,price,quantity)
            mycursor.execute(sql)
            mycon.commit()
            print("Product Added Successfully!")
        
        elif cat.lower()=="laptop":
            itno=ItemNo(cat)
            print("\nEnter required details to add product number",itno,)
            brand=input("Enter brand: ")
            size=int(input("Enter screen size(inches): "))
            storage=input("Enter storage(specify GB or TB): ")
            RAM=int(input("Enter RAM (GB): "))
            popularity=int(input("Enter popularity (1-3): "))
            price=float(input("Enter price: "))
            quantity=int(input("Enter quantity: "))
            sql="Insert into laptop values('{}','{}',{},'{}',{},{},{},{})".format(itno,brand,size,storage,RAM,popularity,price,quantity)
            mycursor.execute(sql)
            mycon.commit()
            print("Product Added Successfully!")
                        
        elif cat.lower()=="keyboard":
            itno=ItemNo(cat)
            print("\nEnter required details to add product number",itno,)
            brand=input("Enter brand: ")
            size=int(input("Enter keyboard size(inches): "))
            switch=input("Enter type of switch: ")
            comp=input("Enter compatibility(Windows,Mac,Win and Mac): ")
            popularity=int(input("Enter popularity (1-3): "))
            price=float(input("Enter price: "))
            quantity=int(input("Enter quantity: "))
            sql="Insert into keyboard Values('{}','{}',{},'{}','{}',{},{},{})".format(itno,brand,size,switch,comp,popularity,price,quantity)
            mycursor.execute(sql)
            mycon.commit()
            print("Product Added Successfully!")
                            
        elif cat.lower()=="mouse":
            itno=ItemNo(cat)
            print("\nEnter required details to add product number",itno,)
            brand=input("Enter brand: ")
            connect=input("Enter mouse connectivity: ")
            weight=int(input("Enter weight(grams): "))
            DPI=int(input("Enter mouse DPI: "))
            popularity=int(input("Enter popularity (1-3): "))
            price=float(input("Enter price: "))
            quantity=int(input("Enter quantity: "))
            sql="Insert into mouse Values('{}','{}','{}',{},{},{},{},{})".format(itno,brand,connect,weight,DPI,popularity,price,quantity)
            mycursor.execute(sql)
            mycon.commit()
            print("Product Added Successfully!")
            
    else:
        print("Invalid category")
            
            
            
def Delete():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',password="Jrs@030105",database='EStore')
    mycursor=mycon.cursor()
    itno=input("Enter item number of product you wish to delete: ")
    j=0
    if itno[-1]=="A":
        cat="smartphone"
    elif itno[-1]=="B":
        cat="tv"
    elif itno[-1]=="C":
        cat="laptop"
    elif itno[-1]=="D":
        cat="keyboard"
    elif itno[-1]=="E":
        cat="mouse"
    else:
        j=1
    if j==0:
        sql="Select * from {} where item_no='{}'".format(cat,itno)
        mycursor.execute(sql)
        mydata=mycursor.fetchall()
        if mycursor.rowcount!=0:
            for x in mydata:
                print(x)
            SQL="Delete from {} where item_no='{}'".format(cat,itno)
            mycursor.execute(SQL)
            mycon.commit()
            print("Product Deleted Successfully")
        else:
            print("Invalid item number")
    else:
        print("Invalid Item number")
        
        
        
def purlog():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',password="Jrs@030105",database='EStore')
    mycursor=mycon.cursor()
    sql="select * from purlog;"
    mycursor.execute(sql)
    mydata=mycursor.fetchall()
    if mycursor.rowcount!=0:
        print("                                      \033[4mPURCHASE LOG\033[0m")
        print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%16s%1s%16s%1s"%("|","Item No","|","Brand","|","Price","|","Quantity","|","Date of Purchase","|","Time of Purchase","|"))
        for x in mydata:
            print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%16s%1s%16s%1s"%("|",x[0],"|",x[1],"|",x[3],"|",x[2],"|",x[4],"|",x[5],"|"))
            
    else:
        print("Purchase Log Empty")        
        
        
        
        
        
def DOTD():
    import mysql.connector,random,pickle
    mycon=mysql.connector.connect(host='localhost',user='root',password="Jrs@030105",database='EStore')
    mycursor=mycon.cursor()
    
    
    fin=open("DOTD.dat","rb")
    T=pickle.load(fin)
    cat=pickle.load(fin)
    if len(T)!=0:
        sql="update {} set price={} where item_no='{}'".format(cat,T[-2],T[0])
        mycursor.execute(sql)
        mycon.commit()
    
    
    Lcat=["Smartphone","TV","Laptop","Keyboard","Mouse"]
    cat=Lcat[random.randint(0,4)]
    sql="select * from {}".format(cat)
    mycursor.execute(sql)
    mydata=mycursor.fetchall()
    no=int(mydata[-1][0][2])
    rand=random.randint(1,no)
    for x in mydata:
        if int(x[0][2])==rand:
            item=x
    fout=open("DOTD.dat","wb")
    pickle.dump(item,fout)
    pickle.dump(cat,fout)
    fout.close()
    price=50/100*item[-2]
    sql="update {} set price={} where item_no='{}'".format(cat,price,item[0])
    mycursor.execute(sql)
    mycon.commit()
    print("\n******************************************************")
    print("                  \033[4mDEAL OF THE DAY\033[0m !!")
    print("          ",item[1],cat,"is on a 50% SALE")
    print("                    Was",item[-2],"$")
    print("                    Now",price,"$")
    print("-- For more product Details View Item number",item[0],"--")
    print("******************************************************")
    
    


def browcat(emp):
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',password="Jrs@030105",database='EStore') 
    mycursor=mycon.cursor()
    print("\n1:Smartphone")
    print("2:Tv")
    print("3:Laptop")
    print("4:Keyboard")
    print("5:Mouse")
    n=int(input("enter category no of item you wish to see: "))
    if n==1:
        sql="select * from smartphone;"
        mycursor.execute(sql)
        mydata=mycursor.fetchall()
        if emp==0:
            print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%15s%1s%10s%1s"%("|","Item No","|","brand","|","screen size","|","camera quality","|","storage","|","os","|","price","|"))
            for x in mydata:
                print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%15s%1s%10s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[5],"|",x[7],"|"))
        else:
            print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%15s%1s%10s%1s%10s%1s%12s%1s"%("|","Item No","|","brand","|","screen size","|","camera quality","|","storage","|","os","|","price","|","Quantity","|","Popularity","|"))
            for x in mydata:
                print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%15s%1s%10s%1s%10s%1s%12s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[5],"|",x[7],"|",x[8],"|",x[6],"|"))
    elif n==2:    
        sql="select * from tv;"
        mycursor.execute(sql)
        mydata=mycursor.fetchall()
        if emp==0:
            print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%18s%1s%10s%1s"%("|","Item No","|","brand","|","display size","|","display type","|","no of ports","|","image resolution","|","price","|"))
            for x in mydata:
                print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%18s%1s%10s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[5],"|",x[7],"|"))
        else:
            print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%18s%1s%10s%1s%10s%1s%12s%1s"%("|","Item No","|","brand","|","display size","|","display type","|","no of ports","|","image resolution","|","price","|","Quantity","|","Popularity","|"))
            for x in mydata:
                print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%18s%1s%10s%1s%10s%1s%12s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[5],"|",x[7],"|",x[8],"|",x[6],"|"))
    elif n==3:
        sql="select * from laptop;"
        mycursor.execute(sql)
        mydata=mycursor.fetchall()
        if emp==0:
            print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%15s%1s"%("|","Item No","|","brand","|","screen size","|","storage","|","ram","|","price","|"))
            for x in mydata:
                print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%15s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[6],"|"))
        else:
            print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%10s%1s%10s%1s%12s%1s"%("|","Item No","|","brand","|","screen size","|","storage","|","ram","|","price","|","Quantity","|","Popularity","|"))
            for x in mydata:
                print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%10s%1s%10s%1s%12s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[6],"|",x[7],"|",x[5],"|"))
    elif n==4:
        sql="select * from keyboard;"
        mycursor.execute(sql)
        mydata=mycursor.fetchall()
        if emp==0:
            print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%15s%1s"%("|","Item No","|","brand","|","keyboard size","|","switch","|","compatibility","|","price","|"))
            for x in mydata:
                print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%15s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[6],"|"))
        else:
            print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%10s%1s%10s%1s%12s%1s"%("|","Item No","|","brand","|","keyboard size","|","switch","|","compatibility","|","price","|","Quantity","|","Popularity","|"))
            for x in mydata:
                print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%10s%1s%10s%1s%12s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[6],"|",x[7],"|",x[5],"|"))
    elif n==5:
        sql="select * from mouse;"
        mycursor.execute(sql)
        mydata=mycursor.fetchall()
        if emp==0:
            print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%15s%1s"%("|","Item No","|","brand","|","connectivity","|","weight","|","dpi","|","price","|"))
            for x in mydata:
                print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%15s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[6],"|"))
        else:
            print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%10s%1s%10s%1s%12s%1s"%("|","Item No","|","brand","|","connectivity","|","weight","|","dpi","|","price","|","Quantity","|","Popularity","|"))
            for x in mydata:
                print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%10s%1s%10s%1s%12s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[6],"|",x[7],"|",x[5],"|"))
    else:
        print("Invalid Option")


    
    
def AsDs():
    print()
    print("1. Highest to Lowest")
    print("2. Lowest to Highest")
    ans=int(input("Which would you prefer: "))
    if ans==1:
        return "desc"
    else:
        return ""
    
def Sort():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',password="Jrs@030105",database='EStore')
    mycursor=mycon.cursor()
    
    print("CATEGORIES:")
    print("-Smartphone")
    print("-TV")
    print("-Laptop")
    print("-Keyboard")
    print("-Mouse")
    j=0
    cat=input("Name the category of product you wish to sort: ")
    if cat.lower()=="smartphone":
        a,b,c,d=",screen_size",",camera_quality",",storage","OS"
        A,B,C="Size(inches)","Camera(MP)","Storage(GB)"
    elif cat.lower()=="tv":
        a,b,c,d=",display_size",",display_type",",Ports",",resolution"
        A,B,C="Size(inches)","Display type","Ports"
    elif cat.lower()=="laptop":
        a,b,c,d=",screen_size",",storage",",RAM",""
        A,B,C="Size(inches)","Storage","RAM (GB)"
    elif cat.lower()=="keyboard":
        a,b,c,d=",keyboard_size",",switch",",Compatibility",""
        A,B,C="Size(inches)","Switch Type","Compatibility"
    elif cat.lower()=="mouse":
        a,b,c,d=",connectivity",",weight",",DPI",""
        A,B,C="Connectivity","Weight(grams)","Mouse DPI"
    else:
        print("Invalid category")
        j=1
    
    
    if j==0:    
        temp=pr=pop=0
        stack=[]
        while True:
            print("\nSort By: ")
            if pop==0:
                print("1. Popularity")
            if pr==0:
                print("2. Price")
            print("3. Continue")
            ch=int(input("Enter your choice: "))
            if ch==1 and pop==0:
                temp+=1
                pop=1
                stack.append("popularity")
                stack.append(AsDs())
                
            elif ch==2 and pr==0:
                pr=1
                temp+=1
                stack.append("price")
                stack.append(AsDs())
                
            elif ch==3:
                print()
                if temp==0:
                    print("Insufficient data!")    
                
                elif temp<2:
                    I,II=stack
                    sql="select item_no ,brand {} {} {} {} ,price from {} order by {} {}".format(a,b,c,d,cat,I,II)
                    mycursor.execute(sql)
                    mydata=mycursor.fetchall()
                    print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|","Item No","|","Brand","|",A,"|",B,"|",C,"|","Price($)","|"))
                    for x in mydata:
                        print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[-1],"|"))
                
                else:
                    I,II,III,IV=stack
                    sql="select item_no ,brand {} {} {} {} ,price from {} order by {} {} , {} {}".format(a,b,c,d,cat,I,II,III,IV)
                    mycursor.execute(sql)
                    mydata=mycursor.fetchall()
                    print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|","Item No","|","Brand","|",A,"|",B,"|",C,"|","Price($)","|"))
                    for x in mydata:
                        print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[-1],"|"))
                break
            else:
                print("Invalid option. Please Try again!")
                
                
                
                
                
                
                
def Search():
        import mysql.connector
        mycon=mysql.connector.connect(host='localhost',user='root',password="Jrs@030105",database='EStore')
        mycursor=mycon.cursor()
        print("Search Tab:")
        print("1. View a specific item: ")
        print("2. Filter Items to find What you're looking for")
        ch=int(input("Enter your choice: "))
        print()
        if ch==1:
            itno=input("Enter item number of product you wish to view: ")
            if itno[-1]=="A":
                sql="SELECT * FROM Smartphone WHERE ITEM_NO='{}'".format(itno)
                mycursor.execute(sql)
                mydata=mycursor.fetchall()
                if mycursor.rowcount==0:
                    print("Invalid Item number")
                else:
                    print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|","Item No","|","Phone Brand","|","Size(inches)","|","Camera(MP)","|","Storage(GB)","|","Price($)","|"))
                    for x in mydata:
                        print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[-2],"|"))
            
            elif itno[-1]=="B":
                sql="SELECT * FROM TV WHERE ITEM_NO='{}'".format(itno)
                mycursor.execute(sql)
                mydata=mycursor.fetchall()
                if mycursor.rowcount==0:
                    print("Invalid Item number")
                else:
                    print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|","Item No","|","TV Brand","|","Size(inches)","|","Display type","|","Ports","|","Price($)","|"))
                    for x in mydata:
                        print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[-2],"|"))
            
            elif itno[-1]=="C":
                sql="SELECT * FROM Laptop WHERE ITEM_NO='{}'".format(itno)
                mycursor.execute(sql)
                mydata=mycursor.fetchall()
                if mycursor.rowcount==0:
                    print("Invalid Item number")
                else:
                    print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|","Item No","|","Laptop Brand","|","Size(inches)","|","Storage","|","RAM (GB)","|","Price($)","|"))
                    for x in mydata:
                        print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[-2],"|"))
                        
            elif itno[-1]=="D":
                sql="SELECT * FROM Keyboard WHERE ITEM_NO='{}'".format(itno)
                mycursor.execute(sql)
                mydata=mycursor.fetchall()
                if mycursor.rowcount==0:
                    print("Invalid Item number")
                else:
                    print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|","Item No","|","Keybd Brand","|","Size(inches)","|","Switch Type","|","Compatibility","|","Price($)","|"))
                    for x in mydata:
                        print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[-2],"|"))
                    
            elif itno[-1]=="E":
                sql="SELECT * FROM Mouse WHERE ITEM_NO='{}'".format(itno)
                mycursor.execute(sql)
                mydata=mycursor.fetchall()
                if mycursor.rowcount==0:
                    print("Invalid Item number")
                else:
                    print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|","Item No","|","Mouse Brand","|","Connectivity","|","Weight(grams)","|","Mouse DPI","|","Price($)","|"))
                    for x in mydata:
                        print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[-2],"|"))
            else:
                print("Invalid item number")
        
        
        
        
        elif ch==2:
            print("CATEGORIES:")
            print("-Smartphone")
            print("-TV")
            print("-Laptop")
            print("-Keyboard")
            print("-Mouse")
            cat=input("Name the category of product you wish to filter: ")
            if cat.lower() in ["smartphone","tv","laptop","keyboard","mouse"]:
                sql=("SELECT * FROM {}".format(cat))
                mycursor.execute(sql)
                L=mycursor.fetchall()
                print()
                if cat.lower()=="smartphone":
                    while True:
                        print("Choose the specifications you require: ")
                        print("1. Screen Size")
                        print("2. Camera Quality")
                        print("3. Storage")
                        print("4. Operating system")
                        print("5. Continue")
                        ans=int(input("What particular specifications are you looking for: "))
                        if ans==1:
                            screen=float(input("Screen size in inches:- 6.1 , 6.3 , 6.4 : "))
                            T=[]
                            for x in range(0,len(L)):
                                if L[x][2]!=screen:
                                    T.append(L[x])
                            for x in T:
                                L.remove(x)
                        elif ans==2:
                            camera=int(input("Camera quality in Megapixels:- 12 , 16, 64 : "))
                            T=[]
                            for x in range(0,len(L)):
                                if L[x][3]!=camera:
                                    T.append(L[x])
                            for x in T:
                                L.remove(x)
                        elif ans==3:
                            store=int(input("Storage space in Gigabytes:- 32 , 64, 128 , 256 : "))
                            T=[]
                            for x in range(0,len(L)):
                                if L[x][4]!=store:
                                    T.append(L[x])
                            for x in T:
                                L.remove(x)
                        elif ans==4:
                            os=input("Operating System:- IOS , Android : ")
                            T=[]
                            for x in range(0,len(L)):
                                if L[x][5].lower()!=os.lower():
                                    T.append(L[x])
                            for x in T:
                                L.remove(x)
                        elif ans==5:
                            print()
                            if len(L)==0:
                                print("Sorry but we currently do not have exactly what you are looking for")
                            else:
                                print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|","Item No","|","Phone Brand","|","Size(inches)","|","Camera(MP)","|","Storage(GB)","|","Price($)","|"))
                                for x in L:
                                    print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[-2],"|"))
                                
                            break
                        else:
                            print("Invalid Option. Please try Again!")
                        
                
                
                elif cat.lower()=="tv":
                    while True:
                        print("Choose the specifications you require: ")
                        print("1. Display Size")
                        print("2. Display Type")
                        print("3. Number of Ports")
                        print("4. Resolution")
                        print("5. Continue")
                        ans=int(input("What particular specifications are you looking for: "))
                        if ans==1:
                            size=int(input("Display size in inches:- 46 , 55 , 65 : "))
                            T=[]
                            for x in range(0,len(L)):
                                if L[x][2]!=size:
                                    T.append(L[x])
                            for x in T:
                                L.remove(x)
                        elif ans==2:
                            type=input("Type of Display:- LCD , LED , QLED : ")
                            T=[]
                            for x in range(0,len(L)):
                                if L[x][3].lower()!=type.lower():
                                    T.append(L[x])
                            for x in T:
                                L.remove(x)
                        elif ans==3:
                            port=int(input("Number of ports:- 2 , 5 , 8 : "))
                            T=[]
                            for x in range(0,len(L)):
                                if L[x][4]!=port:
                                    T.append(L[x])
                            for x in T:
                                L.remove(x)
                        elif ans==4:
                            res=input("Video Resolution:- 1080P , 4K : ")
                            T=[]
                            for x in range(0,len(L)):
                                if L[x][5].lower()!=res.lower():
                                    T.append(L[x])
                            for x in T:
                                L.remove(x)
                        elif ans==5:
                            print()
                            if len(L)==0:
                                print("Sorry but we currently do not have exactly what you are looking for")
                            else:
                                print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|","Item No","|","TV Brand","|","Size(inches)","|","Display type","|","Ports","|","Price($)","|"))
                                for x in L:
                                    print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[-2],"|"))
                            break
                        else:
                            print("Invalid Option. Please try Again!")
                
                
                
                elif cat.lower()=="laptop":
                    while True:
                        print("Choose the specifications you require: ")
                        print("1. Screen Size")
                        print("2. Storage Space")
                        print("3. RAM")
                        print("4. Continue")
                        ans=int(input("What particular specifications are you looking for: "))
                        if ans==1:
                            size=int(input("Screen size in inches:- 12 , 14 , 15 : "))
                            T=[]
                            for x in range(0,len(L)):
                                if L[x][2]!=size:
                                    T.append(L[x])
                            for x in T:
                                L.remove(x)
                        elif ans==2:
                            store=input("Total Internal Storage:- 500GB , 1TB , 1.5TB : ")
                            T=[]
                            for x in range(0,len(L)):
                                if L[x][3].lower()!=store.lower():
                                    T.append(L[x])
                            for x in T:
                                L.remove(x)
                        elif ans==3:
                            ram=int(input("Total Built in RAM:- 16 , 32 , 64 : "))
                            T=[]
                            for x in range(0,len(L)):
                                if L[x][4]!=ram:
                                    T.append(L[x])
                            for x in T:
                                L.remove(x)
                        elif ans==4:
                            print()
                            if len(L)==0:
                                print("Sorry but we currently do not have exactly what you are looking for")
                            else:
                                print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|","Item No","|","Laptop Brand","|","Size(inches)","|","Storage","|","RAM (GB)","|","Price($)","|"))
                                for x in L:
                                    print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[-2],"|"))
                            break
                        else:
                            print("Invalid Option. Please try Again!")
               
                        
               
                
                elif cat.lower()=="keyboard":
                    while True:
                        print("Choose the specifications you require: ")
                        print("1. Keyboard Size")
                        print("2. Type of Switch")
                        print("3. Compatibility")
                        print("4. Continue")
                        ans=int(input("What particular specifications are you looking for: "))
                        if ans==1:
                            size=int(input("Screen size in inches:- 14 , 15 , 19 : "))
                            T=[]
                            for x in range(0,len(L)):
                                if L[x][2]!=size:
                                    T.append(L[x])
                            for x in T:
                                L.remove(x)
                        elif ans==2:
                            switch=input("Keyboard switch type:- Blue Cherry , Red Cherry , Hybrid Blue : ")
                            T=[]
                            for x in range(0,len(L)):
                                if L[x][3].lower()!=switch.lower():
                                    T.append(L[x])
                            for x in T:
                                L.remove(x)
                        elif ans==3:
                            comp=input("Operating System Compatibility: Windows , Mac , Win and Mac : ")
                            T=[]
                            for x in range(0,len(L)):
                                if L[x][4].lower()!=comp.lower():
                                    T.append(L[x])
                            for x in T:
                                L.remove(x)
                        elif ans==4:
                            print()
                            if len(L)==0:
                                print("Sorry but we currently do not have exactly what you are looking for")
                            else:
                                print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|","Item No","|","Keybd Brand","|","Size(inches)","|","Switch Type","|","Compatibility","|","Price($)","|"))
                                for x in L:
                                    print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[-2],"|"))
                            break
                        else:
                            print("Invalid Option. Please try Again!")
                
                
                
                
                elif cat.lower()=="mouse":
                    while True:
                        print("Choose the specifications you require: ")
                        print("1. Connectivity")
                        print("2. Weight")
                        print("3. DPI")
                        print("4. Continue")
                        ans=int(input("What particular specifications are you looking for: "))
                        if ans==1:
                            connect=input("Mode of Connectivity:- Wired USB , Wireless USB , Bluetooth : ")
                            T=[]
                            for x in range(0,len(L)):
                                if L[x][2].lower()!=connect.lower():
                                    T.append(L[x])
                            for x in T:
                                L.remove(x)
                        elif ans==2:
                            weight=int(input("Weight of mouse in grams:- 100 , 115 , 120 : "))
                            T=[]
                            for x in range(0,len    (L)):
                                if L[x][3]!=weight:
                                    T.append(L[x])
                            for x in T:
                                L.remove(x)
                        elif ans==3:
                            dpi=int(input("Mouse DPI:- 1000 , 1200 , 1600 : "))
                            T=[]
                            for x in range(0,len(L)):
                                if L[x][4]!=dpi:
                                    T.append(L[x])
                            for x in T:
                                L.remove(x)
                        elif ans==4:
                            print()
                            if len(L)==0:
                                print("Sorry but we currently do not have exactly what you are looking for")
                            else:
                                print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|","Item No","|","Mouse Brand","|","Connectivity","|","Weight(grams)","|","Mouse DPI","|","Price($)","|"))
                                for x in L:
                                    print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s%12s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|",x[-2],"|"))
                            break
                        else:
                            print("Invalid Option. Please try Again!")
                
            else:
                print("Invalid Category. Please Try again")
        else:
            print("Invalid choice")
                
                
                
                
mycart=[]


def Buy():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',password="Jrs@030105",database='EStore')
    mycursor=mycon.cursor()
    
    itno=input("Enter item number of product you wish to buy: ")
    j=0
    if itno[-1]=="A":
        cat="smartphone"
        j=1
    elif itno[-1]=="B":
        cat="tv"
        j=1
    elif itno[-1]=="C":
        cat="laptop"
        j=1
    elif itno[-1]=="D":
        cat="keyboard"
        j=1
    elif itno[-1]=="E":
        cat="mouse"
        j=1
    if j==1:
        sql="select item_no,brand,price from {} where item_no='{}';".format(cat,itno)
        mycursor.execute(sql)
        mydata=mycursor.fetchall()
        if mycursor.rowcount==0:
            print("Invalid Item Number")
        else:
            SQL="select price,quantity from {} where item_no='{}'".format(cat,itno)
            mycursor.execute(SQL)
            MYDATA=mycursor.fetchall()
            q=int(input("How many units would you like: "))
            
            if MYDATA[0][-1]>=q:
                current=MYDATA[0][-1]
                stock=MYDATA[0][1]-q
                for x in range (len(mycart)):
                    if mycart[x][0]==mydata[0][0]:
                        stock=stock-mycart[x][2]
                        current=current-mycart[x][2]
                if stock<0:
                    print("Sorry there are",current,"more unit(s) left of this product")
                else:   
                    print("Would you like to add",q,"unit(s) of the below",cat,"to your cart: \n",mydata)
                    ch=input("Y/N: ")
                    if ch.lower()=="y":
                        Q=MYDATA[0][1]-q
                        T=(mydata[0][0],mydata[0][1],q,MYDATA[0][0],MYDATA[0][0]*q,cat,Q)
                        mycart.append(T)
                        print()
            else:
                if MYDATA[0][-1]==0:
                    print("Sorry that Item is currently out of Stock")
                else:
                    print("Sorry we only have",MYDATA[0][-1],"more unit(s) of this product")
    else:
        print("Invalid Item number")
                
      
                

                
def MyCart():
    import mysql.connector,datetime
    mycon=mysql.connector.connect(host='localhost',user='root',password="Jrs@030105",database='EStore')
    mycursor=mycon.cursor()
    
    while True:
        if mycart==[]:
            print("No Items in Cart")
            break
        print("%40s"%("\033[4mMY CART\033[0m"))
        print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s"%("|","Item No","|","Brand","|","Quantity","|","Unit Price","|","Ammount","|"))
        for x in mycart:
            print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|"))
        print()
        print("1. Add more items to cart") 
        print("2. Remove an item from cart")
        print("3. Confirm purchase")
        print("4. Continue shopping")
        ch=int(input("Enter your choice: "))
        if ch==1:
            Buy()
        elif ch==2:
            itno=input("Enter item number of product you wish to remove: ")
            i=0
            for x in range(0,len(mycart)):
                if mycart[x][0]==itno:
                    t=mycart[x]
                    i=1
            if i==1:
                mycart.remove(t)
                print()
            else:
                print("Item Is not in Cart\n")
        elif ch==3:
            print()
            
            datetime=datetime.datetime.now()
            datetime=str(datetime)
            date=datetime[0:10]
            time=datetime[11:19]
            
            for x in mycart:
                sql="update {} set quantity={} where item_no='{}';".format(x[5],x[6],x[0])
                mycursor.execute(sql)
                mycon.commit()
            Bill=0
            for x in mycart:
                Bill+=x[4]
            print("%40s"%("\033[4mReceipt\033[0m"))
            print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s"%("|","Item No","|","Brand","|","Quantity","|","Unit Price","|","Ammount","|"))
            for x in mycart:
                print("%1s%8s%1s%12s%1s%15s%1s%15s%1s%15s%1s"%("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|",x[4],"|"))
                sql="INSERT INTO purlog VALUES('{}','{}',{},{},'{}','{}')".format(x[0],x[1],x[2],x[3],date,time)
                mycursor.execute(sql)
                mycon.commit()   
            print("                      \033[4mFinal Bill\033[0m: ",Bill,"$")
            mycart.clear()
            
            break
        elif ch==4:
            break
        else:
            print("Invalid option! Please Try Again")
            break
                                       