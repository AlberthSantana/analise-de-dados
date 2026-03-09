from collections import deque

frutas = ["maçã", "banana", "laranja",  "uva", "pêssego"]
print(frutas)

frutas.pop()
print(frutas)

frutas.append("melancia")
print(frutas)

frutas = deque(frutas)
print(frutas)

frutas.popleft()
print(frutas)

frutas.appendleft("maçã")
print(frutas)

for fruta in frutas:
    if fruta == "maçã":
        print(fruta)
    elif fruta == "laranja":
        print(fruta)
