# -*- coding: utf-8 -*-
"""
Part II 练习 —— 语句：选择与循环
包含 3 个练习：
  1. 用户登录系统
  2. 十进制转二进制（不用内置函数）
  3. 十进制转十六进制（不用内置函数）
"""


def login_system():
    """练习1：简单的用户登录系统，最多尝试 3 次"""
    saved_username = "admin"
    saved_password = "123456"
    max_attempts = 3

    for attempt in range(max_attempts):
        username = input("请输入用户名：")
        password = input("请输入密码：")
        if username == saved_username and password == saved_password:
            print("登录成功！")
            return True
        remaining = max_attempts - attempt - 1
        print(f"用户名或密码错误！剩余尝试次数：{remaining}")

    print("已达到最大尝试次数，登录失败！")
    return False


def dec_to_bin(n):
    """练习2：十进制转二进制（不用内置函数）"""
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = str(n % 2) + result  # 余数拼到前面
        n = n // 2
    return result


def dec_to_hex(n):
    """练习3：十进制转十六进制（不用内置函数）"""
    if n == 0:
        return "0"
    digits = "0123456789ABCDEF"  # 十六进制的 16 个字符
    result = ""
    while n > 0:
        result = digits[n % 16] + result
        n = n // 16
    return result


def main():
    print("请选择要运行的练习：")
    print("  1. 用户登录系统")
    print("  2. 十进制转二进制")
    print("  3. 十进制转十六进制")
    choice = input("请输入编号（1/2/3）：")

    if choice == "1":
        login_system()
    elif choice == "2":
        num = int(input("请输入一个十进制数："))
        print(f"{num} 的二进制是：{dec_to_bin(num)}")
    elif choice == "3":
        num = int(input("请输入一个十进制数："))
        print(f"{num} 的十六进制是：{dec_to_hex(num)}")
    else:
        print("输入无效，请重新运行程序。")


if __name__ == "__main__":
    main()
