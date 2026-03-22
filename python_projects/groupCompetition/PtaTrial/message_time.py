"""
战争时期，前线有n个哨所，每个哨所可能会与其他若干个哨所之间有通信联系。
信使负责在哨所之间传递信息，当然，这是要花费一定时间的（以天为单位）。
指挥部设在第一个哨所。当指挥部下达一个命令后，指挥部就派出若干个信使向与指挥部相连的哨所送信。
当一个哨所接到信后，这个哨所内的信使们也以同样的方式向其他哨所送信。
直至所有n个哨所全部接到命令后，送信才算成功。
因为准备充足，每个哨所内都安排了足够的信使（如果一个哨所与其他k个哨所有通信联系的话，这个哨所内至少会配备k个信使）。
现在总指挥请你编一个程序，计算出完成整个送信过程最短需要多少时间。
"""
import heapq


def dijkstra(n, graph, start):
    """
    使用Dijkstra算法计算从起点到所有节点的最短路径
    :param n: 节点数量
    :param graph: 图的邻接表表示
    :param start: 起始节点
    :return: 从起点到各节点的最短距离数组
    """
    INF = 10 ** 9  # 定义无穷大值
    dist = [INF] * (n + 1)  # 初始化距离数组，索引0不使用
    dist[start] = 0  # 起点到自身的距离为0
    pq = []  # 优先队列，存储(距离, 节点)
    heapq.heappush(pq, (0, start))  # 将起点加入优先队列

    while pq:
        d, u = heapq.heappop(pq)  # 取出距离最小的节点
        if d > dist[u]:  # 如果当前距离大于已知最短距离，则跳过
            continue
        for v, w in graph[u]:  # 遍历当前节点的所有邻居
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist


# 读入数据：n个哨所，m条通信线路
n, m = map(int, input().split())
# 构建图的邻接表，索引0不使用
graph = [[] for _ in range(n + 1)]
# 读入每条通信线路的信息
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # 无向图需要双向添加

# 计算从 1 出发到所有点的最短距离
dist = dijkstra(n, graph, 1)

# 找出最远的那个哨所的距离
max_time = max(dist[1:])  # 忽略下标0

if max_time >= 10 ** 9:
    print(-1)
else:
    print(max_time)