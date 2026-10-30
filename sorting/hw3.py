def insertion_sort(array):
    for i in range(1, len(array)):
        val = array[i]
        j = i - 1

        while j >= 0 and array[j] > val:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = val

    return array


array = [9, 7, 2, 11]
print(insertion_sort(array))