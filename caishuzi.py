import random

def guess_number():
    # 生成一个1到100之间的随机数作为答案
    answer = random.randint(1, 100)

    # 初始化猜测次数
    guesses_taken = 0

    print("欢迎参加猜数字游戏！")
    print("我已经想好了一个1到100之间的数字，你需要猜出来。")

    while True:
        guess = int(input("请输入你的猜测："))

        guesses_taken += 1

        if guess < answer:
            print("你猜的数字太小了，请再试一次！")
        elif guess > answer:
            print("你猜的数字太大了，请再试一次！")
        else:
            print(f"恭喜你，猜对了！答案就是{answer}。")
            print(f"你猜了{guesses_taken}次。")
            break

    print("游戏结束。感谢参与！")

# 调用函数开始游戏
guess_number()
