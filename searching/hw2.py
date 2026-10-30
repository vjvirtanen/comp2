def sequential_search(array, target):
    for i in range(len(array)):

        if array[i] == target:
            return i

    return -1

students = ['alissa','ben','charlie','dianna']
grades = ['b','d','b','a']

print(grades[sequential_search(students, 'charlie')])
