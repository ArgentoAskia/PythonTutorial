import random

if __name__ == '__main__':
    # 该实例演示了数字猜谜游戏
    number = random.randint(1, 100)
    guess = -1
    print("数字猜谜游戏!(1 - 100以内)")
    while guess != number:
        guess = int(input("请输入你猜的数字："))
        if guess == number:
            print("恭喜，你猜对了！")
        elif guess < number:
            print("猜的数字小了...")
        elif guess > number:
            print("猜的数字大了...")