from math import sqrt,pow

def initialise_AStar(arr,n):
    costs=[]
    for i in range(n):
        ll=[]
        for j in range(n):
            ll.append(0)
        costs.append(ll)
    for i in range(n):
        for j in range(n):
            costs[i][j]=round(sqrt(i*i+j*j),3)
    
    heuristic=[]
    for i in range(n):
        ll=[]
        for j in range(n):
            ll.append(0)
        heuristic.append(ll)
    for i in range(n):
        for j in range(n):
            heuristic[i][j]=(6-i-j)

    return costs,heuristic
    
def initialise(arr,n,costs,heuristic):
    g=[]
    h=[]
    f=[]
    for i in range(n):
        ll=[]
        for j in range(n):
            ll.append(10000)
        g.append(ll)
    
    g[0][0]=0

    for i in range(n):
        ll=[]
        for j in range(n):
            ll.append(0)
        h.append(ll) 

    for i in range(n):
        ll=[]
        for j in range(n):
            ll.append(0)
        f.append(ll)    

    for i in range(n):
        for j in range(n):
            h[i][j]=2*(n-1)-i-j
            f[i][j]=g[i][j]+h[i][j]
    
    return g,h,f

def set_parents(arr,n):
    parents=[]
    for i in range(n):
        ll=[]
        for j in range(n):
            ll.append(0)
        parents.append(ll)
    parents[0][0]=(0,0)
    return parents
    
def calculatef(arr,f):
    mini=100000
    xmin=-1
    ymin=-1
    for val in arr:
        n1=val[0]
        n2=val[1]
        # print(f)
        # print(n1,n2,mini)
        # print(type(f[n1][n2]),type(mini))
        if(f[n1][n2]<mini):
            mini=f[n1][n2]
            xmin=val[0]
            ymin=val[1]
    
    return (mini,xmin,ymin)

def find_neighbours(x,y,n):
    ll=[(x,y-1),(x,y+1),(x+1,y),(x-1,y)]
    for v in ll:
        if(v[0]<0 or v[0]>=n or v[1]<0 or v[1]>=n):
            ll.remove(v)
    return ll


def AStar(arr,f,g,h,parents,n):
    open=[(0,0)]
    closed=[]
    fl=0
    while(fl==0):
        mini,xmin,ymin=calculatef(open,f)
        current=arr[xmin][ymin]
        open.remove((xmin,ymin))
        if(xmin==n-1 and ymin==n-1):
            fl=1
            return
        else:
            closed.append((xmin,ymin))
            neighbours=find_neighbours(xmin,ymin,n)
            for u in neighbours:
                vall=g[xmin][ymin]
                if(g[u[0]][u[1]]>(vall+sqrt(pow(u[0]-xmin,2)+pow(u[1]-ymin,2))) and ((u[0],u[1]) not in open)):
                    g[u[0]][u[1]]=round(vall+sqrt(pow(u[0]-xmin,2)+pow(u[1]-ymin,2)),3)
                    f[u[0]][u[1]]=g[u[0]][u[1]]+h[u[0]][u[1]]
                    parents[u[0]][u[1]]=(xmin,ymin)
                    if((u[0],u[1]) not in open):
                        open.append((u[0],u[1]))

maze=[]
n=4
for i in range(n):
    ll=[]
    for j in range(n):
        ll.append((i,j))
    maze.append(ll)

# print(maze)

costs,heuristic=initialise_AStar(maze,n)
# print(costs,heuristic)
g,h,f=initialise(maze,n,costs,heuristic)
parents=set_parents(maze,n)
AStar(maze,f,g,h,parents,n)

path=[]
xx=n-1
yy=n-1
while(xx!=0 or yy!=0):
    path.append((xx,yy))
    xx,yy=parents[xx][yy][0],parents[xx][yy][1]
path.append((0,0))
print(path)
