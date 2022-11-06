class Elemento:
    def __init__(self):
        self.valor = 0
        self.prox = None
        self.ant = None
primeiro = Elemento()
primeiro.valor = 0
primeiro.prox = primeiro
primeiro.ant = primeiro

def busca (chave, primeiro):
    ultimo =primeiro.ant
    if((ultimo != None) and (chave <= ultimo.valor)):
        pont =primeiro.prox
        while(pont.valor < chave):
            pont = pont.prox
        return pont 
    else:
        return primeiro

def inclusao(chave, primeiro):
    pont = busca(chave, primeiro)
    if((pont == primeiro) or (chave != pont.valor)):
        anterior = pont.ant
        novo = Elemento()
        novo.valor = chave
        novo.prox = pont
        novo.ant = anterior
        anterior.prox = novo
        pont.ant = novo
        print("elemento incluido")
    else:
        print("Elemento já existe na lista")

def remocao (chave,primeiro):
    pont = busca(chave, primeiro)
    if((pont!= primeiro) and (pont.valor == chave)):
        anterior = pont.ant
        proximo = pont.prox
        anterior.proximo = proximo
        proximo.ant = anterior
        del pont
    else:
        print("Chave não existe")

inclusao(0, primeiro)
inclusao(0, primeiro)
remocao(0, primeiro)
busca(0, primeiro)