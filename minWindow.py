# -*- coding: utf-8 -*-
'''
@Author: tanbo
@Time: 2022/1/9 2:58 下午
@File: minWindow.py
滑动窗口
'''
import loguru
logger = loguru.logger


def min_window(s, t):
    """
    给定两个字符串，在S中找到包含T中全部字母的最短子串
    :param s: source 字符串
    :param t: target 字符串
    :return:
    """
    need = {}
    window = {}
    for c in t:
        if c not in need:
            need[c] = 0
        need[c] += 1
    left, right = 0, 0
    valid = 0 # valid的作用是啥？
    # 记录最小覆盖子串的起始索引和长度
    start = 0
    int_max = ln = 5^10
    while right < len(s):
        c = s[right]
        right += 1
        if c in need:
            window[c] = window.get(c, 0) +1
            if window[c] == need[c]: # 当某个元素的个数满足需要的时候
                valid += 1
        # 至到window中包含必要的元素,   valid达到要求，这个时候需要减少window中数据
        while valid == len(need):
            if right - left < ln:
                start = left
                ln = right - left
            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1

    logger.info(f"start:{start}; ln:{ln}")
    if ln == int_max:
        return ""

    return s[start: start+ln]


if __name__ == "__main__":
    s = "ADBECFEBANC"
    t = "BANC"
    print(min_window(s, t))



