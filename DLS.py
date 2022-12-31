visited=[]
stack=[]
def dfs(graph,tmp,goal):
    dept=1
    lev=3
    visited.append(tmp)
    stack.append(tmp)
    while stack:
        node=stack.pop()
        print(node, end=" ")
        if node==goal:
            break
        else:
            for child in graph[node]:
                if child not in visited:
                    visited.append(child)
                    stack.append(child)
                    i=1
            if i==1:
                dept=dept+1
            if(dept==lev):
                break


total_vertex=int(input("Enter the no. of vertex : "))
graph={}
flag=True
for i in range(total_vertex):
    vertex=input("Enter vertex : ")
    graph[vertex]=list()
    while flag:
        child=input(f"Enter child of {vertex} (-1 for exit) :")
        if child=='-1':
            flag=False
        else:
            graph[vertex].append(child)
    flag=True
print("Entered graph is : ",graph)
rt=input("Enter root node : ")
goal=input("Enter goal node : ")
dfs(graph,rt,goal)