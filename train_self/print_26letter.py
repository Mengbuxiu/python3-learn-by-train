"""
ord     -返回单个字符的Unicode值
chr     -返回整数对应的字符
map     -该类是可迭代的，接收两个参数，第一个是迭代中要执行的函数，第二个是迭代器
            def __init__(self, func, *iterable) 从这就可以看出
list    -应该是拼接序列吧，具体拼接过程不晓得
"""
print(ord('a'))
print(chr(97))
print(list(map(chr, range(ord('a'), ord('a') + 1))))
print(list(map(chr, range(ord('a'), ord('z') + 1))))

"""
方式差不多
"""
print([chr(x) for x in range(ord('a'), ord('z') + 1)])