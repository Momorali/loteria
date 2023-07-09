import pandas as pd

def contabilizar_resultados_loteria(tipo):
    # Carregar o arquivo CSV
    file = pd.read_csv('caminho/do/arquivo.csv')

    # Inicializar contadores
    quadras = 0
    quinas = 0
    senas = 0

    # Percorrer cada linha da tabela
    for index, row in file.iterrows():
        numeros_sorteio = row[['dz1', 'dz2', 'dz3', 'dz4', 'dz5', 'dz6']].values.tolist()
        
        # Aqui você pode adicionar sua lógica de verificação dos números da loteria
        # Por exemplo, você pode comparar os números com os números apostados

        # Exemplo de lógica de verificação (números sorteados são 1, 2, 3, 4, 5, 6)
        numeros_apostados = [1, 2, 3, 4, 5, 6]
        acertos = sum([1 for num in numeros_sorteio if num in numeros_apostados])
        
        if acertos == 4:
            quadras += 1
        elif acertos == 5:
            quinas += 1
        elif acertos == 6:
            senas += 1

    # Exibir os resultados
    print(f"Quadras encontradas: {quadras}")
    print(f"Quinas encontradas: {quinas}")
    print(f"Senas encontradas: {senas}")

# Chamada da função
contabilizar_resultados_loteria('mega-sena')
