'''
Given an array of integers, there is a sliding window of size k which is moving from the left side of the array to the right, one element at a time. You can only interact with the k numbers in the window. Return an array consisting of the maximum value of each window of elements.
'''

def sliding_window_max(arr, k):

    output = []
    # loop from k-1 til len(arr) - (k - 1)
    for i in range(len(arr)):
        if i + (k - 1) == len(arr):
            return output
        # compare values in windows size
        highest = arr[i]
        for j in range(1, k):
            if arr[i+j] > highest:
                highest = arr[i+j]
    
        output.append(highest)