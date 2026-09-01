# -*- coding: utf-8 -*-
"""
Part III 练习 —— 函数与类
包含：
  1. 求列表最大嵌套深度的函数
  2. （单元测试见 test_part3.py，至少 5 个用例）
  3. User 类（first_name、last_name、describe_user、greet_user）
  4. Admin 类（继承 User，含 privileges 属性和 show_privileges 方法）
"""


def max_depth(lst):
    """练习1：返回列表的最大嵌套深度。
    例如：[1, 2, 3] 的深度为 1，[[1], [2, [3]]] 的深度为 3。
    """
    if not isinstance(lst, list):
        return 0  # 非列表，深度为 0
    max_d = 1
    for item in lst:
        if isinstance(item, list):
            depth = 1 + max_depth(item)
            if depth > max_d:
                max_d = depth
    return max_d


class User:
    """练习3：表示一个普通用户"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """打印用户信息"""
        print(f"用户信息：{self.first_name} {self.last_name}")

    def greet_user(self):
        """打印问候语"""
        print(f"你好，{self.first_name} {self.last_name}！欢迎回来！")


class Admin(User):
    """练习4：管理员，是一种特殊的用户（继承 User）"""

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # privileges 属性：存储权限的字符串列表
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """显示管理员的全部权限"""
        print(f"{self.first_name} 拥有的权限：")
        for p in self.privileges:
            print(f"  - {p}")


def main():
    # 演示练习1：嵌套深度
    print("=" * 30)
    print("列表嵌套深度")
    print("=" * 30)
    print("[1, 2, 3] 的深度 =", max_depth([1, 2, 3]))
    print("[[1], [2, [3]]] 的深度 =", max_depth([[1], [2, [3]]]))

    # 演示练习3：User 类
    print("\n" + "=" * 30)
    print("User 类")
    print("=" * 30)
    user = User("Jiang", "Yefei")
    user.describe_user()
    user.greet_user()

    # 演示练习4：Admin 类
    print("\n" + "=" * 30)
    print("Admin 类")
    print("=" * 30)
    admin = Admin("Zhang", "San")
    admin.describe_user()
    admin.greet_user()
    admin.show_privileges()


if __name__ == "__main__":
    main()
