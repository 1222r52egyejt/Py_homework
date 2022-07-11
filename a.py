def choiceNum(maxNum, stepNum):
    data = []
    delData = []
    num = 0
    for i in range (1, maxNum + 1):
        data.append(i)

    while len(data) > 1:
        num += 1
        temp = data.pop(0)
        if num == stepNum:
            delData.append(temp)
            num = 0
        else:
            data.append(temp)

    return{
        'lastData' : data[0],
        'delData' : delData
    }

result = choiceNum(41, 3)
print('最后剩下的是第', result['lastData'], '人')
print('淘汰的顺序是',result['delData'])