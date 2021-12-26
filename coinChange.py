# -*- coding: utf-8 -*-
'''
@Author: tanbo
@Time: 2021/12/25 12:01 下午
@File: coinChange.py
'''


def coin_change(coins, amount):
    """
    dp[n]代表凑到n元需要的最小组合数量
    :param coins: 硬币的各种面值
    :param amount: 目标总数
    :return:
    """
    dp = [float('inf')] * (amount+1)
    dp[0] = 0
    # 1.外层的问题规模遍历
    for i in range(1, len(dp)):
        for j in coins: # 2. 状态值枚举
            if i-j < 0:
                continue
            # 一个硬币对应一个问题规模的缩减
            dp[i] = min(dp[i], dp[i-j]+1)
    return dp[-1]


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(coin_change(coins, amount))