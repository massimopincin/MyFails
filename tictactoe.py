def won(c, n):
    if c[0] == n and c[1] == n and c[2] == n: return 1
    if c[3] == n and c[4] == n and c[5] == n: return 1
    if c[6] == n and c[7] == n and c[8] == n: return 1
    if c[0] == n and c[3] == n and c[6] == n: return 1
    if c[1] == n and c[4] == n and c[7] == n: return 1
    if c[2] == n and c[5] == n and c[8] == n: return 1
    if c[0] == n and c[4] == n and c[8] == n: return 1
    if c[2] == n and c[4] == n and c[6] == n: return 1
    return 0

def display(a):
    print("\n\n{}|{}|{}".format(a[6],a[7],a[8]))
    print("-----")
    print("{}|{}|{}".format(a[3],a[4],a[5]))
    print("-----")
    print("{}|{}|{}\n\n".format(a[0],a[1],a[2]))

def xo(num):
    if num==1:
        return("X")
    else:
        return("O")

def name():
    x=["",""]
    print("Welcome! First, insert the players' names:\n")
    x[0]=input("Insert Player 1 name: ")
    x[1]=input("Insert Player 2 name: ")
    return(x)

def play_again(res,names):
        y1=input("\nWanna play again?(yes/no)\n")
        if y1=="yes":
            y2=input("\nWanna keep the same names?(yes/no)\n")
            if y2=="yes":
                play(res,names)
            else:
                res=[0,0]
                play(res,name())        
    
def play(res,names):
    a=[]
    b=[]
    for i in range(0,9):
        a.append(0)
        b.append(" ")

    current=1
    count=0
    c=0

    print("\n\n\nWelcome to tic tac toe!\n\n{} wins: {}\n{} wins: {}\n\nIf you want to interrupt, write 'exit'. Enjoy!\n\n".format(names[0],res[0],names[1],res[1]))

    while c==0 and count<9:
        print("\n------------------------------------------\n------------------------------------------\n------------------------------------------")
        display(b)

        count+=1
        x=0
        while x not in range(1,10) or a[x-1]!=0:
            x=input("{} playing. Choose a move: ".format(names[current-1]))
            if x=="exit":
                raise Exception("\n\nOk, goodbye.\n\n")
                break
            x=int(x)
            if x not in range(1,10):
                print("\nInvalid input!\n")
            elif a[x-1]!=0:
                print("\nAlready taken!\n")

        a[x-1]=current
        b[x-1]=xo(current) 

        c=won(a,current)

        if c==1:
            print("\n\n {} wins!".format(names[current-1]))
            display(b)
            if current==1:
                res[0]+=1
            else:
                res[1]+=1
            play_again(res,names)

        if count==9:
            display(b)
            print("\nFull board!\n")
            play_again(res,names)                       

        if current==1:
            current=2
        else:
            current=1

res=[0,0]
namelist=name()
play(res,namelist)