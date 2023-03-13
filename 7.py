CH = int(input())
for i in range(1,CH+1):
    K = 0
    if CH % i == 0:
        K += 1
print(K)