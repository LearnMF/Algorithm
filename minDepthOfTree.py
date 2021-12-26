# -*- coding: utf-8 -*-
'''
@Author: tanbo
@Time: 2021/12/25 5:32 下午
@File: minDepthOfTree.py
'''
import loguru
logger = loguru.logger

class Node(object):
    def __init__(self, left,right,val):
        self.left = left
        self.right = right
        self.val = val


def min_depth_of_tree(tree):
    """
    BFS
    note:for循环中的对象q是可变对象，如果一边取一边增加，会造成死循环！
    :param tree: Node
    :return:
    """
    if not tree:
        return 0
    q = [tree]
    depth = 1
    while q:
        nex_q = []
        for i in q:
            if not i.left and not i.right: #
                return depth
            if i.left:
                nex_q.append(i.left)

            if i.right:
                nex_q.append(i.right)

        depth += 1
        q = nex_q
    return depth


if __name__ == "__main__":
    node_1 = Node(left=None, right=None,val=10)
    node0 = Node(left=None, right=None, val=11)
    node1 = Node(left=node0, right=node_1, val=14)
    node2 = Node(left=None, right=None, val=7)
    node3 = Node(left=node1, right=node2, val=15)
    print(min_depth_of_tree(node3))
