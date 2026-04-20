# sorted函数（数据容器，reverse= bool）
# 对容器排序，从小到大，不会改变原容器
# 返回值 经过排序的新容器
nums = [10,23,15,5,14,69]
print(sorted(nums,reverse=True))

# len 统计容器中的元素个数 返回值：元素个数
print(len(nums))

# max 返回容器中或多个值中最大值 返回值：最大值
print(max(nums))

# min 返回容器中或多个值中最小值 返回值：最小值
print(min(nums))

# sum 计算容器中元素的总和 返回值：元素总和
# 注意：元素必须是数字类型
print(sum(nums))
