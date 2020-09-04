# A Python program to print all  
# permutations of given length 
from itertools import combinations_with_replacement 
from itertools import permutations

def f(x):
    return x * 4 + 6
  
# Get all permutations of length 2 
# and length 2 
q = (1, 3, 4, 7, 12)
comb = combinations_with_replacement(q, 2)  
combos_added = {}
combos_sub = {}
combos_list = []
# Print the obtained permutations 
for i in list(comb): 
    combos_added[i] = f(i[0]) + f(i[1])
    combos_sub[i] = f(i[0]) - f(i[1]) if i[0] >= i[1] else f(i[1]) - f(i[0])
    combos_list.append(i)



"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))

# print(combos_added)
# print(combos_sub)
# print(combos_list)



# Your code here

perms_of_combos = permutations(combos_list, 2) 

equals = {}
  
# Print the obtained permutations 
for i in list(perms_of_combos): 
    if combos_added[i[0]] == combos_sub[i[1]]:
        equals[combos_added[i[0]]] = i
        # equals.append(i[0])
        # equals.append(i[1])
        # equals.append(f"They equal {combos_added[i[0]]}")

print(equals)


# break problem down
# we have the same value for like 1,1 so we shouldn't calculate it again
# we should get the value and store it and access that value everytime we need it
print(f(1) + f(1))







