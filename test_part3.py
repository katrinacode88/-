# -*- coding: utf-8 -*-
"""
Part III 练习2 —— 用 unittest 写出至少 5 个单元测试用例并执行
针对 part3_function_class.py 中的 max_depth 函数进行测试。
"""

import unittest
from part3_function_class import max_depth


class TestMaxDepth(unittest.TestCase):
    """测试 max_depth 函数"""


    def test_flat_list(self):
        """平铺列表，深度为 1"""
        self.assertEqual(max_depth([1, 2, 3]), 1)

    def test_nested_example(self):
        """题目给出的例子 [[1], [2, [3]]]，深度为 3"""
        self.assertEqual(max_depth([[1], [2, [3]]]), 3)

    def test_empty_list(self):
        """空列表也是一个列表，深度为 1"""
        self.assertEqual(max_depth([]), 1)

    def test_deeply_nested(self):
        """多层嵌套 [[[[1]]]]，深度为 4"""
        self.assertEqual(max_depth([[[[1]]]]), 4)

    def test_mixed(self):
        """混合嵌套 [1, [2, [3, [4]]], 5]，深度为 4"""
        self.assertEqual(max_depth([1, [2, [3, [4]]], 5]), 4)

    def test_non_list(self):
        """非列表元素，深度为 0"""
        self.assertEqual(max_depth(5), 0)


if __name__ == "__main__":
    unittest.main()
