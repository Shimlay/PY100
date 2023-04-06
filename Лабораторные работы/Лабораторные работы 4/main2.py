def delete(lst, index=None):
    # TODO реализовать функцию удаления элемента из списка по индексу
    if index is None:
        del lst[-1]
    else:
        del lst[index]
    return lst


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
