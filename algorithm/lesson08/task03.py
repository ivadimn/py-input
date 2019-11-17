# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.


def generate_graph(n: int) -> list:
    g = []
    for i in range(n):
        g.append([j for j in range(n) if i != j])
    return g

def dfs(g, v, visited):
    if v not in visited:
        visited.append(v)
        for n in g[v]:
            dfs(g, n, visited)
    return visited

n = int(input("Введите число вершин : "))
graph = generate_graph(n)
visited = dfs(graph, 0, [])
print(visited)
