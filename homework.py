data = []
delData = []
num = 0
for i in range(1,42):
    data.append(i)

while len(data) > 1:
    num += 1
    temp = data.pop(0)
    if num == 3:
        delData.append(temp)
        num = 0
    else:
        data.append(temp)

print('最后剩下的是第',data[0],'人')
print('淘汰顺序为',delData)