from datetime import datetime


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    # 计数器 记录学号
    count = 0

    # 初始化方法
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        Student.count += 1
        self.stu_id = f"{datetime.now().year}{Student.count:03d}"
        self.scores = {}

    # 给学生添加成绩
    def add_score(self, subject, score):
        self.scores[subject] = score

    # 计算平均成绩
    def calce_avg(self):
        if self.scores:
            avg = sum(self.scores.values()) / len(self.scores)
            return f"{avg:.1f}"
        else:
            return 0

    # 魔法方法
    def __str__(self):
        return f"{self.name}-{self.age}-{self.gender}-{self.stu_id}-{self.scores}-{self.calce_avg()}"


class Manager:
    def __init__(self):
        self.stu_list = []

    # 添加学生
    def add_student(self):
        name = input("请输入姓名")
        age = int(input("请输入年龄"))
        gender = input("请输入性别")
        stu = Student(name, age, gender)
        self.stu_list.append(stu)
        print(f"{stu.stu_id}")

    # 删除学生
    def del_stu(self):
        sid = input("请输入删除学生的学号")
        target = None
        for stu in self.stu_list:
            if stu.stu_id == sid:
                target = stu
                break

        if target is None:
            print(f"{sid}不存在")
        else:
            self.stu_list.remove(target)
            print(f"删除成功")

    # 展示所有学生
    def show_stu(self):
        if self.stu_list:
            for stu in self.stu_list:
                print(stu)
        else:
            print("暂无学生")

    # 给指定学生添加成绩
    def set_score(self):
        sid = input("请输入学号")
        for stu in self.stu_list:
            if sid == stu.stu_id:
                score_str = input("请输入成绩（学科-分数,学科-分数）")
                score_list = score_str.replace('，',',').split(',')
                for item in score_list:
                    subject, score = item.split('-')
                    subject = subject.strip()
                    score = float(score.strip())
                    stu.add_score(subject, score)
                print('添加成功')
                return
        print('学生不存在')

    def run(self):
        while True:
            print(f"{'*' * 10 }学生管理{'*' * 10 }")
            print(f"1.添加学生")
            print(f"2.删除学生")
            print(f"3.查看所有学生")
            print(f"4.录入成绩")
            print(f"5.退出\n")
            chocie = input('请输入操作编号:')
            if chocie == '1':
                self.add_student()
            elif chocie == '2':
                self.del_stu()
            elif chocie == '3':
                self.show_stu()
            elif chocie == '4':
                self.set_score()
            elif chocie == '5':
                print('再见')
                break
            else:
                print('输入有误')

M1 = Manager()
M1.run()
