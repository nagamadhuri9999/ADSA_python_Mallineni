def merge_lists(L1,L2):
    i,j=0,0 
    res=[]
    while i<len(L1) and j<len(L2):
        if L1[i]<=L2[j]:#i=0,j=0: L1[0]<L2[0],1<2 
            res.append(L1[i])
            i+=1 
        elif L1[i]>L2[j]:#i=0,j=0: L1[0]<L2[0],1<2
            res.append(L2[j])
            j+=1 
    res.extend(L1[i:])
    res.extend(L2[j:])
    return res
ans=merge_lists([1,5,6],[2,3,5,7,8])
print(ans)
#[1,2,3,5,5,6,7,8]