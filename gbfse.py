visited=[]
from queue import PriorityQueue
def bfs(graph,tmp,goal):
    visited.append(tmp)
    queue=PriorityQueue()
    queue.put((0,tmp))
    while queue:
        node=queue.get()[1]
        print(node,end=" ")
        if goal==node:
            break;
        else:
            for v,c in graph[node]:
                if v not in visited:
                    visited.append(v)
                    queue.put((c,v))
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
            cost=int(input("Enter cost : "))
            value=(cost,child)
            graph[vertex].append(value)
    flag=True
print(graph)
rt=input("Enter root node : ")
goal=input("Enter goal node : ")
bfs(graph,rt,goal)
