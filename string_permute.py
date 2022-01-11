# -*- coding: utf-8 -*-
'''
@Author: tanbo
@Time: 2022/1/10 1:01 下午
@File: string_permute.py
滑动窗口
输入两个字符串S和T,判断S是否包含T的排列，也就是判断S中是否存在一个子串是T的一种全排列

假设给定一个S和一个T，请问S中是否存在一个子串，包含T中所有的字符且不包含其他字符吗？
'''


def checkInclusion(t, s):
    """
    left,right 左闭右开
    :param t: target str
    :param s: source str
    :return:
    """
    need, window = {}, {}
    for c in t:
        need[c] = need.get(c, 0) +1
    left, right = 0, 0
    valid, ln = 0, 10^5
    while right < len(s):
        c = s[right]
        right += 1
        if c in need: # 先增加window，在更新valid
            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                valid += 1

        while (right - left) >= len(t):

            # 收缩的判断条件,因为每个不同的排列的长度都是一致的
            if valid == len(need):
                print(s[left:right])
                return True
            d = s[left]
            left += 1

            if d in need: # 先更新valid，在更新window
                if window.get(d, 0) == need[d]:
                    valid -= 1
                window[d] = window.get(d, 0) -1
    return False


if __name__ == "__main__":
    s = "helloworld"
    t = "oow"
    print(checkInclusion(t, s))




