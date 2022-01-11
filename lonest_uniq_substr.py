# -*- coding: utf-8 -*-
'''
@Author: tanbo
@Time: 2022/1/10 10:19 下午
@File: lonest_uniq_substr.py
求最长不重复子串
'''


def find_longest_uniq_str(s):
    """
    寻找最长不重复子串
    :param s:
    :return:
    """
    window = {}
    left, right = 0, 0
    max_ln = 0
    while right < len(s):
        c = s[right]
        right += 1
        window[c] = window.get(c, 0) + 1
        # 以c结尾的字符存在重复的时候
        while window[c] > 1:
            d = s[left]
            left += 1
            window[d] -= 1
        max_ln = max(max_ln, right -left)

    return max_ln


if __name__ == "__main__":
    s = "aabab"
    o = find_longest_uniq_str(s)
    print(o)

