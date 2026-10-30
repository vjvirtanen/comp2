def selection_sort(array):
    n = len(array)
    for i in range(n - 1):

        min_idx = i

        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
              
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]

        print(array)

#selection_sort([-4, 11, 7, -12, 6, 1])

def bubble_sort(array):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False

        print(array)

bubble_sort([-4, 11, 7, -12, 6, 1])