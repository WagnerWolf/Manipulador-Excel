import pandas as pd
import pathlib
import os

def manipula(arquivo):
    #abre o arquivo:
    df = pd.read_excel(arquivo)
    
    #adicionando os zeros:
    df['CNPJ/CPF Cliente/Fornecedor'] = df['CNPJ/CPF Cliente/Fornecedor'].apply(lambda x: str(x).zfill(11)).replace('00000000000', '000000001-91')
    df.to_excel('./output/atualizado '+str(arquivo.name),index=False)

files = [f for f in pathlib.Path('input').iterdir() if f.is_file()]
for file in files:
    if pathlib.Path(file).suffix == '.xlsx':
        print('Processando: '+ file.name)
        manipula(file)
for file in files:
    os.remove(file)