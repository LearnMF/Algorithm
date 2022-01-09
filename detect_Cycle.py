# -*- coding: utf-8 -*-
'''
@Author: tanbo
@Time: 2022/1/2 4:48 下午
@File: detect_Cycle.py
已知链表中含有环,返回环的起始位置
'''


def detect_cycle(head):
    """

    :param head: ListNode
    :return:
    """
    fast = slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    slow = head
    while slow != fast:
        fast = fast.next
        slow = slow.next

    return slow