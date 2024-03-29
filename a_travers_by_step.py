import time
# import sys

from collections import deque

def choiceNum(stepNum, start_id):
    data = deque(['小明', '小梅', '小李', '小王', '小陈', 'kitty', 'hellokitty', '小红','曹总', '小曹' ])
    # data = deque(range(10))
    delData = deque()
    if 0 <= start_id < len(data):
        data.rotate(-(start_id))
    elif start_id >= len(data):
       # data.rotate(-(len(data) - start_id - 1))
        data.rotate(-(start_id % len(data)))
    else :
        # print('输入错误')
        # sys.exit(1)
        data.rotate(-(start_id % len(data) + len(data) + 1))

    while len(data) > 1:
        data.rotate(-(stepNum-1)) #左移stepNum-1次
        delData.append(data[0])
        # delData.append(data[0] + 1)
        data.popleft()      #删除第stepNum元素
    # return data[0] + 1, delData
    return data[0],delData

def time_master(choiceNum):     
    print('开始运行程序...')
    start = time.time()
    print(choiceNum(3, 15))
    stop = time.time()
    print('程序结束运行...')
    print(f'一共耗费了{(stop - start):.2f}秒。')

# print(choiceNum(2, 0))
time_master(choiceNum)