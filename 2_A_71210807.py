def ambil_huruf(simbol,sususan= None):
        if sususan == None:
                if len(simbol)%2 == 0:
                        hasil_1 = simbol[int(((len(simbol))/2))]
                else:
                        hasil_1 = simbol[int(((len(simbol) -1)/2))]
                return hasil_1
        else:
                if len(simbol)%2 == 0:
                        hasil_1 = simbol[int(((len(simbol))/2) + sususan)]
                else:
                        hasil_1 = simbol[int(((len(simbol) -1)/2) + sususan)]
                return hasil_1

print(ambil_huruf("abcdefg", 1))
print(ambil_huruf("abcdefg", 2))
print(ambil_huruf("abcd"))
