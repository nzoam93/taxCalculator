
def bubbleSortArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                # temp = arr[j+1]
                # arr[j+1] = arr[j]
                # arr[j] = temp
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr

unsortedArr = [11,23,423,233,101,23,2,1,4,3,5,2,3,5,2,4,2,56,23,23]
print(bubbleSortArray(unsortedArr))




def insertionSort(arr):
    for i in range(1,len(arr)): #start off at element #2 so that you can compare it to something on the left
        key_value = arr[i] #the value we are concerned with sorting
        j = i - 1 #we are always looking at the array just to the left of i (one element to the left)
        while j >= 0 and arr[j] > key_value: #stop the loop if we go all the way to the left OR if arr[j] is no longer smaller
            arr[j+1] = arr[j] #have the original key_value position take on all the spots from before it (we will make room for it and shift everything later)
            j -= 1
        arr[j+1] = key_value #actually inserting the value into the spot
    return arr

print(insertionSort(unsortedArr))



def selectionSort(arr):
    sortedArr = []
    for i in range(len(arr)):
        min = 1000000000000000
        for j in range(len(arr)): #gets decremented each time because the array keeps on having one ele removed but it's already accounted for since the len(arr) keeps changing
            if arr[j] < min:
                min = arr[j]
        sortedArr.append(min)
        arr.remove(min)
    return sortedArr

unsortedArr4 = [11,23,423,233,101,23,2,1,4,3,5,2,3,5,2,4,2,56,23,23]
print("selectionSort:", selectionSort(unsortedArr4))


#print(sortArray(unsortedArr))
#print(sortArray2(unsortedArr))

# print(sorted(unsortedArr))
