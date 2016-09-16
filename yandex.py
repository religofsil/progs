nk=raw_input("").split(" ")
n=int(nk[0])
k=int(nk[1])
allkinds=range(1, k+1)
raw_trees=raw_input("").split(" ")
trees=[]
for tree in raw_trees:
    trees.append(int(tree))
def finder(trees=trees, i=0, n=0):
    while sorted(list(set(trees[:i])))!=allkinds:
        i+=1
    else:
        stop=i
    while sorted(list(set(trees[n:i])))==allkinds:
        n+=1
    else:
        start=n
    return start, stop
arr=[]
print finder()[0], finder()[1]
for x in range(n):
    print finder(trees[x:])
