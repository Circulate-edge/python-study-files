__all__ = ['findOne', 'findTwo']
def findOne(arr: list[int]) -> int:
    """
    在数组中找到唯一一个出现奇数次的数
    :param arr:
    :return: a
    """
    #  将所有元素进行异或运算，成对出现的数字会被抵消为0
    #  最终结果就是那个出现奇数次的数字
    eor = 0
    for i in range(len(arr)):
        eor ^= arr[i]
    return eor

def findTwo(arr: list[int]) -> tuple[int, int]:
    """
    在数组中找到唯二两个出现奇数次的数
    :param arr:
    :return: a, b
    """
    #  求异或和为a^b
    eor = findOne(arr)
    #  eor & (~eor + 1) 提取出 eor 中最右边的1位
    r1 = eor & (~eor + 1)
    #  得到其中一个数 one，另一个数通过 eor ^ one 计算得出
    one = 0
    for i in range(len(arr)):
        if (arr[i] & r1) == r1:
            one ^= arr[i]
    return one, eor ^ one

if __name__ == '__main__':
    arr1 = [1,1,2,2,3,4,4]
    print(findOne(arr1))
    arr2 = [1,1,2,2,3,4,4,5]
    print(findTwo(arr2))