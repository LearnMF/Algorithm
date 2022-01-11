# -*- coding: utf-8 -*-
'''
@Author: tanbo
@Time: 2022/1/10 9:47 下午
@File: diff_position_char.py
异位字符
'''


def find_diff_char(s, t):
    """
    寻找s中包含t的全排列的字符,并输出起始位置
    :param s: source
    :param t: target
    :return:
    """
    result = []
    window, need = {}, {}
    left, right = 0, 0
    valid = 0
    for c in t:
        need[c] = need.get(c, 0) +1

    while right < len(s):
        c = s[right]
        right += 1

        if c in need:
            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                valid += 1
        # 当字符串宽度一旦达到t，就进行检测
        while right - left == len(t):
            if valid == len(need):
                result.append(left)
            d = s[left]
            left += 1
            if d in need: # 如果移除的是我们需要的
                if window[d] == need[d]:
                    valid-=1
                window[d]-=1

    return result


if __name__ == "__main__":
    s = "cbaebabacd"
    t = "abc"
    o = find_diff_char(s, t)
    print(o)
