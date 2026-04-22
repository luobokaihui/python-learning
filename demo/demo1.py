# 练习一：水果清单

# 1. 定义一个字典，包含一些水果的名称和价格，例如：苹果，橘子，香蕉等。
fruits = {"苹果": 5, "橘子": 3, "香蕉": 4, "葡萄": 6, "西瓜": 10}

# 打印所有水果

# for key in fruits:
#     print(f'{key}:{fruits[key]}元/斤')

# 找到最贵的水果
# key = max(fruits,key=fruits.get) # type: ignore
# print(f'最贵的水果是:{key},{fruits[key]}元/斤')

# 找到最便宜的水果
# key = min(fruits,key=fruits.get) # type: ignore
# print(f'最便宜的水果是:{key},{fruits[key]}元/斤')

# 练习二 学生成绩表
# 1. 定义一个列表，包含一些学生的姓名和成绩，成绩是字典包含各科成绩，例如：小明，小红，小刚等。
students = [
    {"name": "小明", "scores": {"语文": 85, "数学": 90, "英语": 80}},
    {"name": "小红", "scores": {"语文": 90, "数学": 85, "英语": 95}},
    {"name": "小刚", "scores": {"语文": 80, "数学": 80, "英语": 85}},
    {"name": "小华", "scores": {"语文": 95, "数学": 92, "英语": 88}},
    {"name": "小李", "scores": {"语文": 95, "数学": 92, "英语": 100}},
    {"name": "小丽", "scores": {"语文": 88, "数学": 91, "英语": 90}},
]

# 计算每个学生的平均分
# for stu in students:
#   avg = sum(stu['scores'].values()) / len(stu['scores'])
#   print(f'{stu['name']}学生的平均成绩是：{avg:.1f}')

# 找到总分最高的学生
def find_best():
    best_stu = []
    best_score = 0
    for stu in students:
        total = sum(stu['scores'].values())
        print(f'{total}')
        if total > best_score:
            best_stu = [stu['name']]
            best_score = total
        elif total == best_score:
            best_stu.append(stu['name'])
    print(f'成绩最高的孩子是{best_stu}，总分{best_score}')

find_best()
