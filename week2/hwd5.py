def second_largest(arr):
    arr1 = []

    max = arr[0]
    max1 = arr[0]
    for item in arr :
        if item not in arr1 :
            arr1.append(item)
    for item in arr1 :

        if item > max :
            max = item
            arr1.remove(item)
    for item1 in arr1:

        if item1 > max1:
            max1 = item1

    return max1

print(second_largest([1,1,2,2,3,4,5,6,7,7,8,8]))


