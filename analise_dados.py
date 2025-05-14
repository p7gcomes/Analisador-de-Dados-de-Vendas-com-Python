import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv('dados.csv')

# Limpeza básica
df.dropna(subset=['Vendas'], inplace=True)
df['Data'] = pd.to_datetime(df['Data'])

# Estatísticas descritivas
print("\nResumo estatístico:")
print(df.describe())

# Total de vendas por produto
vendas_produto = df.groupby('Produto')['Vendas'].sum()
print("\nTotal de vendas por produto:")
print(vendas_produto)

# Gráfico de barras
plt.figure(figsize=(8, 5))
sns.barplot(x=vendas_produto.index, y=vendas_produto.values)
plt.title('Total de Vendas por Produto')
plt.ylabel('Vendas')
plt.xlabel('Produto')
plt.tight_layout()
plt.savefig("vendas_por_produto.png")
plt.show()

# Gráfico de linha: vendas ao longo do tempo
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='Data', y='Vendas', hue='Produto')
plt.title('Vendas ao Longo do Tempo')
plt.tight_layout()
plt.savefig("vendas_tempo.png")
plt.show()
