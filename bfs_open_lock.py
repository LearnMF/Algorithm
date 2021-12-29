# -*- coding: utf-8 -*-
'''
@Author: tanbo
@Time: 2021/12/28 11:04 下午
@File: bfs_open_lock.py
'''


def minus_one(s, idx):
    """
    逆时针
    :param s:
    :param idx:
    :return:
    """
    s_list = list(s)
    if s_list[idx] == "0":
        s_list[idx] = "9"
    else:
        s_list[idx] = str(int(s_list[idx])+1)

    return "".join(s_list)



def plus_one(s, idx):
    """
    顺时针旋转
    :param s: 字符串
    :param idx:
    :return:
    """
    s_list = list(s)
    if s_list[idx] == "9":
        s_list[idx] = "0"
    else:
        s_list[idx] = str(int(s_list[idx]) + 1)

    return "".join(s_list)


def open_lock(deadends, target):
    """
    找不到的时候返回-1
    :param deadends: list
    :param target:
    :return:
    """
    deads = set(deadends)
    visited = {"0000"} # 只用来做追踪，不做判断
    q = ["0000"]
    step = 0
    while q:
        next_q = []
        for item in q:
            # 判断是否到达终点
            if item in deads:
                continue
            if item == target:
                return step
            # 生成候选集合
            visited.add(item)
            for i in range(4): # 每个位置都有两种变化的可能
                up = plus_one(item, i)
                down = minus_one(item, i)
                if up not in visited:
                    next_q.append(up)

                if down not in visited:
                    next_q.append(down)
        step += 1
        q = next_q

    return -1


if __name__ == "__main__":
    x = "0009"
    j = 1
    print(minus_one(x, j))