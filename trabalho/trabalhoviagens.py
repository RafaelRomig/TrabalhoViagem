import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
import scipy.stats as stats

df = pd.read_csv('C:\\Users\\Rafael\\Documents\\TrabalhoViagens\\Viagem_limpo.csv')

# Função para plotar o gráfico de boxplot
def plot_boxplot():
    sns.set_theme(style="whitegrid")
    ax = sns.boxplot(x=df["valor_total"])
    plt.title('Boxplot para valor_total')
    plt.show()

# Função para plotar o histograma
def plot_histogram():
    plt.hist(df_aux.valor_total)
    plt.title('Frequência por valor total')
    plt.show()

# Função para plotar o histograma com 22 bins
def plot_histogram_22_bins():
    df_aux.valor_total.hist(bins=22)
    plt.title('Distribuição por Valor Total - Viagens 2016')
    plt.show()

# Função para plotar o histograma com cores por orgao_solicitante
def plot_histogram_color():
    grafico = px.histogram(df_aux, x="valor_total", nbins=22, color='orgao_solicitante')
    grafico.update_layout(width=1500, height=1000, title_text='Distribuição Valor Total - Orgao Solicitante')
    grafico.show()

# Função para plotar a matriz de correlação
def plot_correlation_matrix():
    numeric_columns_encoded = df_aux_encoded[['valor_diarias', 'valor_passagens', 'valor_devolucao', 'valor_outros_ gastos', 'valor_total']]
    corr_encoded = numeric_columns_encoded.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_encoded, annot=True, cmap='coolwarm', linewidths=.5)
    plt.title('Matriz de Correlação para df_aux_encoded')
    plt.show()

# Função para plotar o scatter plot entre valor_diarias e valor_total
def plot_scatter_value_diarias():
    sns.scatterplot(data=df_aux, x=df_aux['valor_diarias'], y=df_aux['valor_total'])
    plt.title('Scatter plot entre valor_diarias e valor_total')
    plt.show()

# Função para plotar o scatter plot entre valor_passagens e valor_total
def plot_scatter_value_passagens():
    sns.scatterplot(data=df_aux, x=df_aux['valor_passagens'], y=df_aux['valor_total'])
    plt.title('Scatter plot entre valor_passagens e valor_total')
    plt.show()

# Função para plotar o scatter plot entre valor_passagens e valor_diarias
def plot_scatter_passagens_diarias():
    sns.scatterplot(data=df_aux, x=df_aux['valor_passagens'], y=df_aux['valor_diarias'])
    plt.title('Scatter plot entre valor_passagens e valor_diarias')
    plt.show()

# Função para plotar o gráfico de barras de contagem de ocorrências por orgao_solicitante
def plot_barplot():
    dfgraph = df_aux.groupby(['orgao_solicitante']).size().reset_index(name='COUNT')
    dfgraph = dfgraph.sort_values('COUNT')
    dfgraph = dfgraph[dfgraph['COUNT'] > 10000].sort_values('COUNT', ascending=False)
    plt.figure(figsize=(15, 8))
    sns.barplot(data=dfgraph, x='COUNT', y='orgao_solicitante', orient='h')
    plt.title('Gráfico de barras de contagem de ocorrências por orgao_solicitante')
    plt.show()

# Função para plotar o gráfico de probabilidade
def plot_probability_plot():
    stats.probplot(df_aux_encoded['valor_total'], dist="norm", plot=plt)
    plt.title("Normal Q-Q plot")
    plt.show()

# Função para executar o teste estatístico Mann-Whitney U
def run_mannwhitneyu():
    stat, p = stats.mannwhitneyu(df_inss['valor_total'], df_pf['valor_total'])
    print('Estatística de teste: {}'.format(stat.round(2)))
    print('p-valor: {}'.format(p))
    input("Pressione Enter para continuar...") 

# Função para mostrar estatísticas para o INSS
def show_inss_stats():
    print(df_inss['valor_total'].describe())
    input("Pressione Enter para continuar...")

# Função para mostrar estatísticas para a Polícia Federal
def show_pf_stats():
    print(df_pf['valor_total'].describe())
    input("Pressione Enter para continuar...")

# Convertendo datas
df['data_ini'] = pd.to_datetime(df['data_ini'], format='%d/%m/%Y')
df['data_fim'] = pd.to_datetime(df['data_fim'], format='%d/%m/%Y')

# Excluindo linhas com valor total = 0.00
df = df[df['valor_total'] != 0.00]

# Filtrando valores de valor_total menores que 1600
df_aux = df[df['valor_total'] < 1600]

# Codificando variáveis categóricas usando one-hot encoding
df_aux_encoded = pd.get_dummies(df_aux, columns=['orgao_solicitante'])

# Selecionando apenas as colunas numéricas relevantes
numeric_columns_encoded = df_aux_encoded[['valor_diarias', 'valor_passagens', 'valor_devolucao', 'valor_outros_ gastos', 'valor_total']]

# Scatter plot entre valor_diarias e valor_total
warnings.filterwarnings("ignore", category=FutureWarning)
sns.set()

# Contagem de ocorrências por orgao_solicitante
dfgraph = df_aux.groupby(['orgao_solicitante']).size().reset_index(name='COUNT')
dfgraph = dfgraph.sort_values('COUNT')
dfgraph = dfgraph[dfgraph['COUNT'] > 10000].sort_values('COUNT', ascending=False)

# Filtrando DataFrames por orgao_solicitante
df_inss = df_aux_encoded[df_aux_encoded['orgao_solicitante_Instituto Nacional do Seguro Social'] == 1]
df_pf = df_aux_encoded[df_aux_encoded['orgao_solicitante_Departamento de Polícia Federal'] == 1]
df_mte = df_aux_encoded[df_aux_encoded['orgao_solicitante_Ministério do Trabalho e Emprego - Unidades com vínculo direto'] == 1]

# Loop interativo para receber a entrada do usuário e mostrar o gráfico correspondente
while True:
    print("Escolha um gráfico para visualizar:")
    print("A - Boxplot para valor_total")
    print("B - Histograma de frequência por valor total")
    print("C - Histograma com 22 bins")
    print("D - Histograma com cores por orgao_solicitante")
    print("E - Matriz de Correlação")
    print("F - Scatter plot entre valor_diarias e valor_total")
    print("G - Scatter plot entre valor_passagens e valor_total")
    print("H - Scatter plot entre valor_passagens e valor_diarias")
    print("I - Gráfico de barras de contagem de ocorrências por orgao_solicitante")
    print("J - Gráfico de probabilidade")
    print("K - Executar teste estatístico Mann-Whitney U")
    print("L - Mostrar estatísticas para o INSS")
    print("M - Mostrar estatísticas para a Polícia Federal")
    print("X - Sair")

    choice = input("Digite a letra correspondente (ou 'X' para sair): ").upper()

    if choice == 'A':
        plot_boxplot()
    elif choice == 'B':
        plot_histogram()
    elif choice == 'C':
        plot_histogram_22_bins()
    elif choice == 'D':
        plot_histogram_color()
    elif choice == 'E':
        plot_correlation_matrix()
    elif choice == 'F':
        plot_scatter_value_diarias()
    elif choice == 'G':
        plot_scatter_value_passagens()
    elif choice == 'H':
        plot_scatter_passagens_diarias()
    elif choice == 'I':
        plot_barplot()
    elif choice == 'J':
        plot_probability_plot()
    elif choice == 'K':
        run_mannwhitneyu()
    elif choice == 'L':
        show_inss_stats()
    elif choice == 'M':
        show_pf_stats()
    elif choice == 'X':
        print("Saindo do programa.")
        break
    else:
        print("Escolha invalida. Tente novamente.")
        input("Pressione Enter para continuar...")

