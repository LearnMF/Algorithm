# -*- coding: utf-8 -*-
'''
@Author: tanbo
@Time: 2021/12/27 10:55 下午
@File: permute.py
'''

result = []


def permute(nums, path, result):
    if len(path) == len(nums):
        result.append(path)
        return

    for i in nums:
        if i in path:
            continue
        path.append(i)
        permute(nums, path[:], result)
        path.pop()


if __name__ == "__main__":
    x = [1, 2, 3]
    permute(x, [], result)
    print(result)

