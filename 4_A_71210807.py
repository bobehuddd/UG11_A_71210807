def ambildanbalik(simbol,mulai,akhir,bole):
        if bole == False:
                hslbalik1 = simbol[mulai-1:akhir]
        else:
                hslbalik1 = simbol[akhir-1:mulai-2:-1]
        return hslbalik1

print(ambildanbalik("abcdefg",2,4,True))
print(ambildanbalik("abcdefg",1,5,False))
print(ambildanbalik("qwerty",3,4,True))
print(ambildanbalik("qwerty",2,2,False))
