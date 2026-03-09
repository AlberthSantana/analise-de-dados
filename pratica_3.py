from collections import deque

lista = [1,2,3,4]
print(lista)

lista.pop()
print(lista)

lista = deque()

lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
print(lista)

lista.popleft()
print(lista)
