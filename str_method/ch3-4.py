# coding=utf-8
import string

print("aaa".center(9, '-'))

print("zlsssslz".find('l'))  # 返回最低索引，从0开始
print("zlsssslz".rfind('l'))  # 返回最高索引，从0开始

print("abcsa".rindex('a'))

print('-'.join(['1', '2', '3']))
#  print('-'.join(['1', '2', '3', 4]))  # error!

print('/'.join(['', 'usr', 'bin', 'env']))
print('C:'+'\\'.join(['', 'usr', 'bin', 'env']))

print("ABC".lower())
print("that's all gifts!".title())  # 识别单词的方式有问题  That'S All Gifts!
print(string.capwords("that's all gifts!"))  # That's All Gifts!

print("This is a test!".replace('!', '~'))
print("This is a test!".replace('!', '').split())

print("** hello, word**!".strip(" *!"))  # 注意strip中共包含三个字符 ，lstrip rstrip 了解一下

# k => c, z => s, del blank. 单字符替换，能够同时替换多个字符，效率高于replace
print("this is a test case".translate(str.maketrans('cs', 'kz', ' ')))