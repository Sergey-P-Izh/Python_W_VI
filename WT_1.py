n=7#skolko chlenov vivest
i=1
acc_an=2
list_=[0]*n
list_[0]=acc_an
print(acc_an)
while i<n:
    acc_an=acc_an-2
    list_[i]=acc_an
    print('nomer elementa: %d,sam element %d'%(i, acc_an))
    i+=1   
print(list_)
print(sum(list_))