"""
筛选嫌疑人：遍历每个通话者的拨出记录，统计其每天给不同人拨出的短通话（时长≤5 分钟）数量，以及这些人中回拨的比例。若短通话数超过 k 且回拨比例≤20%，则判定为嫌疑人。
团伙划分：嫌疑人之间若有通话（无论呼出 / 接收），则属于同一个团伙。这是典型的连通分量问题，可使用并查集（Union-Find） 解决。
输出处理：将每个连通分量的成员按升序排列，再按每个团伙第一个成员的升序输出。
"""
#导入defaltdict
from collections import defaultdict
#  读取输入,k=短通话阈值,n=号码数量,m=通话对数
k,n,m = [int(x) for x in input().split()]
# 存储：呼出者 -> {接收者: 是否短通话(时长<=5)}
call_out = defaultdict(dict)
# 存储：接收者 -> 呼出者集合（用于快速判断是否回拨）
call_in = defaultdict(set)
# 存储所有通话对（用于后续团伙判断）
calls = []
for _ in range(m):
    a,b,t = [int(x) for x in input().split()]
    calls.append((a,b))
    # 记录呼出者a到b的通话是否为短通话
    # 累积标记: 如果某两人之间有多次通话，只要其中有一次是短通话，就认为存在短通话关系
    # 避免覆盖: 防止后来的长通话覆盖之前的短通话记录
    # 简化判断: 最终只需要知道两人间是否存在短通话，而不需要记录每次的具体时长
    call_out[a][b] = call_out[a].get(b, False) or (t <= 5)
    # 记录接收者b的呼出者a
    call_in[b].add(a)