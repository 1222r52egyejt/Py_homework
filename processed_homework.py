import time
from turtle import delay

def choiceNum(stepNum, maxNum):   
    data = []
    del_data = []
    num = 0
    #delay(2)
    for i in range(1,maxNum + 1):
        data.append(i)

    while len(data) > 1:
        num += 1
        temp = data.pop(0)
        if num == stepNum:
            del_data.append(temp)
            num = 0
        else:
            data.append(temp)
    return{
        'last_data': data[0],
        'del_data': del_data
    }


def time_master(choiceNum):
    print('开始运行程序...')
    start = time.time()
    result = choiceNum(3, 44444)
    print('最后剩下的是第',result['last_data'],'人')
    print('淘汰顺序为',result['del_data'])
    stop = time.time()
    print('程序结束运行...')
    print(f'一共耗费了{(stop - start):.2f}秒。')

time_master(choiceNum)