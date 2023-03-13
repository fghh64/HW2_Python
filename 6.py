FAC = 1
OTV = 1
CH = int(input())
for i in range(1,CH+1):
    FAC = FAC * i
    OTV = OTV + (FAC**-1)
print(OTV)