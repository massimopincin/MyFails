import random
import math

def gen_pts(n):
    res=[]
    for i in range(0,n):
        res.append(random.uniform(0,1))
    return res

def make_pairs(l):
    res=[]
    for i in range(0,int(len(l)/2)):
        temp=[]
        temp.append(l[2*i])
        temp.append(l[2*i+1])
        res.append(temp)
    return res

def dist(l):
    return math.sqrt(l[0]**2+l[1]**2)

def list_dist(l):
    res=[]
    for i in range(0,len(l)):
        res.append(dist(l[i]))
    return res

def calc(l):
    a=0
    b=len(l)
    for i in l:
        if i<=1:
            a+=1
    return 4*a/b

def final(x):
    return calc(list_dist(make_pairs(gen_pts(x))))

a=[]
for i in range(1000):
    a.append(final(10000))

print(sum(a)/len(a))
