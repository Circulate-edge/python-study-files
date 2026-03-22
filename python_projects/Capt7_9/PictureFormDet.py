import os

def check_picture_form(picture):
    """
    Check if the picture is in the correct format
    """
    try:
        pic_form = picture.split(".")[-1]
    except Exception:
        print("图片格式不规范")
        return

    try:
        assert pic_form in ["jpg", "jpeg", "png"], f"不支持文件格式{pic_form}"
    except AssertionError as error:
        print(error)
    else:
        return True

def select(pic, tar_path):
    if os.isfile(pic):
        name = pic.split('.')[-2]
        name = name.split('\\')[-1]
        try:
            bin_file = open(pic, 'rb')
            with open(f"{tar_path}/{name}", 'wb') as new:
                new.write(bin_file)
            print("上传成功")
        except FileNotFoundError:
            print("文件不存在")
        finally:
            bin_file.close()

    else:
        print("上传失败")

if __name__ == "__main__":
    while True:
        pic_name = input("请输入图片路径：")
        if pic_name == "q":
            break
        if check_picture_form(pic_name):
            select(pic_name)