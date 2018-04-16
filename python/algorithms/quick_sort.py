

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    store_idx = 1

    for i in range(store_idx, len(arr)):
        if arr[i] < arr[0]:  # arr[0] == pivot
            arr[i], arr[store_idx] = arr[store_idx], arr[i]
            store_idx += 1

    arr[0], arr[store_idx - 1] = arr[store_idx - 1], arr[0]

    first = quick_sort(arr[:store_idx - 1])
    second = quick_sort(arr[store_idx:])
    first.append(arr[store_idx - 1])

    return first + second


if __name__ == "__main__":
    arr = [3, 2, 38, 5, 47, 15, 36, 26, 27, 44, 46, 4]

    print arr
    print quick_sort(arr)
        


