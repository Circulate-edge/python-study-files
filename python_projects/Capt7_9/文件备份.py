import os


def write_file(old_filepath, new_filepath):  # 备份文件
    with open(old_filepath, 'rb') as source:  # 读取原文件作为变量source
        with open(new_filepath, 'wb') as target:  # 写入新文件作为变量target
            target.write(source.read())


def copy_dir(old_dir, new_dir):  # 复制目录
    if not os.path.exists(new_dir):  # 新目录的路径不存在
        os.mkdir(new_dir)  # 创建新目录
    dirs = os.listdir(old_dir)  # 获取原目录中的子目录名和文件名列表
    for i in range(len(dirs)):  # 遍历原目录中的每项子目录和文件
        if os.path.isdir(old_dir + '\\' + dirs[i]):  # 该项是目录，准备复制目录
            copy_dir(old_dir + '\\' + dirs[i], new_dir + '\\' + dirs[i])
            print(f'目录《{dirs[i]}》备份成功！')
        elif os.path.isfile(old_dir + '\\' + dirs[i]):  # 该项是文件，准备复制文件
            copy_file(old_dir + '\\' + dirs[i], new_dir + '\\' + dirs[i])
            print(f'文件《{dirs[i]}》备份成功！')


def copy_file(old_filedir, new_filedir):  # 复制文件内容
    new_filepath = os.path.dirname(new_filedir)  # 获取新文件所在目录的路径
    if not os.path.exists(new_filepath):  # 新文件所在目录的路径不存在
        os.mkdir(new_filepath)  # 创建新文件所在目录
    write_file(old_filedir, new_filedir)  # 写入新文件


old_path = input('请输入原文件或目录的路径：')
if os.path.isdir(old_path):  # 是目录
    new_path = input('请输入新目录的路径：')
    copy_dir(old_path, new_path)
elif os.path.isfile(old_path):  # 是文件
    new_path = input('请输入新文件的路径：')
    copy_file(old_path, new_path)
else:
    print('原文件或目录的路径不存在！')
