#猜数游戏
import random

exit_game = 1
while exit_game:
    num = random.randint(1,100)
    #print(num)
    while True:
        num1 = int(input("你觉得是多少呢："))
        if num1 > num:
            print("数大了，继续猜")
        elif num1 < num:
            print("数小了，继续猜")
        else:
            print("猜中啦！超厉害！")
            break
    exit_game = input("再玩一次请输入yes,退出请输入exit或者直接回车：")
    if  'exit' == exit_game:
        break