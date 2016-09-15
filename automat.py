print "Hi!"
x=raw_input('type Latin infinitive: ')
## кортеж: x=(1, 2, 3)
n=1
transitions={(1, 'a'):2, (1, 'e'):2, (1, 'i'):2, (2, 'a'):2, (2, 'e'):2, (2, 'i'):2, (2, 'r'):3, (3, 'e'):4, (4, 'a'):2, (4, 'i'):2, (4, 'e'):2}
for i in x:
    if n==1 and i not in 'aei':
        n=1
    elif (n, i) in transitions:
        n=transitions[(n, i)]
    else:
        n=1
if n==4:
    print "Congratulations, you can type!"
else:
    print 'No, I said "Latin infinitive"'
