'''
Write a function that receives an array of integers and returns an array consisting of the product of all numbers in the array except the number at that index.
'''

def product_of_all_other_numbers(arr):

    products = []

    # loop using indexer
    for i in range(len(arr)):

        # init sum
        product = 0
        # inner loop 
        for j in range(len(arr)):
            # if indexers not equal, multcrement sum
            if j != i:
                if product == 0:
                    product += arr[j]
                else:
                    product *= arr[j]
        # set val in new array
        products.append(product)

    return products

