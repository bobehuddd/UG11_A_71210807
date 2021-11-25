def hitung_hapus():
        sentence = input("Masukkan Kalimat: ")
        mulai = int(input("Index Start :")) + 1
        berhenti = int(input("Index Stop :")) + 1
        hps = berhenti - mulai + 1
        total = (hps/len(sentence))*100

        if mulai > len(sentence) or berhenti > len(sentence):
                return 0.0
        elif total < 0:
                return 0.0
        else:
                return total

print(hitung_hapus())
