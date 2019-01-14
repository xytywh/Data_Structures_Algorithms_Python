def convert_int_to_str(num, decimal):
    """将一个十进制整数转化为二进制到十六进制之间任意进制的字符串形式"""
    str_convert = '0123456789ABCDEF'
    if num < decimal:
        return str_convert[num]
    else:
        return convert_int_to_str(num // decimal, decimal) + str_convert[num % decimal]


print(type(convert_int_to_str(255, 2)), convert_int_to_str(255, 2))
print(type(convert_int_to_str(255, 8)), convert_int_to_str(255, 8))
print(type(convert_int_to_str(255, 10)), convert_int_to_str(255, 10))
print(type(convert_int_to_str(255, 16)), convert_int_to_str(255, 16))
