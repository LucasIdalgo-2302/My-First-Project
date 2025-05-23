

import pandas as pd

def main():
    print("Projeto iniciado com sucesso! Vamos dominar Python e Dados!")
    # Lê o arquivo CSV
    df = pd.read_csv("data/raw/alunos.csv")

    # Mostra as 5 primeiras linhas
    print("\n Primeiras linhas do dataset:")
    print(df.head())

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
    
if __name__ == "__main__":
    main()




    

