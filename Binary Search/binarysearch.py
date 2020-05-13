#Binary Search Algorithm implementation
def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1
    index = int(end/2)

    if len(arr)==0:
        return "N/A"

    else:
        while True:

            if target == arr[index]:
                return arr[index], index
            
            elif start == end:
                return "N/A"

            elif target > arr[index]:
                start = index + 1
                index = int((start+end)/2)

            elif target < arr[index]:
                end = index - 1
                index = int((start+end)/2)


#l = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
#l = [5,7]
#print(binarySearch(l , 7))