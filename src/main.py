
import pandas as pd
import sqlite3

def main():
    print("Projeto iniciado com sucesso! Vamos dominar Python e Dados!")
    # Lê o arquivo CSV
    df = pd.read_csv("data/processed/alunos_limpos.csv")

    # Mostra as 5 primeiras linhas
    print("\n Primeiras linhas do dataset:")
    print(df.head())

    # Estatísticas básicas
    print("\n Estatísticas gerais:")
    print("Média das notas:", df['nota'].mean())
    print("Mediana das idades:", df['idade'].median())
    print("Maior nota:", df['nota'].max())
    print("Menor nota:", df['nota'].min())
    print("Desvio padrão das notas:", df['nota'].std())

    # Conecta com bando de dados SQLite e cria a tabela 'alunos'
    conn = sqlite3.connect("data/database/escola.db")
    df.to_sql("alunos", conn, if_exists="replace", index=False)
    conn.close()

    # Nova conexão para consultar dados com SQL
    conn = sqlite3.connect("data/database/escola.db")

    print("\nConsulta SQL: Alunos com nota maior que 7")
    consulta1 = pd.read_sql_query("SELECT * FROM alunos WHERE nota > 7", conn)
    print(consulta1)

    print("\nConsulta SQL: Média de nota por idade")
    consulta2 = pd.read_sql_query("""
        SELECT idade, AVG(nota) as media_nota
        FROM alunos
        GROUP BY idade
        ORDER BY idade
    """, conn)                      
    print(consulta2)

    print("\nConsulta SQL: Aluno com maior nota")
    consulta3 = pd.read_sql_query("""
        SELECT aluno, nota
        FROM alunos
        ORDER BY nota DESC
        LIMIT 1
    """, conn)
    print(consulta3)

    # Fechando conexão
    conn.close()                                                       
                                  

    print("\n Dados inseridos com sucesso no banco SQLite em 'data/database/escola.db'!")


    #Resumo completo:
    print("\n Resumo completo com describe():")
    print(df.describe())

    #Contagem de nomes repetidos:
    print("\n Frequência de nomes:")
    print(df['aluno'].value_counts())

    #Média da nota por idade:
    print("\n Média de nota por idade:")
    print(df.groupby('idade')['nota'].mean())

    # Alunos com nota maior que 7
    print("\n Alunos com nota maior que 7:")
    print(df[df['nota']>7])

    #Ordenar alunos por nota(decrescente)
    print("\n Alunos ordenados por nota (decrescente):")
    print(df.sort_values(by='nota', ascending=False))

    # Salva os alunos com nota acima de 7 em um novo arquivo CSV
    df[df['nota'] > 7].to_csv("data/processed/alunos_aprovados.csv",index=False)

    print("\n Arquivo 'alunos_aprovados.csv' salvo em data/processed/")

    # Salva os alunos ordenados por nota (decrescente)
    df.sort_values(by='nota', ascending=False).to_csv("data/processed/alunos_ordenados.csv", index=False)

    print("Arquivo 'alunos_ordenados.csv' salvo em data/processed/")

    print("\n valores ausentes por coluna:")
    print(df.isnull().sum())

    df['nota'] = df['nota'].fillna(0) # Preenche notas nulas com 0
    df.drop_duplicates(inplace=True) # Remover duplicadas
    df.rename(columns={"nome": "aluno"}, inplace=True) # Renomear colunas
    df['idade'] = df['idade'].astype(int) # Alterar tipo de dados (ex: string --> int)
    df.to_csv("data/processed/alunos_limpos.csv", index=False) # Salvar dados limpos
    
    #Gráficos
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize=(8, 5))
    sns.barplot(x='aluno', y='nota', data=df)
    plt.title("Notas por Aluno")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8,5))
    sns.histplot(df['nota'], bins=5, kde=True)
    plt.title("Distribuição das Notas")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    sns.histplot(df['nota'], bins=5, kde=True)
    plt.title("Distribuição das Notas")
    plt.xlabel("Nota")
    plt.ylabel("Frequência")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    sns.barplot(x='aluno', y= 'nota', data=df)
    plt.title("Notas por Aluno")
    plt.xlabel("Aluno")
    plt.ylabel("Nota")
    plt.tight_layout()

    # Salvar em arquivo
    plt.savefig("visualizations/notas_por_aluno.png")

    # Exibir o gráfico nomalmente
    plt.show()

    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='idade', y='nota', data=df)
    plt.title("Nota vs Idade")
    plt.xlabel("Idade")
    plt.ylabel("Nota")
    plt.tight_layout()
    plt.savefig("visualizations/scatter_idade_nota.png")
    plt.show()

    plt.figure(figsize=(6,4))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.title("Mapa de Correlação")
    plt.tight_layout()
    plt.savefig("visualizations/heatmap_correlacao.png")
    plt.show()

    sns.pairplot(df)
    plt.savefig("visualizations/pairplot_dados.png")
    plt.show()

    print("\nmédia das notas por idade")
    media_nota_idade= df.groupby('idade')['nota'].mean()
    print(media_nota_idade)
                                                                         
    


if __name__ == "__main__":
    main()




    

