from math import sqrt,pow

def initialise_AStar(arr,m,n,start,stop):
    costs=[]
    for i in range(m):
        ll=[]
        for j in range(n):
            ll.append(-1)
        costs.append(ll)
    for i in range(m):
        for j in range(n):
            if(arr[i][j]!=-1):
                costs[i][j]=round(sqrt(pow(i-start[0],2)+pow(j-start[1],2)),3)
    
    heuristic=[]
    for i in range(m):
        ll=[]
        for j in range(n):
            ll.append(-1)
        heuristic.append(ll)
    for i in range(m):
        for j in range(n):
            if(arr[i][j]!=-1):
                heuristic[i][j]=(stop[0]+stop[1]-i-j)

    return costs,heuristic
    
def initialise(arr,m,n,costs,heuristic,start,stop):
    g=[]
    h=[]
    f=[]
    for i in range(m):
        ll=[]
        for j in range(n):
            ll.append(10000)
        g.append(ll)
    
    g[start[0]][start[1]]=0

    for i in range(m):
        ll=[]
        for j in range(n):
            ll.append(-1)
        h.append(ll) 

    for i in range(m):
        ll=[]
        for j in range(n):
            ll.append(-1)
        f.append(ll)    

    for i in range(m):
        for j in range(n):
            if(arr[i][j]!=-1):
                h[i][j]=stop[0]+stop[1]-i-j
                f[i][j]=g[i][j]+h[i][j]
    
    return g,h,f

def set_parents(arr,m,n,start,stop):
    parents=[]
    for i in range(m):
        ll=[]
        for j in range(n):
            ll.append((-1,-1))
        parents.append(ll)
    parents[start[0]][start[1]]=(start[0],start[1])
    return parents
    
def calculatef(arr,array,f,start,stop):
    mini=100000
    xmin=-1
    ymin=-1
    for val in array:
        n1=val[0]
        n2=val[1]
        # print(f)
        # print(n1,n2)
        # print(type(f[n1][n2]),type(mini))
        if(f[n1][n2]<mini and arr[n1][n2]!=-1):
            mini=f[n1][n2]
            xmin=val[0]
            ymin=val[1]
    
    return (mini,xmin,ymin)

def find_neighbours(arr,x,y,m,n,start,stop):
    ll=[(x,y-1),(x,y+1),(x+1,y),(x-1,y),(x+1,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1)]
    lll=[]
    for v in ll:
        if(v[0]>=0 and v[0]<m and v[1]>=0 and v[1]<n and arr[v[0]][v[1]]!=-1):
            lll.append(v)
    # print("I am ")
    # print(lll)
    return lll


def AStar(arr,f,g,h,parents,m,n,start,stop):
    open=[start]
    closed=[]
    fl=0
    while(fl==0):
        # print(open)
        mini,xmin,ymin=calculatef(arr,open,f,start,stop)
        current=arr[xmin][ymin]
        open.remove((xmin,ymin))
        if(xmin==stop[0] and ymin==stop[1]):
            fl=1
            return
        else:
            closed.append((xmin,ymin))
            neighbours=find_neighbours(arr,xmin,ymin,m,n,start,stop)
            for u in neighbours:
                if(arr[u[0]][u[1]]==-1 or (u in closed)):
                    continue
                vall=g[xmin][ymin]
                if(g[u[0]][u[1]]>(vall+sqrt(pow(u[0]-xmin,2)+pow(u[1]-ymin,2))) and ((u[0],u[1]) not in open)):
                    g[u[0]][u[1]]=round(vall+sqrt(pow(u[0]-xmin,2)+pow(u[1]-ymin,2)),3)
                    f[u[0]][u[1]]=g[u[0]][u[1]]+h[u[0]][u[1]]
                    parents[u[0]][u[1]]=(xmin,ymin)
                    if((u[0],u[1]) not in open):
                        open.append((u[0],u[1]))

maze=[]
m=4
n=5
for i in range(m):
    ll=[]
    for j in range(n):
        ll.append((i,j))
    maze.append(ll)
maze[3][1]=-1
maze[3][2]=-1

# print(maze)

begin=(0,2)
end=(2,3)

costs,heuristic=initialise_AStar(maze,m,n,begin,end)
# print(costs,heuristic)
g,h,f=initialise(maze,m,n,costs,heuristic,begin,end)
parents=set_parents(maze,m,n,begin,end)
AStar(maze,f,g,h,parents,m,n,begin,end)

path=[]
xx=end[0]
yy=end[1]
while(xx!=begin[0] or yy!=begin[1]):
    path.append((xx,yy))
    xx,yy=parents[xx][yy][0],parents[xx][yy][1]
path.append(begin)
# print(path[::-1])
