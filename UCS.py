from collections import defaultdict
from queue import PriorityQueue

class Graph:
    def __init__(self,directed):
        self.graph=defaultdict(list)
        self.directed=directed
    def add_edge(self,u,v,weight):
        if self.directed:
            value=(weight,v)
            self.graph[u].append(value)
        else:
            value=(v,weight)
            self.graph[u].append(value)
            value=(u,weight)
            self.graph[v].append(value)
    def ucs(self,current_node,goal_node):
        visited=[]
        queue=PriorityQueue()
        queue.put((0,current_node))
        while queue:
            item=queue.get()
            current_node=item[1]
            if current_node==goal_node:
                print(current_node,end=" ")
                queue.queue.clear()
            else:
                if current_node in visited:
                    continue
                print(current_node,end=" ")
                visited.append(current_node)
                for neighbour in self.graph[current_node]:
                    queue.put((neighbour[0],neighbour[1]))
g=Graph(True)
g.graph=defaultdict(list)
g.add_edge('S','A',1)
g.add_edge('S','G',12)
g.add_edge('A','B',3)
g.add_edge('A','C',1)
g.add_edge('C','D',1)
g.add_edge('B','D',3)
g.add_edge('C','G',2)
g.add_edge('D','G',3)

g.ucs('S','G')


