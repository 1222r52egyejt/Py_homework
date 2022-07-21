
# import sys
from collections import deque
# from turtle import circle

class Person:
    
    def __init__(self, members = []):
        self._members = members
    def add_member(self, name):
        return self._members.append(name)

classA = Person()
classA.add_member('mary')
classA.add_member('jack')
classA.add_member('曹总')
classA.add_member('红红')
classA.add_member('小明')
classA.add_member('小王')
group = classA._members
# # print(group)

def choiceNum(stepNum, start_id, maxNum):
    # data = deque(['小明', '小梅', '小李', '小王', '小陈', 'kitty', 'hellokitty', '小红','曹总', '小曹' ])
    data = deque(range(maxNum))
    # data = deque(group)
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
        #delData.append(data[0])
        delData.append(data[0])
        data.popleft()      #删除第stepNum元素
    return data[0], delData
    #return data[0],delData
        

if __name__ == '_main_':
    choiceNum()


