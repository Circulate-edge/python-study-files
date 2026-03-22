"""
洛谷P267 NOIP2015 扫雷
"""
graph = []
n, m = map(int, input().split()) # n:行数 m:列数
for i in range(n):
    graph.append(input())

dev = [(-1, -1), (-1 , 0), (-1, 1),
       (0, -1),           (0, 1),
       (1, -1), (1, 0), (1, 1)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == '*':
            print('*', end="")
        elif graph[i][j] != '*':
            # 遍历周围8个格子，查找有无地雷
            count = 0
            for dx, dy in dev:
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < m:
                    if graph[x][y] == '*':
                        count += 1
            print(count, end="")
    print()