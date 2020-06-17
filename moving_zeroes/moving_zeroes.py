'''
Write a function that takes an array of integers and moves each non-zero integer to the left side of the array, then returns the altered array. The order of the non-zero integers does not matter in the mutated array.
'''

def moving_zeroes(arr):

    # array may or may not have zeroes
    # final order doesnt matter

    # swap zeroes with last index thats not already a zero
    for i in range(len(arr)):
        if arr[i] == 0:
            j = len(arr) - 1
            while j > i and arr[j] == 0:
                j -= 1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
    return arr

arr = [0, 3, 1, 0, -2]
print(moving_zeroes(arr))