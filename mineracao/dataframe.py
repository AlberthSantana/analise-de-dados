import pandas as pd 

data = {
    'nome': ["Alberth", "Arthur", "Samira", "Franciele"],
    'Idade': [36, 8, 6, 31],
    'Cidade': ["Campo Grande", "Rio dos cedros", "Timbó", "Ribas do rio pardo"]
}

df = pd.DataFrame(data)

print(df)

#acessar prpriedade especifica
print(df['nome'])

#acessar um linha
print(df.iloc[0])

#acessar valor especifico da linha
print(df.loc[1, 'Cidade'])