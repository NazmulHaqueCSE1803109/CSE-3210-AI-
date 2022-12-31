visited=[]
queue=[]
def bfs(graph,tmp):
    visited.append(tmp)
    queue.append(tmp)
    while queue:
        node=queue.pop(0)
        print(node,end=" ")
        if goal==node:
            break;
        else:
            for child in graph[node]:
                if child not in visited:
                    visited.append(child)
                    queue.append(child)
total_vertex=int(input("Enter the total number of vertex : "))
graph={}
flag=True
for i in range(total_vertex):
    vertex=input("Enter vertex : ")
    graph[vertex]=list()
    while flag:
        child=input(f"Enter child of {vertex} (-1 for exit : )")
        if child=='-1':
            flag=False
        else:
            graph[vertex].append(child)
    flag=True
print(graph)
rt=input("Enter root node : ")
goal=input("Enter goal node : ")
bfs(graph,rt,goal)
