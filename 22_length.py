def length(l):
    if l==[]:
        return(0)
    else:
        return(l+length(l[1:]))
