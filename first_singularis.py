word=0
while word!="!":
    word=raw_input("type something please:")
    letters=list(word)
    letters.reverse()
    l=letters[0:3:1]
    print(l)
    if l==["s", "i", "t"]:
        print ("2pl")
    elif l[1]=="o" and l[0]=="r":
        print ("1sg.praes.ind.pass.")
    elif l[0]=="o":
        print ("1sg.praes.ind.act.")
    elif l[0]=="!":
        print ("goodbye!")
    else:
        print ("something else")
