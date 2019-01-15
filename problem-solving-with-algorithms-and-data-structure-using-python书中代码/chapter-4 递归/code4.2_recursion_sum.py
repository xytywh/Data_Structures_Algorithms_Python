def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    # 下面两句都行，等价的
    return list_sum(num_list[:-1]) + num_list[-1]
    # return num_list[0] + list_sum(num_list[1:])


print(list_sum([1, 3, 5, 7, 9]))
