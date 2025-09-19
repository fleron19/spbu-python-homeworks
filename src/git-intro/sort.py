def bubbleSort(toSort):
    for i in range(len(toSort)):
        for j in range(i, len(toSort)):
            if toSort[i] > toSort[j]:
                toSort[i], toSort[j] = toSort[j], toSort[i]
    return toSort

print(bubbleSort([2, 7, 6, 12, 1, 9, 4, 7, 3]))
