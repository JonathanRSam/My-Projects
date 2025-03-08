import random
a=b=c=d=e=f=g=h=i="-"

#Displaying the board
def PrintBoard(G):
    if G==0:
        print()
        print(" ",a ,"|" ,b ,"|" ,c,"                 ","a" ,"|" ,"b" ,"|" ,"c")
        print(" ---+---+---","               ","---+---+---")
        print(" ",d ,"|" ,e ,"|" ,f,"                 ","d" ,"|" ,"e" ,"|" ,"f")
        print(" ---+---+---","               ","---+---+---")
        print(" ",g ,"|" ,h ,"|" ,i,"                 ","g" ,"|" ,"h" ,"|" ,"i")
        print()
    else:
        print()
        print(" ",a ,"|" ,b ,"|" ,c)
        print(" ---+---+---")
        print(" ",d ,"|" ,e ,"|" ,f)
        print(" ---+---+---")
        print(" ",g ,"|" ,h ,"|" ,i)
        print()


#Checking if X or O can win
def Check_Win(Y):
    global a,b,c,d,e,f,g,h,i
    if a==b==Y and c=="-":
        c="O"
        return False
    elif b==c==Y and a=="-":
        a="O"
        return False
    elif a==c==Y and b=="-":
        b="O"
        return False
    elif d==e==Y and f=="-":
        f="O"
        return False
    elif e==f==Y and d=="-":
        d="O"
        return False
    elif d==f==Y and e=="-":
        e="O"
        return False
    elif g==h==Y and i=="-":
        i="O"
        return False
    elif h==i==Y and g=="-":
        g="O"
        return False
    elif g==i==Y and h=="-":
        h="O"
        return False
    
    elif a==d==Y and g=="-":
        g="O"
        return False
    elif d==g==Y and a=="-":
        a="O"
        return False
    elif a==g==Y and d=="-":
        d="O"
        return False
    elif b==e==Y and h=="-":
        h="O"
        return False
    elif e==h==Y and b=="-":
        b="O"
        return False
    elif b==h==Y and e=="-":
        e="O"
        return False
    elif c==f==Y and i=="-":
        i="O"
        return False
    elif f==i==Y and c=="-":
        c="O"
        return False
    elif c==i==Y and f=="-":
        f="O" 
        return False
    
    elif a==e==Y and i=="-":
        i="O"
        return False
    elif e==i==Y and a=="-":
        a="O"
        return False
    elif a==i==Y and e=="-":
        e="O"
        return False
    elif c==e==Y and g=="-":
        g="O" 
        return False
    elif e==g==Y and c=="-":
        c="O"
        return False
    elif c==g==Y and e=="-":
        e="O"
        return False
    
    else:
        return True


#Playing a random available move
def Random():
    global a,b,c,d,e,f,g,h,i
    t=0
    while t==0:
        o=random.randint(1,9)
        if o==1 and a=="-":
            a="O"
            t=1
        elif o==2 and b=="-":
            b="O"
            t=1
        elif o==3 and c=="-":
            c="O"
            t=1
        elif o==4 and d=="-":
            d="O"
            t=1
        elif o==5 and e=="-":
            e="O"
            t=1
        elif o==6 and f=="-":
            f="O"
            t=1
        elif o==7 and g=="-":
            g="O"
            t=1
        elif o==8 and h=="-":
            h="O"
            t=1
        elif o==9 and i=="-":
            i="O"
            t=1

def Defend():
    print("\nUse the characters shown on the right side grid to play each move")
    global a,b,c,d,e,f,g,h,i
    turn=0
    first=""
    while True:
        PrintBoard(0)
        #Users move
        valid=True
        m=input("Enter your move: ")
        if m=="a" and a=="-":
            a="X"
        elif m=="b" and b=="-":
            b="X"
        elif m=="c" and c=="-":
            c="X"
        elif m=="d" and d=="-":
            d="X"
        elif m=="e" and e=="-":
            e="X"
        elif m=="f" and f=="-":
            f="X"
        elif m=="g" and g=="-":
            g="X"
        elif m=="h" and h=="-":
            h="X"
        elif m=="i" and i=="-":
            i="X"
        else:
            print("Invalid move. Try Again")
            valid=False
        
        #Checking if X won
        if a==b==c!="-" or d==e==f!="-" or g==h==i!="-" or a==d==g!="-" or b==e==h!="-" or c==f==i!="-" or a==e==i!="-" or c==e==g!="-":
            PrintBoard(1)
            print("You Win!")
            break
        
        #Checking if game over as draw
        if valid:
            turn+=1
        if turn==5:
            PrintBoard(1)
            print("Draw! Game Over")
            break
        if turn==1 and valid:
            first=m
        elif turn==2 and valid:
            second=m        
        
        #Counter play algorithm if user starts centre
        if first=="e" and valid:
            #Move1
            if turn==1:
                o=random.choice([1,3,7,9])
                if o==1 and a=="-":
                    a="O"
                    Ist="a"
                elif o==3 and c=="-":
                    c="O"
                    Ist="c"
                elif o==7 and g=="-":
                    g="O"
                    Ist="g"
                elif o==9 and i=="-":
                    i="O"
                    Ist="i"
            #Move2
            elif turn==2 and Check_Win("X"):
                L=["a","c","g","i"]
                L.remove(Ist)
                L.remove(second)
                o=random.choice(L)
                if o=="a":
                    a="O"
                elif o=="c":
                    c="O"
                elif o=="g":
                    g="O"
                elif o=="i":
                    i="O"        
            #Move3
            elif turn==3 and Check_Win("O"):
                if Check_Win("X"):
                    Random()        
            #Move 4
            elif turn==4 and Check_Win("O"):
                if random.randint(1,2)==1:
                    Random()
                else:
                    if Check_Win("X"):
                        Random()
        
        
        #Counter play agorithm if user starts corner
        if first in "acgi" and valid:
            #Move1
            if turn==1:
                e="O"
                Ist="e"        
            #Move2
            elif turn==2 and Check_Win("X"):
                t=0
                while t==0:
                    o=random.choice([2,4,6,8])
                    if o==2 and b=="-":
                        b="O"
                        t=1
                    elif o==4 and d=="-":
                        d="O"
                        t=1
                    elif o==6 and f=="-":
                        f="O"
                        t=1
                    elif o==8 and h=="-":
                        h="O"
                        t=1        
            #Move3
            elif turn==3 and Check_Win("O"):
                if Check_Win("X"):
                    Random()        
            #Move4
            elif turn==4 and Check_Win("O"):
                if random.randint(1,2)==1:
                    Random()
                else:
                    if Check_Win("X"):
                        Random()
            
        
        #Counter play agorithm if user starts side
        if first in "bdfh" and valid:
            #Move1
            if turn==1:
                D={"b":["a","c"],"d":["g","a"],"f":["c","i"],"h":["i","g"]}
                o=random.choice(D[first])
                if o=="a":
                    a="O"
                    Ist="a"
                elif o=="c":
                    c="O"
                    Ist="c"
                elif o=="g":
                    g="O"
                    Ist="g"
                elif o=="i":
                    i="O"
                    Ist="i"        
            #Move2
            elif turn==2 and Check_Win("X"):
                e="O"            
            #Move3
            elif turn==3 and Check_Win("O"):
                if Check_Win("X"):
                    Random()       
            #Move4
            elif turn==4 and Check_Win("O"):
                if random.randint(1,2)==1:
                    Random()
                else:
                    if Check_Win("X"):
                        Random()
                    
                    
        #Checking if O won        
        if a==b==c!="-" or d==e==f!="-" or g==h==i!="-" or a==d==g!="-" or b==e==h!="-" or c==f==i!="-" or a==e==i!="-" or c==e==g!="-":
            PrintBoard(1)
            print("You Lost! Maybe Next time")
            break




def Attack(r):
    print("\nUse the characters shown on the right side grid to play each move")
    global a,b,c,d,e,f,g,h,i
    opposite=True
    side=True
    valid=True
    turn=0
    first=""
    second=""
    
    #Choosing random moveset
    while True:  
        if valid:
            turn+=1
        
        #Attacking Algorithm starting with centre (41%)
        if r%3==0 and valid:
            #Move1
            if turn==1:
                e="O"
                Ist="e"
            
            #Counterplay if X plays side
            if turn>1 and first in "bdfh":
                #Move2(I)
                if turn==2:
                    o=random.choice([1,3,7,9])
                    if o==1:
                        a="O"
                    elif o==3:
                        c="O"
                    elif o==7:
                        g="O"
                    else:
                        i="O"
                #Move3(I)
                elif turn==3 and Check_Win("O"):
                    if Check_Win("X"):
                        if d==a==b=="-":
                            a="O"
                        elif b==c==f=="-":
                            c="O"
                        elif d==g==h=="-":
                            g="O"
                        else:
                            i="O"
                #Move4(I)
                elif turn==4:
                    Check_Win("O")
            
            #Counterplay if X plays corner
            else:
                #Move2(II)
                if turn==2:
                    if first=="a":
                        i="O"
                        IInd="i"
                    elif first=="c":
                        g="O"
                        IInd="g"
                    elif first=="g":
                        c="O"
                        IInd="c"
                    else:
                        a="O"
                        IInd="a"
                #Move3(II)
                elif turn==3 and Check_Win("X"):
                    if d==a==b=="-":
                        a="O"
                    elif b==c==f=="-":
                        c="O"
                    elif d==g==h=="-":
                        g="O"
                    else:
                        i="O"
                
                #Draw game if X plays 2nd move corner
                if turn>3 and second in "acgi":
                    #Move4(II)(a)
                    if turn==4 and Check_Win("O"):
                        Random()
                    #Move5(II)(a)
                    elif turn==5 and Check_Win("O"):
                        Random()
                #Winning game if X plays anything else
                else:
                    #Move4(II)(b)
                    if turn==4:
                        Check_Win("O")
                    
       
        
        #Attacking Algorithm starting with corner (36%)
        elif r%2==0 and valid:
            #Move1
            if turn==1:
                m=random.choice(["a","c","g","i"])
                if m=="a":
                    a="O"
                elif m=="c":
                    c="O"
                elif m=="g":
                    g="O"
                else:
                    i="O"
                Ist=m
            
            #Counterplay if X plays side (O Wins)
            elif turn>1 and first in "bdfh":
                #Move2(I)
                if turn==2:
                    e="O"
                    IInd="O"
                #Move3(I)
                elif turn==3 and Check_Win("O"):
                    if Check_Win("X"):
                       if d==a==b=="-":
                           a="O"
                       elif b==c==f=="-":
                           c="O"
                       elif d==g==h=="-":
                           g="O"
                       else:
                           i="O"
                #Move4(I)
                elif turn==4:
                    Check_Win("O")
            
            #Counterplay if X plays corner (O Wins)
            elif turn>1 and first in "acgi":
                #Moves2-4(II)
                t=0
                while t==0:
                    m=random.randint(1,4)
                    if m==1 and a=="-":
                        a="O"
                        t=1
                    elif m==2 and c=="-":
                        c="O"
                        t=1
                    elif m==3 and g=="-":
                        g="O"
                        t=1
                    elif m==4 and i=="-":
                        i="O"
                        t=1
                    else:
                        if not Check_Win("O"):
                            t=1
            
            #Counterplay if X plays centre
            else:
                #Move2(III)
                if turn==2:
                    m=random.randint(1,2)
                    if Ist=="a" and m==1:
                        h="O"
                        IInd="h"
                    elif Ist=="a":
                        i="O"
                        IInd="i"
                    elif Ist=="c" and m==1:
                        d="O"
                        IInd="d"
                    elif Ist=="c":
                        g="O"
                        IInd="g"
                    elif Ist=="g" and m==1:
                        f="O"
                        IInd="f"
                    elif Ist=="g":
                        c="O"
                        IInd="c"
                    elif Ist=="i" and m==1:
                        b="O"
                        IInd="b"
                    elif Ist=="i":
                        a="O"
                        IInd="a"
                #Move3(III)
                elif turn==3 and Check_Win("X"):
                    if IInd=="h":
                        g="O"
                    elif IInd=="d":
                        a="O"
                    elif IInd=="b":
                        c="O"
                    elif IInd=="f":
                        i="O"
                #Move4-5(III)
                elif turn>3 and Check_Win("O"):
                    if Check_Win("X"):
                        Random()
           
                        
        #Attacking Algorithm starting with side (23%)                
        elif valid:
            #Move1
            if turn==1:
                m=random.choice(["b","d","f","h"])
                if m=="b":
                    b="O"
                elif m=="d":
                    d="O"
                elif m=="f":
                    f="O"
                elif m=="h":
                    h="O"
                Ist=m
            
            #Evaluating relative position of users first move
            if turn==2:
                #Move2(I)
                if (Ist=="b" and first in "fi") or (Ist=="f" and first in "ab"):
                    c="O"
                elif (Ist=="d" and first in "bc") or (Ist=="b" and first in "dg"):
                    a="O"
                elif (Ist=="f" and first in "gh") or (Ist=="h" and first in "cf"):
                    i="O"
                elif (Ist=="h" and first in "ad") or (Ist=="d" and first in "hi"):
                    g="O"
                else:
                    side=False
            if turn==2:
                #Move2(II)
                if Ist=="b" and first=="h":
                    g="O"
                elif Ist=="f" and first=="d":
                    a="O"
                elif Ist=="h" and first=="b":
                    c="O"
                elif Ist=="d" and first=="f":
                    i="O"
                else:
                    opposite=False
            
            #Counterplay if X plays non adjacent
            if turn>2 and side:
                #Move3(I)
                if turn==3 and Check_Win("O"):
                    e="O"
                #Move4(I)
                elif turn==4:
                    Check_Win("O")
            
            #Counterplay if X plays relatively opposite
            elif turn>2 and opposite:
                #Move3(II)
                if turn==3:
                    if Ist=="b" and a=="-":
                        a="O"
                    elif Ist=="f" and c=="-":
                        c="O"
                    elif Ist=="h" and i=="-":
                        i="O"
                    elif Ist=="d" and g=="-":
                        g="O"
                    else:
                        Random()
                #Move4-5(II)
                elif turn>3 and Check_Win("O"):
                    if Check_Win("X"):
                        Random()
            
            #Counterplay if X plays centre
            elif turn>1 and first=="e":
                #Move2(III)
                if turn==2:
                    if Ist in "bh":
                        L=["d","f"]
                    elif Ist in "df":
                        L=["b","h"]
                    m=random.choice(L)
                    if m=="b":
                        b="O"
                    elif m=="d":
                        d="O"
                    elif m=="f":
                        f="O"
                    elif m=="h":
                        h="O"
                #Move3(III)
                elif turn==3 and Check_Win("X"):
                    if b+d=="OO":
                        a="O"
                    elif b+f=="OO":
                        c="O"
                    elif d+h=="OO":
                        g="O"
                    elif f+h=="OO":
                        i="O"
                #Move4-5(III)
                elif turn>3 and Check_Win("O"):
                    if Check_Win("X"):
                        Random()
            
            #Counterplay if X plays adjacent
            else:
                #Move2(IV)
                if turn==2:
                    if (Ist=="b" and first=="c") or (Ist=="d" and first=="g"):
                        i="O"
                    elif (Ist=="f" and first=="i") or (Ist=="b" and first=="a"):
                        g="O"
                    elif (Ist=="h" and first=="i") or (Ist=="d" and first=="a"):
                        c="O"
                    elif (Ist=="f" and first=="c") or (Ist=="h" and first=="g"):
                        a="O"
                #Move3(IV)
                elif turn==3 and Check_Win("X"):
                    e="O"
                #Move4-5(IV)
                elif turn>3 and Check_Win("O"):
                    if Check_Win("X"):
                        Random()
                
        
        #Checking if O won
        if a==b==c!="-" or d==e==f!="-" or g==h==i!="-" or a==d==g!="-" or b==e==h!="-" or c==f==i!="-" or a==e==i!="-" or c==e==g!="-":
            PrintBoard(1)
            print("You Lost! Maybe Next time")
            break
        
        PrintBoard(0)
        
        #Checking if draw
        if turn==5:
            PrintBoard(1)
            print("Draw! Game Over")
            break
        
        #Users move
        valid=True  
        m=input("Enter your move: ")
        if m=="a" and a=="-":
            a="X"
        elif m=="b" and b=="-":
            b="X"
        elif m=="c" and c=="-":
            c="X"
        elif m=="d" and d=="-":
            d="X"
        elif m=="e" and e=="-":
            e="X"
        elif m=="f" and f=="-":
            f="X"
        elif m=="g" and g=="-":
            g="X"
        elif m=="h" and h=="-":
            h="X"
        elif m=="i" and i=="-":
            i="X"
        else:
            print("Invalid move. Try Again")
            valid=False
        
        if turn==1:
            first=m
        if turn==2:
            second=m
        
        #Checking if X won
        if a==b==c!="-" or d==e==f!="-" or g==h==i!="-" or a==d==g!="-" or b==e==h!="-" or c==f==i!="-" or a==e==i!="-" or c==e==g!="-":
            PrintBoard(1)
            print("You Win!")
            break
        
        
        
        
        
#MAIN
print("                        ABOUT THIS PROGRAM:")
print("This program has been designed to play against you in the famous game of tic-tac-toe.")
print("It has been programmed to play perfect defense, blocking any of your double-attack attempts but occasionally gives a chance for you to win on the last move so as to not make the game mundane and repetitive.")
print("It has also been programmed to start the game and attack in a variety of ways, creating double-attack opportunities based on your first few moves")
while True:
    r=0
    ans="y"
    print("\n                 MAIN MENU")
    print("1. Play continuous Attacking games (you start)")      
    print("2. Play cotninuous Defending games (computer starts)")
    print("3. Play alternate Attacking and Defending games")
    print("4. Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        while ans.lower()!="n":
            a=b=c=d=e=f=g=h=i="-"
            Defend()
            ans=input("Play Again? (Y/N) ")                
    
    elif ch==2:
        while ans.lower()!="n":
            a=b=c=d=e=f=g=h=i="-"
            Attack(r)
            r+=1
            ans=input("Play Again? (Y/N) ")
    
    elif ch==3:
        alt=0
        while ans.lower()!="n":
            a=b=c=d=e=f=g=h=i="-"
            if alt%2==0:
                Defend()
                alt+=1
            else:
                Attack(r)
                r+=1
                alt+=1
            ans=input("Play Again? (Y/N) ")
            
    elif ch==4:
        print("Thanks for playing!")
        break
        
        
    









