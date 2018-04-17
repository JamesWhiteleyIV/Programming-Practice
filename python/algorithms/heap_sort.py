
def heapify(arr, i, n):
    ''' creates max heap for array representation of complete binary tree '''

    # init largest to parent idx    
    largest = i

    # get left and right children idx
    l = 2 * i + 1
    r = 2 * i + 2

    # check if left child exists and is > root
    if l < n and arr[i] < arr[l]:
        largest = l

    # check if right child exists and is > root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # swap root if needed
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]

        heapify(arr, largest, n)
        


def heap_sort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, i, n)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, 0, i)



if __name__ == "__main__":
    arr = [3, 2, 38, 5, 47, 15, 36, 26, 27, 44, 46, 4]
    print arr
    heap_sort(arr)
    print arr


