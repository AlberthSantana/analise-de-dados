class Carro:
    def __init__(self, modelo, placa, ano):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

    def mostrarPlaca(self):
        print(self.placa)

carro1 = Carro("Corsa", "A028G3", 2020)

carro1.mostrarPlaca()