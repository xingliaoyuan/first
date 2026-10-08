import random

secret = random.randint(1, 100)
count = 0

while True:
    guess = int(input("请输入你猜的数字（1-100）："))
    count = count + 1

    if guess > secret:
        print("大了")
    elif guess < secret:
        print("小了")
    else:
        print("恭喜你，猜中了！")
        print("你一共猜了", count, "次")
        break