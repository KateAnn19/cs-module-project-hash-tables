# Your code here
import math

import random 

# similar to memoization
# similar to how we looked things up in a hashtable 

# Inverse square root is 1 /square root of number
# Relatively time consuming
# if you know you need to compute this repeatedly it might be good to use a hashtable or lookup table 
def get_inverse_square(num):
    return 1/math.sqrt(num)

get_inverse_square(500)
# we could do work ahead of time
# store the input
# and then we have the work done for us 
# implies we get all the work done ahead of time 

# what should our lookup table look like
    # keys will be numbers
    # values will be results of get_inverse_square 

def build_lookup_table():
    lookup_table = {}
    for i in range(1, 1000):
        lookup_table[i] = get_inverse_square(i)
    # this creates a hash table (dictionary) that can be accessed by index 
    return lookup_table

# we could save this is in a database

sqrt_lookup_table = build_lookup_table()
# you can access it by index because it's a dictionary 
print(sqrt_lookup_table[356])
# you technically could use an array for this since the Keys are numbers (and it might be a slight optimization - though maybe not in Python)



def slowfun_too_slow(x, y):
    # x represents the base and y represents the exponent - this returns the value of x raised to power y 
    pass
    
    # this gives a single ouput number that is the factorial of v and v is the x raised to power of y
    # if (x,y) not in factorials:
    #     factorials[x,y] = math.factorial(v)
    #     v = factorials[x,y]
    # else:
    #     v = factorials[x,y] 
        
    
    
    # this is floor division. It says v equals v (which we now have the factorial of) divided by (x + y) (rounds results down to nearest whole numebr)
    # if (x,y) not in division:
    #     division[x,y] = v //(x+y)
    #     v = division[x,y]
    # else:
    #     v = division[x,y]
    
    # now v has been divided by x + y and rounded down. Now we take v and mod it by this number 
    # if (x,y) not in modulos:
    #     modulos[x,y] = v % 982451653
    #     v = modulos[x,y]
    # else:
    #     v = modulos[x,y] 

    # if we want to create a lookup table what would it look like?
        # it would have key/value pairs. Keys could be x,y and value would be V
    #return v
powers = {}
factorials = {} 
division = {}
results = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    if (x,y) not in results:
        if (x,y) not in powers:
            powers[x,y] = math.pow(x, y)
            factorials[x,y] = math.factorial(powers[x,y])
            division[x,y] = (factorials[x,y])//(x+y)
            results[x,y] = (division[x,y]) % 982451653

    return results[x,y]
    
    

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
