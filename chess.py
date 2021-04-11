def rmoves():
    res=[]
    for i in range(8):
        res.append([i,0,0,0])
        res.append([-i,0,0,0])
        res.append([0,i,0,0])
        res.append([0,-i,0,0])
    return res

def qmoves():
    res=[]
    for i in range(8):
        res.append([i,0,0,0])
        res.append([-i,0,0,0])
        res.append([0,i,0,0])
        res.append([0,-i,0,0])
        res.append([0,0,i,0])
        res.append([0,0,-i,0])
        res.append([0,0,0,i])
        res.append([0,0,0,-i])
    return res


def nmoves():
    return [[2,1,0,0],[1,2,0,0],[-1,2,0,0],[1,-2,0,0],[-1,-2,0,0],[-2,1,0,0],[2,-1,0,0],[-2,-1,0,0]]

def print_board(h):
    for i in range(8):
        print("_________________________________")
        print("|",h[i][0],"|",h[i][1],"|",h[i][2],"|",h[i][3],"|",h[i][4],"|",h[i][5],"|",h[i][6],"|",h[i][7],"|")
    print("_________________________________")
    


a=["R","N","B","K","Q","B","N","R"]
b=["P","P","P","P","P","P","P","P"]
c=[" "," "," "," "," "," "," "," "]
d=[" "," "," "," "," "," "," "," "]
e=[" "," "," "," "," "," "," "," "]
f=[" "," "," "," "," "," "," "," "]
g=["P","P","P","P","P","P","P","P"]
h=["R","N","B","K","Q","B","N","R"]

list1=[a,b,c,d,e,f,g,h]

class Figure:
    def __init__(self,name,move,capture):
        self.name=name
        self.move=move
        self.capture=capture
    
rook=Figure("R",rmoves(),rmoves())
knight=Figure("N",nmoves(),nmoves())
queen=Figure("Q",qmoves(),qmoves())
pawn=Figure("P",[[0,1,0,0]],[[0,0,1,0],[0,0,0,1]])
king=Figure("K",[])


print(rook.move)



    