from heapq import *
graph = {'A': [(2,'M'), (3,'P')],
         'M': [(2,'A'),(2,'N')],
         'N': [(2,'M'),(2,'B')],
         'P': [(3,'A'),(4,'B')],
         'B': [(4,'P'),(2,'N')]}
ans_cost=list()
ans_path=list()
def dfs(graph,cur,goal,path,pathcost):
    for i in graph[cur]:
        cost, node=i
        if node==goal:
            ans_cost.append(pathcost+cost)
            ans_path.append(path+[node])
        elif not (node in path):
            dfs(graph,node,goal,path+[node],pathcost+cost)

dfs(graph,'A','B',['A'],0)

ind=ans_cost.index(min(ans_cost))
print(ans_path[ind])