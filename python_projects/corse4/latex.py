text = r"人工智能（artificial intelligence）,英文缩写为AI:" \
       r"  是新一轮科技革命和产业变革的重要驱动力量," \
       r"  是研究、开发用于模拟、延伸和扩展人的智能的理论、方法、技术及应用系统的一门新的技术科学.\r\n" \
       r"  人工智能是智能学科重要的组成部分,它企图了解智能的实质,并生产出一种新的能以与人类智能相似的方式做出反应的智能机器." \
       r"人工智能是十分广泛的科学,包括:机器人,语言识别,图像识别,自然语言处理,专家系统,机器学习,计算机视觉等.\r\n" \
       r"  人工智能大模型带来的治理挑战也不容忽视!  马斯克指出,在人工智能机器学习面具之下的本质仍然是统计." \
       r"    营造良好创新生态,需做好前瞻研究,建立健全保障人工智能健康发展的法律法规、制度体系、伦理道德." \
       r"      着眼未来,在重视防范风险的同时,也应同步建立容错、纠错机制,努力实现规范与发展的动态平衡."
while True:
    choice = input("请选择（1）删除空格；（2）英文标点替换；（3）段落分割；（4）字母大写；（0）退出:")
    if choice == '1':
        text = text.replace(' ', '')
        print(text)
    elif choice == '2':
        text = text.replace(',', '，')
        text = text.replace('.', '。')
        text = text.replace('?', '？')
        text = text.replace(':', '：')
        text = text.replace('!', '！')
        text = text.replace(';', '；')
        print(text)
    elif choice == '3':
        resultFind = text.find(r"\r\n")
        if resultFind != -1:
            text = text.split(r"\r\n")
        else:
            text = text.split(r"\R\N")
        text = ("\n".join(text))
        print(text)
    elif choice == '4':
        text = text.upper()
        print(text)
    elif choice == '0':
        break
    else:
        print("False!")