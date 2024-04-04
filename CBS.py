
from AStar_mod2 import initialise_AStar,initialise,set_parents,calculatef,find_neighbours,AStar

class Node:
    def __init__(self): 
        self.leftChild=None
        self.rightChild=None
        self.constraints=[]
        self.solution=[]
        self.cost=0

def find_best_node(arr):
    maxi=100000
    indi=None
    for u in arr:
        if(u.cost<maxi):
            maxi=u.cost
            indi=u 
    return indi

maze=[]
m=4
n=4
for i in range(m):
    ll=[]
    for j in range(n):
        ll.append((i,j))
    maze.append(ll)
maze[0][0]=-1
maze[0][3]=-1
maze[3][0]=-1
maze[3][3]=-1

# print(maze)
start_rat1=(0,1)
start_rat2=(1,0)
stop_rat1=(3,2)
stop_rat2=(2,3)

open=[]

def set_first_path(constraints):
    costs1,heuristic1=initialise_AStar(maze,m,n,start_rat1,stop_rat1)
    g1,h1,f1=initialise(maze,m,n,costs1,heuristic1,start_rat1,stop_rat1)
    parents1=set_parents(maze,m,n,start_rat1,stop_rat1)
    AStar(maze,f1,g1,h1,parents1,m,n,start_rat1,stop_rat1)
    path1=[]
    xx1=stop_rat1[0]
    yy1=stop_rat1[1]
    while(xx1!=start_rat1[0] or yy1!=start_rat1[1]):
        xx1,yy1=parents1[xx1][yy1][0],parents1[xx1][yy1][1]
    path1.append(start_rat1)
    path1=path1[::-1]
    n1=len(path1)
    for j in range(1,n1):
        if((1,path1[j],j) in constraints):
            path1.insert(j,path1[j-1])
            j-=1
    return path1

def set_second_path(constraints):
    costs2,heuristic2=initialise_AStar(maze,m,n,start_rat2,stop_rat2)
    g2,h2,f2=initialise(maze,m,n,costs2,heuristic2,start_rat2,stop_rat2)
    parents2=set_parents(maze,m,n,start_rat2,stop_rat2)
    AStar(maze,f2,g2,h2,parents2,m,n,start_rat2,stop_rat2)
    path2=[]
    xx2=stop_rat2[0]
    yy2=stop_rat2[1]
    while(xx2!=start_rat2[0] or yy2!=start_rat2[1]):
        path2.append((xx2,yy2))
        xx2,yy2=parents2[xx2][yy2][0],parents2[xx2][yy2][1]
    path2.append(start_rat2)
    path2=path2[::-1]
    n2=len(path2)
    for j in range(1,n2):
        if((2,path2[j],j) in constraints):
            path2.insert(j,path2[j-1])
            j-=1
    return path2

R=Node()
R.constraints=[]

# costs1,heuristic1=initialise_AStar(maze,m,n,start_rat1,stop_rat1)
# g1,h1,f1=initialise(maze,m,n,costs1,heuristic1,start_rat1,stop_rat1)
# parents1=set_parents(maze,m,n,start_rat1,stop_rat1)
# AStar(maze,f1,g1,h1,parents1,m,n,start_rat1,stop_rat1)
# path1=[]
# xx1=stop_rat1[0]
# yy1=stop_rat1[1]
# while(xx1!=start_rat1[0] or yy1!=start_rat1[1]):
#     path1.append((xx1,yy1))
#     xx1,yy1=parents1[xx1][yy1][0],parents1[xx1][yy1][1]
# path1.append(start_rat1)
# path1=path1[::-1]

# costs2,heuristic2=initialise_AStar(maze,m,n,start_rat2,stop_rat2)
# g2,h2,f2=initialise(maze,m,n,costs2,heuristic2,start_rat2,stop_rat2)
# parents2=set_parents(maze,m,n,start_rat2,stop_rat2)
# AStar(maze,f2,g2,h2,parents2,m,n,start_rat2,stop_rat2)
# path2=[]
# xx2=stop_rat2[0]
# yy2=stop_rat2[1]
# while(xx2!=start_rat2[0] or yy2!=start_rat2[1]):
#     path2.append((xx2,yy2))
#     xx2,yy2=parents2[xx2][yy2][0],parents2[xx2][yy2][1]
# path2.append(start_rat2)
# path2=path2[::-1]

path1=set_first_path(R.constraints)
path2=set_second_path(R.constraints)
R.solution=[path1,path2]
R.cost=len(R.solution[0])+len(R.solution[1])
open.append(R)
output=None
while(len(open)>0):
    P=find_best_node(open)
    check=1
    con_point=(-1,-1)
    con_time=-1
    sol1=P.solution[0]
    sol2=P.solution[1]
    ll=min(len(sol1),len(sol2))
    for i in range(ll):
        if(sol1[i]==sol2[i] or ((1,sol1[i],i) in P.constraints) or ((1,sol2[i],i) in P.constraints)):
            check=0
            con_point=sol1[i]
            con_time=i
            break 
    if(check==1):
        output=P
        break
    else:
        for q in range(2):
            A=Node()
            A.constraints=P.constraints
            A.constraints.append((q+1,con_point,con_time))
            path1=set_first_path(A.constraints)
            path2=set_second_path(A.constraints)
            A.solution=[path1,path2]
            A.cost=len(A.solution[0])+len(A.solution[1])
            open.append(A)

print(P.solution)



            




