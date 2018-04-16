from insertion_sort import insertion_sort


def calculate_idx(value, n, max_value):
    '''
        returns bucket index
    '''
    return (value * n) / (max_value + 1)


def bucket_sort(arr):

    n = len(arr)
    max_val = max(arr)
    buckets = [[] for x in range(n)] #create n empty buckets

    #add each array item to correct bucket
    for i in range(n):
        idx = calculate_idx(arr[i], n, max_val)
        buckets[idx].append(arr[i])

    #sort each bucket using insertion sort
    for i in range(n):  
        buckets[i] = insertion_sort(buckets[i])

    #concatenate each bucket
    result = []
    for i in range(n):  
        result += buckets[i]

    return result


if __name__ == "__main__":
    arr = [3, 2, 38, 5, 47, 15, 36, 26, 27, 44, 46, 4]
    print arr
    print bucket_sort(arr)


