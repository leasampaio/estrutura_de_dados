def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista)-1
    while baixo<= alto:
        meio = int((baixo+alto)/2)
        chute = lista[meio]
        print(alto, meio, baixo)
        if chute == item:
            return meio
        if chute> item:
            alto =meio-1
        else:
            baixo= meio+1
lista = [1, 2, 3, 4, 5, 6]
print(busca_binaria(lista, 2))