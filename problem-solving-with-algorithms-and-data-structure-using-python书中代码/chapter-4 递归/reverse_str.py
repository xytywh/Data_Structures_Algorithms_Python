def reverse_str(str):
    """反转字符串"""
    if len(str) == 1:
        return str
    else:
        # 下面两种写法都行
        # return str[-1] + reverse_str(str[:-1])
        return reverse_str(str[1:]) + str[0]


print(reverse_str('abcdefg'))
