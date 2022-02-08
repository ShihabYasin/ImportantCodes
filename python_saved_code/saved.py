# formatting 0004 etc. i : int  =9
j =  "{:06d}".format(7)
print(j)

#####################################################

# This module provides support for maintaining a list in sorted order without having to sort the list after each insertion.
# TODO: https://stackoverflow.com/questions/27672494/how-to-use-bisect-insort-left-with-a-key
# bisect : https://docs.python.org/3/library/bisect.html
import bisect as bi
r = [-5, 1, 1, 2, 2, 6, 33, 55, 334]
print(bi.bisect_left(r,338))
print(r)
#####################################################
from collections import deque

d = deque()
for x in ["a","b","c", "d"]:
    d.append(x)  # right append
    print (d)

for x in ["l_a","l_b","l_c", "l_d"]:
    d.appendleft(x) # left append
    print (d)


print(f'Pop Left: {d.popleft()}') # pop left
print(f'Pop Right: {d.pop()}')  # pop right

print(d)

#####################################################
# Stack
l = []
for x in [12,3,4]:
    l.append(x) # push
    print(l)

for _ in range(len(l)):
    print(l.pop()) # pop
    print(l)
#####################################################
# Heap
import heapq as heap  # deafult get min heap formation, for max heap negate all
print("Min heap test")
min_heap_list = [3, -4, -1, 15, 6, 79, -1, 0, 3, 44, 9]
heap.heapify (min_heap_list)
heap.heappush (min_heap_list, -100)  # adding new val in heap
for _ in range (0, len (min_heap_list)):
    print (heap.heappop (min_heap_list), end='  ')

# For max heap
print("\nMax heap test")
max_heap_list = [-x for x in [3, -4, -1, 15, 6, 79, -1, 0, 3, 44, 9]]
heap.heapify (max_heap_list)
heap.heappush (max_heap_list, -(-100))  # negating original input(-100) too

for _ in range (0, len (max_heap_list)):
    print ((-1) * heap.heappop (max_heap_list), end='  ') # -1 * to get original vals
#####################################################
# List
l = [0,1,2,3,4,5]
print(f'Reverse: {l[::-1]}')
print(f'Copy: {l[:]}')

delIndex = 3
print(f'DelVal{3}: {l[0:delIndex]+l[delIndex+1:]}')
print(f'AddValLeft: {[100]+l}')
print(f'AddValRight: {l+[99]}') # Or use append()
#####################################################
# Array
r, c  = 5,4 # row , col
arr = [[0 for _ in range(c)] for _ in range(r)] # formation col->row build
arr[1][1]  = 1 # changing val
for rx in range(r): # c style accessing
    for cx in range (c):
        print(arr[rx][cx], end=' ')
    print('')
#####################################################
## Important Itertools
from itertools import permutations, product, zip_longest

a = [1,2,3]
b = [1,2,3,4,5]
for x,y in zip_longest(a,b,fillvalue=-1):
	print(x,y)

# combination
s = 'abcde'
st = set()
for x in permutations(s,2):
	st.add(''.join(sorted(''.join(x))))
print(st)

# permutaiton
s = 'abcde'
for x in permutations(s,2):
	# print(x)
	print(''.join(x), end=' ')

A = 'abc'
B = 'def'
for x in product(A,B): # Cartesian product
	print(x)
#####################################################
# Dict: https://realpython.com/python-defaultdict/
# https://stackoverflow.com/questions/52195897/how-to-create-a-dict-that-can-account-for-unknown-keys














