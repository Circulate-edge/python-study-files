"""
Artificial intelligence is an important driving force for the new round of technological revolution and industrial transformation.
It is a new technological science that studies and develops theories, methods, technologies, and application systems for simulating, extending, and expanding human intelligence.
Artificial intelligence is an important component of the field of intelligence, attempting to understand the essence of intelligence and produce a new type of intelligent machine that can respond in a way similar to human intelligence.
Artificial intelligence is a very broad science, including robotics, language recognition, image recognition, natural language processing, expert systems, machine learning, computer vision, and more.
"""
text = """
Artificial intelligence is an important driving force for the new round of technological revolution and industrial transformation.
It is a new technological science that studies and develops theories, methods, technologies, and application systems for simulating, extending, and expanding human intelligence.
Artificial intelligence is an important component of the field of intelligence, attempting to understand the essence of intelligence and produce a new type of intelligent machine that can respond in a way similar to human intelligence.
Artificial intelligence is a very broad science, including robotics, language recognition, image recognition, natural language processing, expert systems, machine learning, computer vision, and more.
"""
text = text.lower()  # 字母小写化
text = text.replace(',', '')
text = text.replace('.', '')
words = text.split()  # 分割
frq_dict = {}  # 创建字典
for word in words:  # 在words列表中遍历得到word
    if word not in frq_dict:
        frq_dict[word] = words.count(word)
# print(frq_dict)
# sort_dict
frq_dict = dict(sorted(frq_dict.items(), key=lambda x: x[1], reverse=True))  # 用匿名函数排序
for key, value in frq_dict.items():
    print(f"{key}:{value}")