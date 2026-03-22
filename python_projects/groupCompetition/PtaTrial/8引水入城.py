from collections import deque
import sys

def main():
    # 读入n和m
    n, m = map(int, sys.stdin.readline().split())
    
    # 存储每个城市的海拔高度，n行m列
    city = []
    for _ in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        city.append(row)
    
    # 记录最后一行的哪些列能被灌溉到
    visited_end = [0] * m
    
    # 存储每个水源能灌溉的最后一行的区间[left, right]
    dt = []
    
    # 遍历第一行的每个位置，作为潜在水源
    for t in range(m):
        # 记录从当前水源出发能到达的位置，1表示可达
        map_visited = [[0] * m for _ in range(n)]
        map_visited[0][t] = 1
        q = deque()
        q.append((0, t))
        
        # BFS遍历，从高海拔流向低海拔
        while q:
            i, j = q.popleft()
            
            # 向上走：不越界、未访问过、且当前海拔高于上方
            if i > 0 and map_visited[i-1][j] == 0 and city[i][j] > city[i-1][j]:
                map_visited[i-1][j] = 1
                q.append((i-1, j))
            # 向下走
            if i < n-1 and map_visited[i+1][j] == 0 and city[i][j] > city[i+1][j]:
                map_visited[i+1][j] = 1
                q.append((i+1, j))
            # 向左走
            if j > 0 and map_visited[i][j-1] == 0 and city[i][j] > city[i][j-1]:
                map_visited[i][j-1] = 1
                q.append((i, j-1))
            # 向右走
            if j < m-1 and map_visited[i][j+1] == 0 and city[i][j] > city[i][j+1]:
                map_visited[i][j+1] = 1
                q.append((i, j+1))
        
        # 计算当前水源能灌溉的最后一行的区间
        left = m      # 左边界，初始化为最大值
        right = -1    # 右边界，初始化为最小值
        for k in range(m):
            if map_visited[n-1][k] == 1:
                left = min(left, k)
                right = max(right, k)
                visited_end[k] = 1  # 标记最后一行的该列能被灌溉
        
        # 如果该水源能灌溉到最后一行（至少一列），则记录区间
        if right >= left:
            dt.append((left, right))
    
    # 按区间左端点从小到大排序
    dt.sort(key=lambda x: x[0])
    
    # 检查最后一行的所有列是否都能被灌溉
    covered = 1
    no_water = 0
    for i in range(m):
        if visited_end[i] == 0:
            covered = 0
            no_water += 1
    
    # 输出结果
    if covered == 0:
        # 情况1：无法完全覆盖
        print(0)
        print(no_water)
    else:
        # 情况2：可以完全覆盖，计算最少需要的水源数（区间覆盖问题）
        num = 0              # 需要的水源数量
        right = -1           # 当前已覆盖到的最右列
        next_max_right = 0   # 下一个可能覆盖到的最右列
        i = 0                # 遍历dt的索引
        dt_len = len(dt)
        
        # 贪心算法：每次选择能衔接当前覆盖区间且向右延伸最远的区间
        while right < m-1:   # 当还未完全覆盖最后一行时
            # 找出所有左端点<=right+1的区间，取其中最大的右端点
            while i < dt_len and dt[i][0] <= right + 1:
                next_max_right = max(next_max_right, dt[i][1])
                i += 1
            right = next_max_right  # 更新已覆盖到的最右列
            num += 1                # 增加一个水源
        print(1)
        print(num)

if __name__ == "__main__":
    main()