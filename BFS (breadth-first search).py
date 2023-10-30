from heapq import * #этот модуль обеспечивает реализацию алгоритма очереди с кучами

graph = {'A': [(2,'M'), (3,'P')],
         'M': [(2,'A'),(2,'N')],
         'N': [(2,'M'),(2,'B')],
         'P': [(3,'A'),(4,'B')],
         'B': [(4,'P'),(2,'N')]}

def bfs(start, goal, graph):
    queue=[]
    heappush(queue,(0,start)) #помещает (0, start) в queue, сохраняя инвариант кучи (чтобы 'сверху' был наименьший элемент)
    cost_visited={start:0}
    visited={start:None} #посещенные вершины
    while queue:
        cur_cost, cur_node=heappop(queue) #извлекает и возращает наименьший элемент из queue, сохраняя инвариант кучи
        #cur_cost = стоимость текущего элемента,  cur_node = текущий элемент
        if cur_node==goal:
            break
        next_nodes=graph[cur_node]
        for i in next_nodes:
            neigh_cost, neigh_node=i
            new_cost=cost_visited[cur_node]+neigh_cost # к стоимости вершины прибавляется стоимость предыдущей вершины
            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                heappush(queue, (new_cost, neigh_node))#помещаем в очередь новый элемент
                cost_visited[neigh_node]=new_cost
                visited[neigh_node]=cur_node
                print(visited)
    return visited

start='A'
goal='B'
visited=bfs(start, goal, graph)

cur_node=goal
print(f'\npath from {start} to {goal}: \n {goal}',end='')
while cur_node!=start:
    cur_node=visited[cur_node]
    print(f'--> {cur_node}', end='')
