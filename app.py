# Contador zerado para a quantidade de vezes que "excelente", "bom" e "ruim" foram escolhidos.
excelente = 0
bom = 0
ruim = 0

# Laço de repetição para analisar a resposta dos 50 entrevistados.
for i in range (50):
    
    nome = str(input("Digite o seu nome:\n-> "))
    idade = int(input("Digite a sua idade:\n->" ))
       
    while True:
        avaliacao = input("Digite a nota de avaliação\n1 para EXCELENTE\n2 para BOM\n3 para RUIM:\n-> ")
        
        # Caso o usuário responda "excelente", "bom" ou "ruim", será contado para os contadores zerados.
        match avaliacao:
            
            case "1":
                excelente += 1
                break
            case "2":
                bom += 1
                break
            case "3":
                ruim += 1
                break
            case _: # Caso o usuário responda algo diferente do que o programa prevê, retornará para o input de "avaliacao"
              print ("\nPor favor digite uma nota váida para a pesquisa.")
              
# Exibição dos contadores após o fim da entrevista.
print ("\n----------PESQUISA DE AVALIAÇÃO----------\n")
print(f"Excelente: {excelente}\n")
print(f"Bom: {bom}\n")
print(f"Ruim: {ruim}\n")              