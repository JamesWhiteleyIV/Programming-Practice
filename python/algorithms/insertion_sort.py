

def insertion_sort(arr):
    ''' iterative solution '''
    for i in range(len(arr)):
        num = arr[i]
        for j in reversed(range(i)):
            if num < arr[j]:
                arr[j+1] = arr[j]
                arr[j] = num
            else:
                break

    return arr


if __name__ == "__main__":
    arr = [3, 2, 38, 5, 47, 15, 36, 26, 27, 44, 46, 4]
    print arr
    print insertion_sort(arr)
    print '-------------------------------------------'


