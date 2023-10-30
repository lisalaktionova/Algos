from collections import deque

graph = {'A': ['M', 'P'],
         'M': ['A', 'N'],
         'N': ['M', 'B','P'],
         'P': ['A', 'B','N'],
         'B': ['P', 'N']}

def bfs(start, goal, graph):
    queue=deque([start]) #начальную вершину кладем в очередь
    visited = {start: None} #словарь посещенных вершин
    while queue:
        cur_node=queue.popleft() #достаем из очереди первый элемент
        if cur_node==goal:
            break
        next_nodes=graph[cur_node]
        for i in next_nodes:
            if i not in visited:
                queue.append(i)
                visited[i]=cur_node
    return visited

start='A'
goal='B'
visited=bfs(start, goal, graph)

cur_node=goal
print(f'\npath from {start} to {goal}: \n {goal}',end='')
while cur_node!=start:
    cur_node=visited[cur_node]
    print(f'--> {cur_node}', end='')
