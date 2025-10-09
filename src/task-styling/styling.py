def extendedEuclidean(a, b):
    if a == 0:
        return (b, 0, 1)
    d = extendedEuclidean(b % a, a) # Рекурсивно применяем алгоритм Евклида
    x = d[2] - (b // a) * d[1] # Преобразуем для получения линейного представления
    y = d[1]
    return (d[0], x, y) 
# Возвращаем кортеж из трех чисел, где первое = gcd, второе = коэф. первого числа, третье = коэф второго числа
print(extendedEuclidean(12, 4))
print(extendedEuclidean(25, 15))
