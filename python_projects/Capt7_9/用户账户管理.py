def read_info(filename):
    with open(filename, mode='r+') as file:
        info_dict = {}
        for line in file:
            info = line.strip('\n')
            info = info.split()
            info_dict[info[0]] = info[1]
    return info_dict


def write_info(filename, info_dict):
    with open(filename, mode='w+') as file:
        for key, value in info_dict.items():
            file.write(key + ' ' + value + '\n')


print('欢迎使用用户账户管理程序！')
while True:
    choice = input('1.用户注册\n2.用户登录\n3.用户注销\n4.修改密码\n0.退出\n')
    info_dict = read_info('user.txt')
    if choice == '1':
        username = input('请注册用户名：')
        if username in info_dict.keys():
            print('用户名已存在！')
        else:
            while True:
                password = input('请输入密码：')
                password2 = input('请再次输入密码：')
                if password == password2:
                    info_dict[username] = password
                    write_info('user.txt', info_dict)
                    print('注册成功！')
                    break
                else:
                    print('两次密码不一致！')

    elif choice == '2':
        username = input('请输入用户名：')
        password = input('请输入密码：')
        if username in info_dict.keys() and password == info_dict[username]:
            print('登录成功！')
        else:
            print('用户名或密码错误！')

    elif choice == '3':
        username = input('请输入用户名：')
        password = input('请输入密码：')
        if username in info_dict.keys() and password == info_dict[username]:
            info_dict.pop(username)
            write_info('user.txt', info_dict)
            print('注销成功！')
        else:
            print('用户名或密码错误！')

    elif choice == '4':
        username = input('请输入用户名：')
        password = input('请输入密码：')
        if username in info_dict.keys() and password == info_dict[username]:
            while True:
                password3 = input('请修改密码：')
                password4 = input('请确认新密码：')
                if password4 == password3:
                    info_dict[username] = password3
                    write_info('user.txt', info_dict)
                    print('密码修改成功！')
                    break
                else:
                    print('两次密码不一致！')

        else:
            print('用户名或密码错误！')
    else:
        break
