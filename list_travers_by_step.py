# import time
# from turtle import delay

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


if __name__ == '_main_':
    choiceNum()
   