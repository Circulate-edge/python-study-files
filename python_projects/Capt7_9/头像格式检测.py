import os

filepath = input('请输入图片路径：')
try:
    with open(filepath, 'rb') as source:
        extension = os.path.splitext(filepath)[1]  # 扩展名
        assert extension == '.jpg' or extension == '.png' or extension == '.jpeg'
        print('图片上传成功！')
except FileNotFoundError as error:
    print('图片路径输入错误！', error)
except PermissionError as error:
    print('没有访问权限！', error)
except AssertionError:
    print('图片格式不是.jpg/png/jpeg！')
