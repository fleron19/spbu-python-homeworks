def bubble_sort(to_sort):
    for i in range(len(to_sort)):
        for j in range(i, len(to_sort)):
            if to_sort[i] > to_sort[j]:
                to_sort[i], to_sort[j] = to_sort[j], to_sort[i]
    return to_sort

print(bubble_sort([2, 7, 6, 12, 1, 9, 4, 7, 3]))
