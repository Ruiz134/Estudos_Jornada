lista: list = [64, 34, 25, 12, 22, 11, 90]

def somar_lista(lista_para_somar):
    soma = 0
    for i in lista_para_somar:
        soma += i
    
resultado = somar_lista(lista)
print(resultado)
