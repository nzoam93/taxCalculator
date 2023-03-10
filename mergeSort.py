def mergeSort(array):
    if len(array) < 2: #once it eventually splits into just 1 or 0 elements, return that array itself to be merged
        return array
    midpoint = len(array) // 2 #the double "//" sign divides the number and returns the nearest integer, rounded down

    return merge(
        mergeSort(array[:midpoint]), #calls the merge function, which recursively calls the mergeSort function. it makes sense when done with pen and paper
        mergeSort(array[midpoint:]))


def merge(left, right):
    # if len(left) == 0: #optional. This was in the tutorial, but doesn't seem necessary: if the left array is empty, just return the right array. Nothing needs to be merged
    #     return right
    # if len(right) == 0:
    #     return left

    result = []
    left_index = 0
    right_index = 0

    while len(result) < len(left) + len(right): #repeat until you have hit every element
        if left[left_index] <= right[right_index]: # merge the sorted arrays together into a bigger sorted array
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

        if right_index == len(right): #if you've finished adding all the right, then add the rest of the left (kind of like in the vibes game with Max)
            result += left[left_index:]
            break
        if left_index == len(left):
            result += right[right_index:]
            break

    return result #return the sorted array



unsortedArr = [11,101,23,2,1,4,3,5,2,3,5,2,4,2,56,23,23,5,6]
print("mergeSort:", mergeSort(unsortedArr))


def quickSort(arr):
    if len(arr) < 2:
        return arr

    low, same, high = [], [], []

    pivot = arr[len(arr)//2]

    for item in arr:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        else:
            high.append(item)

    return quickSort(low) + same + quickSort(high)


unsortedArr5 = [11,101,23,2,1,4,3,5,2,3,5,2,4,2,56,23,23,5,6]
print("quickSort:", quickSort(unsortedArr5))
