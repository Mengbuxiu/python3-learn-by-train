d = {'x': 1, 'y': 2}
print(d.popitem())      # 随机弹出一个项
print(d)
print(dict.update(d, {'x': 111}))  # 使用字典的项更新另一个字典
print(d)