import pandas as pd
import random

def gerar_palpites(dezenas_loteria, palpite_loteria, quantidade):
    palpites = []
    for i in range(quantidade):
        numeros = random.sample(range(1, dezenas_loteria+1), palpite_loteria)
        numeros.sort()
        palpites.append(numeros)
    return palpites
    

def contabilizar_resultados_loteria(tipo, numeros_apostados):
    # Carregar o arquivo XLSX
    file = pd.read_excel('/DEV/Loteria/dados/quina_asloterias_ate_concurso_6184_sorteio.xlsx', engine='openpyxl')

    # Inicializar contadores
    duques = 0
    ternos = 0
    quadras = 0
    quinas = 0
    senas = 0

    # Percorrer cada linha da tabela
    for index, row in file.iterrows():
        numeros_sorteio = row[['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5']].values.tolist()
        
        # Aqui você pode adicionar sua lógica de verificação dos números da loteria
        # Por exemplo, você pode comparar os números com os números apostados

        # Exemplo de lógica de verificação (números sorteados são 1, 2, 3, 4, 5, 6)
        acertos = sum([1 for num in numeros_sorteio if num in numeros_apostados])
        
        if acertos == 2:
            duques += 1
        elif acertos == 3:
            ternos += 1
        elif acertos == 4:
            quadras += 1
        elif acertos == 5:
            quinas += 1
        elif acertos == 6:
            senas += 1

    # Exibir os resultados
    print(f"Duques encontradas: {duques}")
    print(f"Ternos encontradas: {ternos}")
    print(f"Quadras encontradas: {quadras}")
    print(f"Quinas encontradas: {quinas}")
    print(f"Senas encontradas: {senas}")

    if quadras >= 1:
        return "yes"

# Chamada da função

dezenas_loteria = input("Loteria de 01 a quanto? ")
dezenas_loteria = int(dezenas_loteria)

palpite_loteria = input("Palpite de quantas dezenas? ")
palpite_loteria = int(palpite_loteria)

quantidade = input("Quantos palpites deseja? ")
quantidade = int(quantidade)

rand_chars = input("Digite frases aleatorias para random: ")
random.seed(rand_chars)

palpites = gerar_palpites(dezenas_loteria, palpite_loteria, quantidade)

i = 1
x = 0
for palpite in palpites:
    print(f"Palpite n. {i} - {palpite}")
    achei = contabilizar_resultados_loteria('Quina', palpite)
    if achei == "yes":
        print("Achei um bom palpite")
        x += 1
    i += 1
print(f"Achei {x} palpites bons")