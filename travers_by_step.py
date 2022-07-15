import queue


def yuesefu(maxNum,s_value):
   
    # :param value: 总人数
    # :param s_value: 最后需要留下的人数
    # :return: 留下来的两位数
   
    # 列表生成式生成1到value的列表
    l1 = [item for item in range(1, maxNum)]
    # 初始化一个队列
    que = queue()
    # 遍历列表入队
    for i in l1:
        que.enqueue(i)
        # 判断队列中留下来的人数
    while que.size() != s_value:
        # 将队列前面的两个出队再进队
        que.enqueue(que.dequeue())
        que.enqueue(que.dequeue())
        # 将第三个出队
        que.dequeue()
    # 最后返回队列中的元素
    return que.que()

result = yuesefu(41, 3)
print('淘汰的顺序为',result[yuesefu])
