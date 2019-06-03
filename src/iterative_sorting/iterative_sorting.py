# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
         for j in range(cur_index, len(arr)):  # O(n)
            if arr[j] < arr[smallest_index]:  # O(1)
                smallest_index = j  # O(1)
        temp = arr[cur_index]  # O(1)
        arr[cur_index] = arr[smallest_index]  # O(1)

        arr[smallest_index] = temp  # O(1)
    
    return arr
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        # TO-DO: swap


# TO-DO:  implement the Bubble Sort function below
# compare 
def bubble_sort( arr ):


    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr