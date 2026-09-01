# -*- coding: utf-8 -*-
"""
Part I 练习 —— 数据类型
题目：用字典和列表表示一个班的期末考试成绩（学号、姓名、班级、高数、英语、Java编程……），
     并求出单科第一、总分第一的学生名单、挂科的学生名单。
"""

# 1. 用「列表 + 字典」表示一个班的期末考试成绩
#    列表里的每一个元素是一个字典，代表一个学生
students = [
    {"学号": "001", "姓名": "张三", "班级": "1班", "高数": 92, "英语": 85, "Java编程": 78},
    {"学号": "002", "姓名": "李四", "班级": "1班", "高数": 55, "英语": 88, "Java编程": 90},
    {"学号": "003", "姓名": "王五", "班级": "2班", "高数": 78, "英语": 92, "Java编程": 66},
    {"学号": "004", "姓名": "赵六", "班级": "2班", "高数": 61, "英语": 59, "Java编程": 95},
    {"学号": "005", "姓名": "孙七", "班级": "1班", "高数": 88, "英语": 76, "Java编程": 82},
    {"学号": "006", "姓名": "周八", "班级": "2班", "高数": 40, "英语": 70, "Java编程": 58},
]

# 考试科目（除学号/姓名/班级这些基本信息外）
subjects = ["高数", "英语", "Java编程"]
PASS_LINE = 60  # 及格线


def find_top_in_subject(stu_list, subject):
    """找出某科目成绩最高的学生名单（允许并列）"""
    top_score = max(s[subject] for s in stu_list)
    top_names = [s["姓名"] for s in stu_list if s[subject] == top_score]
    return top_score, top_names


def main():
    # ---- 2. 求单科第一 ----
    print("=" * 30)
    print("单科第一名")
    print("=" * 30)
    for subject in subjects:
        top_score, top_names = find_top_in_subject(students, subject)
        print(f"{subject}：最高分 {top_score} 分，第一名：{', '.join(top_names)}")

    # ---- 3. 求总分第一 ----
    print("\n" + "=" * 30)
    print("总分第一名")
    print("=" * 30)
    for s in students:
        s["总分"] = sum(s[sub] for sub in subjects)  # 计算每个学生的总分
    max_total = max(s["总分"] for s in students)
    top_total_names = [s["姓名"] for s in students if s["总分"] == max_total]
    print(f"总分最高 {max_total} 分，第一名：{', '.join(top_total_names)}")

    # ---- 4. 挂科学生名单（任一科 < 60 分即视为挂科）----
    print("\n" + "=" * 30)
    print("挂科学生名单")
    print("=" * 30)
    has_fail = False
    for s in students:
        failed = [sub for sub in subjects if s[sub] < PASS_LINE]
        if failed:
            has_fail = True
            print(f"{s['姓名']}（{s['班级']}）挂科科目：{', '.join(failed)}")
    if not has_fail:
        print("无人挂科")


if __name__ == "__main__":
    main()
