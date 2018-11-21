import codecs
import json

"""
整理我的书签,没写完 ε=(´ο｀*)))
经搜索发现，多层嵌套的字典，再机器学习的决策树中也有使用
其实再仔细想想，这tm不就是多叉树的递归遍历吗，so，待续
"""


#   递归实现
def produce_link(dict):
    con = []
    if type(dict).__name__ == "dict":
        for v in dict.values():
            print(v)
            # if v['children']:
            #     book_str = []
            #     for l in v['children']:
            #         book_str.append(l)
            #         return book_str
            # else:
            #     con.append(produce_link(v.values()))
    else:
        try:
            produce_link(dict.values())
        except KeyError:
            print("遍历到底了-----")
            return
    return con


#   local = r"C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Default\Bookmarks" win7
local = r"C:\Users\Lenovo\AppData\Local\Google\Chrome\User Data\Default\Bookmarks"      # win10

# with open(local, 'r') as f:
#     contents = f.read().decode('utf-8')
#     print(contents)

#   如果open时使用的encoding和文件本身的encoding不一致的话，那么这里将会产生错误
f = codecs.open(local, 'r', encoding='utf-8')
content = f.read()
# print(content)
bookmark_d = json.loads(content)
# print(type(bookmark_d))
val = produce_link(bookmark_d)
print(val)

