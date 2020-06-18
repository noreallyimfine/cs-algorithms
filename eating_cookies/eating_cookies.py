'''
Cookie Monster can eat either 1, 2, or 3 cookies at a time. If he were given a jar of cookies with n cookies inside of it, how many ways could he eat all n cookies in the cookie jar? Implement a function eating_cookies that counts the number of possible ways Cookie Monster can eat all of the cookies in the jar.

For example, for a jar of cookies with n = 3 (the jar has 3 cookies inside it), there are 4 possible ways for Cookie Monster to eat all the cookies inside it:

He can eat 1 cookie at a time 3 times
He can eat 1 cookie, then 2 cookies
He can eat 2 cookies, then 1 cookie
He can eat 3 cookies all at once.
Thus, eating_cookies(3) should return an answer of 4.

Can you implement a solution that runs fast enough to pass the large input test?
'''

def eating_cookies(n, cache=None):

    # Tribonnacci
    if cache is None:
        cache = {0:1, 1:1, 2:2}
    
    if n in cache:
        return cache[n]
    
    else:
        print(cache)
        cache[n] = (eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache))
        return cache[n]

print(eating_cookies(9))