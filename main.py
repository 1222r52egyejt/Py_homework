import deque_travers_by_step
import list_travers_by_step
import time



def time_master():     
    print('开始运行程序...')
    start = time.time()
    print(deque_travers_by_step.choiceNum(3, 1, 44444))
    #print(list_travers_by_step.choiceNum(3, 44444))
    stop = time.time()
    print('程序结束运行...')
    print(f'一共耗费了{(stop - start):.2f}秒。')

time_master()

