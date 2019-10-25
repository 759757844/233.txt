#一行代码实现1—100之和
# x = sum([i for i in range(1,101)])
# print(sum(range(0,101)))
# print(x)

# arr = 'hello world'.split()
# new_arr = f'{arr[0].capitalize()} {arr[1].capitalize()}'
# print(new_arr)

#编程实现计算文件中的大写字母数
# with open('today',mode='r',encoding='utf-8') as f:
#     count = 0
#     for i in f.readline():
#         if i.isupper():
#             count +=1
#     print('大写字母数:',count)

# from collections import Counter
# a = 'ddsasdsadiuyewsgfdwejhfirehg irtuh'
# print(Counter(a))



#九九乘法表
#正序输出
def nine():
    for i in range(1,10):
        for j in range(1,i+1):
            print(f'{j}*{i}={i*j} ',end='')
        print("")
nine()

print('*'*50)
#逆序输出
def nnine():
    for i in range(9,0,-1):
        for j in range(i,0,-1):
            print(f'{j}*{i}={j*i} ',end='')
        print('')
nnine()


