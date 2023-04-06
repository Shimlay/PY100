list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее арифметическое уникальных чисел

unique_nums = set(list_)
sum_unique = sum(unique_nums)
count_unique = len(unique_nums)
mean_unique = sum_unique/count_unique

print(sum_unique)
print(count_unique)
print(round(mean_unique, 5))
