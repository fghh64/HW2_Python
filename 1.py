n = int(input()) 
for i in range(2,n): #начинаем цикл от числа 2 до нашего вводного числа
    if n % i == 0: #если вводное число делится на число из цикла без остатка оно его принтует
        print(i)
        break # остановили работу что бы было только 1 число