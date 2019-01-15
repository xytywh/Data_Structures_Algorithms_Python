import re


def is_palindrome_str(str):
    """判断字符串是否是回文串"""
    # 去除任意非字母和数字
    str = re.sub(r'[^\w]', '', str)
    # 两种写法都一样
    # if len(str) <= 1:
    #     return True
    # else:
    #     if str[0].upper() == str[-1].upper():
    #         return is_palindrome_str(str[1:-1])
    #     else:
    #         return False
    if len(str) <= 1:
        return True
    if str[0].upper() != str[-1].upper():
        return False
    """在递归过程中，变化的是str"""
    return is_palindrome_str(str[1:-1])


def is_palindrome_str_1(str, start, end):
    # 去除任意非字母和数字
    str = re.sub(r'[^\w]', '', str)
    # 这里用start>=end，考虑一下为什么
    if start >= end:
        return True
    if str[start].upper() != str[end].upper():
        return False
    """在递归过程中，变化的是开始和结束的下标，而不是str，类似快速排序"""
    return is_palindrome_str_1(str, start + 1, end - 1)


def clear_str(str):
    str = re.sub(r'[^\w]', '', str)
    return str


str = 'Reviled did I live, said I, as evil I did deliver'
str = clear_str(str)
print(is_palindrome_str('aibohphobia'))
print(is_palindrome_str('Live not on evil'))
print(is_palindrome_str('Reviled did I live, said I, as evil I did deliver'))
print(is_palindrome_str('Go hang a salami; I’m a lasagna hog.'))
print(is_palindrome_str('Wassamassaw'))
print(is_palindrome_str('abcdfr'))
print(is_palindrome_str_1(str, 0, len(str) - 1))
