print('请输入学生成绩，输入‘结束’停止录入')
score_list = []

while True:
    data = input('请输入成绩：')
    if data == '结束':
        break
    else:
        score_list.append(int(data))
if score_list:
    print('具体的统计代码')
    # 统计平均分
    avg = sum(score_list) / len(score_list)
    # 合格人数
    pass_count = 0
    # 优秀人数
    excellent_count = 0
    for item in score_list:
        if item >= 60:
            pass_count += 1
        if item >= 90:
            excellent_count += 1
    # 合格率
    pass_rate = pass_count / len(score_list) * 100
    # 优秀率
    excellent_rate = excellent_count / len(score_list) * 100
    print(f'****统计信息如下****')
    print(f'总人数:{len(score_list)}\n合格人数:{pass_count},合格率:{pass_rate}\n优秀人数:{excellent_count},优秀率:{excellent_rate}')
else:
    print('没有输入任何成绩')
