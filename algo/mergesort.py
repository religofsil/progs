# -*- coding: utf-8 -*-

def merge(arr1, arr2):
    """берёт два массива и сливает так, чтобы элементы массива были отсортированы"""
    arr = []  # 1 присвоение значения переменной
    i = 0  # 1 присвоение значения переменной
    j = 0  # 1 присвоение значения переменной
    while i < len(arr1) and j < len(arr2): # 2 сравнения; повторение цикла min(len(arr1), len(arr2)) раз
        if arr1[i] < arr2[j]: # 1 сравнение
            arr.append(arr1[i]) # 1 увеличение массива на 1 элемент
            i += 1  # 1 увеличение переменной
        else:  # 0 операций
            arr.append(arr2[j])  # 1 увеличение массива на 1 элемент
            j += 1 # 1 увеличение переменной

    """min(len(arr1), len(arr2))*5+|len(arr1)-len(arr2)|*3"""
    """adding remains of first array, if any"""
    while i < len(arr1):
        arr.append(arr1[i])
        i += 1

    """adding remains of second array, if any"""
    while j < len(arr2):
        arr.append(arr2[j])
        j += 1
    return arr


def mergesort(arr):
    """takes an array, gives it back sorted"""
    if len(arr) >= 2:
        middle = len(arr) / 2  # the middle of given array
        left = arr[middle:]
        right = arr[:middle]
        left = mergesort(left)
        right = mergesort(right)
        arr = merge(left, right)
    return arr

infile=open('in.txt')
N = int(infile.readline())
for i in xrange(N):
    a = [int(x) for x in infile.readline().split()]
    print mergesort(a)