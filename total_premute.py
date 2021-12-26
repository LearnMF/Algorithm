# -*- coding: utf-8 -*-
'''
@Author: tanbo
@Time: 2021/12/25 3:11 下午
@File: total_premute.py
'''
import loguru
logger = loguru.logger


def permute(nums, tmp_result, result):
    """
    寻找nums中，不重复的所有排列组合数量
    note:回溯一定要有return; list的pop方法弹出最后一个元素
    :param nums: 全局不变量，参数
    :param tmp_result: 当前层的结果
    :param result: 全局结果;list of list
    :return:
    """
    if len(tmp_result) == len(nums):
        result.append(tmp_result)
        # logger.info(f"result:{result}")
        return
    for item in nums:
        if item in tmp_result:
            continue
        tmp_result.append(item)
        logger.info(f"tmp_result:{tmp_result}")
        permute(nums, tmp_result[:], result) # 尝试不对tmp_result做拷贝的话，会发生什么？
        tmp_result.pop()
        logger.info(f"back tmp_result:{tmp_result}")


if __name__ == "__main__":
    x = [2, 3, 1]
    result = []
    permute(x, [], result)
    print(result)