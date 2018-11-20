def fun_a():
    return 1


x = y = fun_a()
print(type(x))

#   print(input("请输入名字：") or 'unknow')

print(sorted('Bac', key=str.lower))

for i in range(10):
    if i == 17:
        print(i)
        break

else:
    print('aa')