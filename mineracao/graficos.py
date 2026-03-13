import matplotlib.pyplot as plt

nome = ['Ricardo', 'João', 'Maria', 'Mauricio']
salario = [2535.25, 2080.50, 3233.96, 5236.52]

plt.bar(nome, salario, color = "red")

plt.xlabel('Nomes')
plt.ylabel('Sálarios')
plt.title('Comparação de sálario')

plt.show()