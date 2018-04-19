# Magic Index 

# brute force O(n)
def magic(arr):
    for i in range(len(arr)):
        if i == arr[i]:
            return i
    return None

# optimized O(log n) using binary search
def magic_opt(arr, start=0, end=None):

    if end is None:
        end = len(arr) - 1

    if end < start:
        return None

    mid = (start+end) / 2

    if mid == arr[mid]:
        return mid

    if mid < arr[mid]:
        return magic_opt(arr, start=mid+1, end=end)
    else:
        return magic_opt(arr, start=start, end=mid-1)


if __name__ == "__main__":
    arr = [1, 2, 4, 5, 5, 5]
    print magic(arr)

    arr = [1, 2, 4, 5, 5, 5]
    print magic_opt(arr)

    arr = [1, 2, 4, 10, 90, 999]
    print magic_opt(arr)
