
import sys

from collections import deque

def choiceNum(stepNum, start_id):
    data = deque(['小明', '小梅', '小李', '小王', '小陈', 'kitty', 'hellokitty'])
    delData = deque()
    if 0 <= start_id < len(data):
        data.rotate(-(start_id))
    elif start_id >= len(data):
        data.rotate(-(len(data) - start_id - 1))
    else :
        print('输入错误')
        sys.exit(1)

    while len(data) > 1:
        data.rotate(-(stepNum-1)) #左移k-1次
        delData.append(data[0])
        data.popleft()      #删除第k元素
    return data[0], delData

print(choiceNum(2, 0))
