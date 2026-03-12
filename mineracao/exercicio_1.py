import pandas as pd

funcionarios = {
    'nome': ['Alberth', 'Marcelo', 'Kauan', 'Rafael'],
    'endereço': ['Dona clara', 'Tiradentes', 'Fritz loreanz', 'Getulio vargas'],
    'data de nascimento': ["19/08/1989", "25/12/1965", "12/10/2006", "28/02/2003"],
    'data admissão': ["22/02/2022", "15/11/2024", "26/08/2025", "04/06/2020"],
    'salário': [1965.89, 2030.69, 3056.45, 2500.65],
    'cargo': ["Talhador", "Modelista", "Aux.adm", "Revisor"]
}

df = pd.DataFrame(funcionarios)

print(df['data admissão'])