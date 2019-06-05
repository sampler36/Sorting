# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    i = 0
    j = 0
    k = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            k += 1
            i += 1
        else:
            merged_arr[k] = arrB[j]
            k += 1
            j += 1
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        k += 1
        i += 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k += 1
        j += 1
    
    return merged_arr

 
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        l = merge_sort(arr[0: len(arr) // 2])
        r = merge_sort(arr[len(arr)//2:])
        arr = merge(l, r)
    return arr
 


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    # L = arr[start:mid]
    # R = arr[mid:end+1]
    # L.append()
    # R.append()
    # i = j = 0

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO
#    if l < r:
#        center = (l + r) //2
#        merge_in_place(arr, l, center)
#        merge_in_place(arr, center+1, r)
#        merge(arr, l, center, r)

   return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
