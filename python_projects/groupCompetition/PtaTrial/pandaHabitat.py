"""
1. 读取 n 个时间段
2. 将每个时间段的 start 和 finish 转换为总秒数
3. 创建事件列表：(time, type)，type 为 +1（开始）或 -1（结束）
4. 按 time 排序事件
5. 遍历事件，累加计数，记录最大值
6. 输出最大值（即最少山头数）
"""
#   时间转秒
"""
def time_to_seconds(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s

panda_num = int(input())
time_list = []

#   读取时间
for i in range(panda_num):
    start, finish = input().split()
    #  创建事件列表，type 为 +1（开始）或 -1（结束）
    #time_list.append((time_to_seconds(start), 1))
    #time_list.append((time_to_seconds(finish), -1))
    time_list.append((start, 1))
    time_list.append((finish, -1))

#   对事件按时间排序，相同时间点先处理结束事件（-1），再处理开始事件（+1）
time_list.sort(key=lambda x: (x[0],x[1]))

#   使用扫描线法统计任意时刻最多同时活跃的大熊猫数量
count = 0
max_count = 0
for _, type in time_list:
    count += type   # 更新计数，时间
    max_count = max(max_count, count)
print(max_count)
"""
# 扫描线法，用数组存储开始结束时间操作
"""
设置列表长度为一天的秒数+1，
所有元素初始化为0，
列表索引为开始时间存入 +1，为结束存入-1，代表进行事件，记录最大并行区间
结束时间的索引需额外+1代表闭区间
"""
#   输入
"""
n = int(input())
schedule = [0 for _ in range(86401)]
for i in range(n):
    start, finish = input().split()
    st = int(start[:2])*3600 + int(start[3:5])*60 + int(start[6:])
    ft = int(finish[:2])*3600 + int(finish[3:5])*60 + int(finish[6:])
    schedule[st] += 1
    schedule[ft+1] -= 1

interval = 0
max_interval = 0
for i in range(len(schedule)):
    interval += schedule[i]
    max_interval = max(max_interval, interval)

print(max_interval)
"""

#  分别用start,end存放开始和结束时间段
n = int(input())
start,end = [],[]
# 读取每只大熊猫的活动时间段
for i in range(n):
    s_time,e_time = input().split()
    start.append(s_time)
    end.append(e_time)
# 对开始时间和结束时间分别进行排序
start.sort()
end.sort()
# 初始化需要的山头数量为n（最坏情况，每只熊猫都需要独立山头）
interval = n
# 用于遍历结束时间数组的索引
index2 = 0
for index1 in range(n):
    # 如果当前开始时间大于某个结束时间，说明有山头可以复用
    if start[index1] > end[index2]:
        interval -= 1
        index2 += 1
print(interval)