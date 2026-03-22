def searchIndex(arr: list[int], target: int) -> int:
    """
    二分查找，若找到元素返回索引，没找到返回应插入的位置
    :param arr: 有序数组
    :param target: 目标数
    :return: 索引
    """
    #  initialize左右指针
    left = 0
    right = len(arr) - 1
    #  主循环，当左右指针相遇结束循环
    while left <= right:
        #  二分查找
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

if __name__ == "__main__":
    textArr: list[int|float] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    textNum: int|float = 5.5
    print(searchIndex(textArr, textNum))