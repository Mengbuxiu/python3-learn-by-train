def flatten(nested):
    try:
        #   不迭代类似字符串的对象
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for ele in flatten(sublist):
                yield ele
    except TypeError:
        yield nested


print(list(flatten([[1, 2], [3, 4]])))
# print(list(flatten([['ab'], ['cd']])))
