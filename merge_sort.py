import shutil
columns = shutil.get_terminal_size().columns

def Merge(array, copy, low, mid, high):
    k,i = low,low
    j = mid+1
    while i<=mid and j<=high:
        if array[i]<=array[j]:
            copy[k] = array[i]
            i += 1
            k += 1
        else:
            copy[k]=array[j]
            j += 1
            k += 1
    #filling the remaining
    while i<=mid:
        copy[k] = array[i]
        i += 1
        k += 1
    for i in range(low, high+1):
        array[i] = copy[i]

def MergeSort(array, copy, low, high):
    if low == high:
        return
    mid = (low + ((high-low) >>1))
    #left
    MergeSort(array, copy, low, mid)
    #right
    MergeSort(array, copy, mid+1, high)
    #time to merge!
    Merge(array, copy, low, mid, high)

def IsSorted(array):
    prev = array[0]
    for i in range(1,n):
        if prev > array[i]:
            print("Merge Fails!!")
            return False
        prev = array[i]
    return True

if __name__=="__main__":
    print("MERGE SORT".center(columns))

    while True:
        array = input("\nInput the numbers separated by commas: ").split(",")
        array = [int(x) for x in array]
        n = len(array)
        copy = array.copy()
        MergeSort(array,copy, 0, n-1)

        if IsSorted(array):
            print(array)

        ask = input("\nWanna Continue? [y/n]: ").lower()
        if ask == "y":
            continue
        elif ask == "n":
            exit()
