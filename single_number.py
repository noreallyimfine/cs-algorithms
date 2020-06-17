'''
Given a non-empty array of integers where every element appears twice except for one. 
Find that single number. You may assume that there will always be one odd-number-out 
and every other number in the input shows up exactly twice.
'''

def single_number(arr):

    doubles = set()
    # doouble loop through
    for i in range(len(arr)):
        if arr[i] not in doubles:
            for num in arr[i+1:]:
                # if we find double, add to set
                if arr[i] == num:
                        doubles.add(arr[i])
                        break
            # if not return out
            if arr[i] not in doubles:
                return arr[i]


arr = [2, 1, 5, 3, 3, 2, 1]

print(single_number(arr))
    # return number