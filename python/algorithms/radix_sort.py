
def radix_sort(arr):

    n = len(arr)
    max_val = max(arr)
    buckets = [[] for x in range(10)] #create n empty buckets
    output = []

    exp = 1
    

    # iterate over each digit's place 1's, 10's ... etc
    while max_val // exp > 0:

        # add each number to correct bucket
        for i in range(n):
            idx = (arr[i] / exp) % 10
            buckets[idx].append(arr[i])

        # re create array in output
        for i in range(10):
            for j in range(len(buckets[i])):
                output.append(buckets[i].pop(0))

        arr = output
        output = []
        exp *= 10

    return arr




if __name__ == "__main__":
    arr = [3, 2, 38, 5, 47, 15, 36, 26, 27, 44, 46, 4]
    print arr
    print radix_sort(arr)


