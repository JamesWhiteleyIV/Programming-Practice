def merge(a, b):
    '''
        merges 2 lists
    '''
    c = []

    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])

    if len(a) > 0:
        c += a
    else:
        c += b

    return c
            

def merge_sort(arr):
    '''
        sorts array using divide and conquer merge sort algorithm
    '''

    if len(arr) <= 1:
        return arr

    mid = len(arr) / 2
    a = merge_sort(arr[:mid])
    b = merge_sort(arr[mid:])

    return merge(a, b)


if __name__ == "__main__":
    arr = [5, 9, 10, 1, 0, 0, 18, 20, 0, 15]

    print merge_sort(arr)



    

