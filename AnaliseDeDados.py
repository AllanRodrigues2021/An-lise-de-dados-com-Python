import os
import pandas as pd 
import plotly.express as px

lista_arquivo = os.listdir(r"---------")
print(lista_arquivo)

tabela_total = pd.DataFrame()

for arquivo in lista_arquivo:
    if 'Vendas' in arquivo:
        tabela =  pd.read_csv(fr"-Desktop\python\Vendas\{arquivo}")
        print(arquivo)
        tabela_total = tabela_total.append(tabela)
print(tabela_total)  

  #-----------------calculo de indicadores e gráficos -------------------#
  
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)
print(tabela_produtos)

#--------------------Cria coluna Faturamento----------------------#

tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
print(tabela_faturamento)

tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']].sort_values(by="Faturamento", ascending=False)
print(tabela_lojas)

#--------------------Gáfico------------------------#

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show()


    
    

