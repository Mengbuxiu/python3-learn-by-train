import codecs
import json

"""
整理我的书签,没写完 ε=(´ο｀*)))
"""


#   递归实现
def produce_link(dict):
    con = []
    for v in dict.values():
        if type(v) == "__dict__":
            if v['children']:
                book_str = []
                for l in v['children']:
                    book_str.append(l)
                return book_str
            else:
                con.append(produce_link(v.values()))
        else:
            pass
    return con


local = r"C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Default\Bookmarks"

# with open(local, 'r') as f:
#     contents = f.read().decode('utf-8')
#     print(contents)

#   如果open时使用的encoding和文件本身的encoding不一致的话，那么这里将会产生错误
f = codecs.open(local, 'r', encoding='utf-8')
content = f.read()
# print(content)
bookmark_d = json.loads(content)
# print(type(bookmark_d))
print(produce_link(bookmark_d))

