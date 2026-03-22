import heapq
from typing import Tuple

# 定义无穷大值，表示不可达距离
INF = 10**9 + 1
# 类型别名：pii表示一个元组，包含两个整数（节点，权重）
pii = Tuple[int, int]


def dijkstra(graph: list[list[pii]], start: int, n: int) -> list[int]:
    """
    Dijkstra算法实现：求从起点到所有节点的最短路径
    
    Args:
        graph: 邻接表表示的图，graph[u]是一个列表，包含与节点u相连的边
               每个边用元组(v, w)表示，v是目标节点，w是边权重
        start: 起点节点编号
        n: 图中节点的总数（节点编号从1到n）
    
    Returns:
        一个列表dist，dist[i]表示从起点到节点i的最短距离
        如果节点不可达，则dist[i] = INF
    """
    # 初始化距离数组，所有节点初始距离为无穷大
    dist = [INF] * (n + 1)
    
    # 使用最小堆（优先队列）存储(距离, 节点)对
    # Python的heapq默认是最小堆，会自动按距离从小到大排序
    pq = []
    
    # 起点距离设为0，并将其加入优先队列
    dist[start] = 0
    heapq.heappush(pq, (dist[start], start))
    
    # Dijkstra算法主循环
    while pq:
        # 从堆中取出当前距离最小的节点
        d, u = heapq.heappop(pq)  # d: 当前距离, u: 当前节点
        
        # 重要优化：如果取出的距离大于当前记录的距离，说明这个节点已经被处理过
        # 这是必要的，因为同一个节点可能多次进入优先队列（当有更短路径时）
        if d > dist[u]:
            continue  # 跳过这个已经处理过的节点
        
        # 遍历当前节点的所有邻居节点
        for v, w in graph[u]:  # v: 邻居节点, w: 边权重
            # 尝试松弛操作：如果通过u到v的距离比当前记录的距离更短
            if dist[u] + w < dist[v]:
                # 更新到v的最短距离
                dist[v] = dist[u] + w
                # 将更新后的节点加入优先队列
                heapq.heappush(pq, (dist[v], v))
    
    # 返回从起点到所有节点的最短距离数组
    return dist


# 主程序开始
if __name__ == "__main__":
    # 读取节点数n和边数m
    n, m = map(int, input().split())
    
    # 初始化邻接表：graph[i]存储与节点i相连的所有边
    # 使用列表推导式创建n+1个空列表（1-indexed：节点编号从1到n）
    graph = [[] for _ in range(n + 1)]
    
    # 读取所有边的信息
    for _ in range(m):
        # 读取一条边的两个端点u、v和权重w
        u, v, w = map(int, input().split())
        
        # 由于是无向图，需要在两个方向都添加边
        graph[u].append((v, w))  # 从u到v的边，权重为w
        graph[v].append((u, w))  # 从v到u的边，权重为w
    
    # 调用Dijkstra算法，计算从节点1到所有节点的最短距离
    dist = dijkstra(graph, 1, n)
    
    # 初始化答案为0
    ans = 0
    
    # 遍历所有节点（从1到n）
    for i in range(1, n + 1):
        # 检查节点i是否可达（距离是否为无穷大）
        if dist[i] == INF:
            # 如果存在不可达节点，说明图不连通
            ans = -1  # 设置答案为-1
            break     # 不再检查其他节点
        
        # 更新答案：取所有最短距离中的最大值
        ans = max(ans, dist[i])
    
    # 输出最终结果
    print(ans)