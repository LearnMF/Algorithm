# -*- coding: utf-8 -*-
'''
@Author: tanbo
@Time: 2021/12/29 10:01 上午
@File: bi_dfs_open_lock.py
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
        s_list[idx] = str(int(s_list[idx])-1)

    assert len(s_list) == len(s), f"【s_list】:{s_list}; 【s】:{s}"
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

    assert len(s_list) == len(s), f"【s_list】:{s_list}; 【s】:{s}"
    return "".join(s_list)


def open_lock(deadends, target):
    """
    :param deadends: list
    :param target:
    :return:
    """
    deads = set(deadends)
    q1 = {"0000"}
    q2 = {target}
    step = 0
    visited = set()

    while q1 and q2:
        tmp = set()
        for item in q1:
            if item in deads:
                continue
            if item in q2:
                return step
            visited.add(item)

            # 相邻节点加入到集合中
            for i in range(4):
                up = plus_one(item, i)
                if up not in visited:
                    tmp.add(up)
                down = minus_one(item, i)
                if down not in visited:
                    tmp.add(down)
        step+=1

        q1 = q2
        q2 = tmp

    return -1


if __name__ == "__main__":
    deads = ["0098", "0079"]
    start = "0000"
    target = "0165"
    print(open_lock(deads, target=target))
    # x = "9999"
    # for i in range(4):
    #     print(plus_one("9999", i))
    #     print(x)

