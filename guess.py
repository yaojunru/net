#/bin/python
#coding=utf8
import random
secret = random.randint(1,10)
i = 0
print '--------by yaojunru-----------'
temp = input("guess number:")
guess = int(temp)
if guess == secret:
    print "你猜对了，你难道是我心中的蛔虫"
    print "哼，猜对了，也没奖励！"
else:
    if guess > secret:
        print "大了，大了"
    else:
        print "小了，小了"
while guess != secret and i < 2:
    temp = input("please relay input:")
    guess = int(temp)
    if guess == secret:
        print "你猜对了，你难道是我心中的蛔虫"
        print "哼，猜对了，也没奖励！"
    else:
        if guess > secret:
            print "大了，大了"
        else:
            print "小了，小了"
    i = i + 1
    #print "对不起，猜错了，我心中想的是8"
print "游戏结束，不玩拉~"