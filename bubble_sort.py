def bubble_sort(arr):
    """冒泡排序：相邻元素两两比较，大的往后沉，每轮把最大值冒泡到末尾"""
    n = len(arr)
    for i in range(n - 1):
        swapped = False  # 本轮是否发生过交换
        for j in range(n - 1 - i):  # 末尾 i 个已排好，无需再比
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # 一轮下来没有交换，说明已经有序，提前结束
            break
    return arr


if __name__ == "__main__":
    data = [5, 2, 9, 1, 7, 3, 8, 6, 4]
    print("排序前:", data)
    print("排序后:", bubble_sort(data))


/*这里是增加选择算法的第一部分*/