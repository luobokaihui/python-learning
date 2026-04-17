def cal_total(*nums):
    """
    description:
    计算总运动量

    params:
    运动个数

    returns:
    运动总数

    raises:
    """
    return sum(nums)

def cal_avg(total,days= 7):
    """
    :description:计算平均值

    :param total: 总运动量（个）
    :param days: 天数

    :returns:平均值

    :raises:
    """

    return total / days

def check_success(total,goal=120):
    """:Description:是否合格

      :Params:
        total 总天数
        goal 合格数

      :Returns:
        是否合格

      :Raises:
    """
    if total >= goal:
        return '恭喜!挑战成功!'
    else:
        return '抱歉！挑战失败！'

def main(title,duration):
    """:Description: 挑战赛开始

      :Params:
        title:挑战项目
        duration:挑战天数

      :Returns:
        挑战开始

      :Raises:
    """
    print(f'【{title}】【{duration}天】挑战赛（请输入每天的数量）')

main('俯卧撑',14)
