start = int(input("Digite número inicial da contagem: "))
last = int(input("Digite número final da contagem: "))

for i in range(start, last + 1):
    if (i % 2) == 0:
        print(i, end= " ")