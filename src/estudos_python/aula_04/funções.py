# Implementação do algoritmo de ordenação por seleção
lista = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

# Ordenando a lista
print("Lista ordenada com função personalizada:", lista)



#--------------------------------------------------------------

# Lista de exemplo
lista_exemplo = [64, 34, 25, 12, 22, 11, 90]

# Ordenando a lista com sort()
lista_exemplo.sort()

print("Lista ordenada com método built-in:", lista_exemplo)

