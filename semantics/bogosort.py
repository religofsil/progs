import random

arr = [1, 2, 87, 6, 9, 0, 4, 2345, 67, 8, 0, 4]
i=1
while arr != sorted(arr):
    print i, 'still not sorted'
    random.shuffle(arr)
    i+=1
print 'sorted!', arr
