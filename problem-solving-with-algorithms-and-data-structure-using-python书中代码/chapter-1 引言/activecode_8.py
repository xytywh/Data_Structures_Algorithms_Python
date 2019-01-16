wordlist = ['cat', 'dog', 'rabbit']
letterlist = []
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
print(letterlist)

wordlist = ['cat', 'dog', 'rabbit']
letterlist = []
for aword in wordlist:
    for aletter in aword:
        if aletter not in letterlist:
            letterlist.append(aletter)
print(letterlist)

# 注意嵌套循环的顺序，和原来一致，下面的第二种写法是错误的
letterlist = [aletter for aword in wordlist for aletter in aword]
# letterlist = [aletter for alettter in aword for aword in wordlist]
print(letterlist)
# 去除重复元素
print(list(set(letterlist)))
