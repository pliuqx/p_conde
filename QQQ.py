# -*- coding:utf-8 -*-
# @Time : 2021/8/13 14:40
# @Author: 应无所住，何生其心
# @File : QQQ.py
# @software : PyCharm

import random

guess_list = ["石头", "剪刀", "布"]
win_combination = [["布", "石头"], ["石头", "剪刀"], ["剪刀", "布"]]

while True:
    computer = random.choice(guess_list)
    people = input('请输入:石头,剪刀,布\n').strip()  #  .strip()这个函数的作用是去掉换行，空格等多于的符号
    if people not in guess_list:
        continue
    elif computer == people:
        print(computer)
        print("平手，再玩一次！")
    elif [computer, people] in win_combination:  # 判断列表中的值[computer, people]在不在另一个[win_combination]列表中，如果在并进行比较
        print(computer)
        print("电脑获胜，再玩，人获胜才能退出！")
    else:
        print(computer)
        print("人获胜！")
        break
