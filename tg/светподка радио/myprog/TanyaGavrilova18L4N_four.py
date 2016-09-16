q=1
t=1
ls=['']
while q==1:
    l=raw_input('please, enter the word ')
    b=l.split( )
    #slogno=re.search(\W, l)
    #if slogno='':
        #print("It is not a word")
        #continue
    if l=='':
        t=0
        q=0
    elif b[0]!=l:
        print("It is not a word")
        continue
    else:
        ls[0]=l
        q=0
while t==1:
    l=raw_input('please, enter the word ')
    if l=='':
        break
    b=l.split( )
    if b[0]!=l:
        print("It is not a word")
        continue
    ls.insert(0,l)
for i in range(0,len(ls)):
    print(ls[i])
    
