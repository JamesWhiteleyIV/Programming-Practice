

def selection_sort(arr):
    
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr



if __name__ == "__main__":
    arr = [5, 9, 10, 1, 0, 0, 18, 20, 0, 15]

    print arr
    print selection_sort(arr)



    

