# for i in range(1,6):
#     for j in range(i):
#         print('*',end="")
#     print()
count = 3
while count > 0:
    name_user = input('输入用户名：')
    password = input('输入密码：')
    if name_user == 'doctor' and password == '023333':
        print('登陆成功')
        break
    else:
        print("用户名或密码不正确")
        count -= 1
        print('您还有%d次机会'%count)
        if count == 0:
            print('输入错误次数多，请稍后再试')
# for word in "python":
#     if word == 'o':
#         continue
#     print(word,end='')