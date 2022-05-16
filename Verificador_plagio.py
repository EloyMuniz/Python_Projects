import re
def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    #

    a=str(separa_frases(str(separa_sentencas(texto))))
    x=a.replace("[","")
    c=x.replace("]","")
    d=str (separa_palavras(c))
    e=d.replace("\\","")
    f=e.replace("'","")
    g=f.lower()
    h=g.replace('"','')
    i=h.replace(",","")
    j=i.replace(":","")
    k=j.replace(";","")
    l=k.replace("?","")
    
    b = ((n_palavras_diferentes(separa_palavras(l)))/len(texto.split()))
    

    #


    a=str(separa_frases(str(separa_sentencas(texto))))
    x=a.replace("[","")
    p=x.replace("]","")
    d= str(separa_palavras(p))
    e=d.replace("\\","")
    f=e.replace("'","")
    g=f.lower()
    h=g.replace('"','')
    i=h.replace(",","")
    j=i.replace(":","")
    k=j.replace(";","")
    l=k.replace("?","")
    
    c = ((n_palavras_unicas(separa_palavras(l)))/len(texto.split()))



    #
     
    i=len(texto)-len(texto.replace(".",""))
    j=len(texto)-len(texto.replace(" ",""))
    k=len(texto)-len(texto.replace("!",""))
    l=len(texto)-len(texto.replace("?",""))
    d =  ((len(texto)-(i+k+l))/len(separa_sentencas(texto)))
    e = (len(separa_frases(str(separa_sentencas(texto)))))/(len(separa_sentencas(texto)))
    p=len(texto)-len(texto.replace(",",""))
    m =len(texto)-len(texto.replace(" ",""))
    n=len(texto)-len(texto.replace(":",""))
    o=len(texto)-len(texto.replace(";",""))
    s=len(texto)-len(texto.replace(".",""))
    f = (((len(texto)-(p+n+o+s)))/len (separa_frases((str(separa_sentencas(texto))))))
    a = (len(texto)-(i+j+p+o+n))/len(texto.split())
    z = [a,b,c,d,e,f]
    return z



def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    a = as_a
    b = as_b

    

       
        
    d = ((abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])+abs(a[3]-b[3])+abs(a[4]-b[4])+abs(a[5]-b[5]))/6)
        

    return d


    

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    #

    a=str(separa_frases(str(separa_sentencas(texto))))
    x=a.replace("[","")
    c=x.replace("]","")
    d=str (separa_palavras(c))
    e=d.replace("\\","")
    f=e.replace("'","")
    g=f.lower()
    h=g.replace('"','')
    i=h.replace(",","")
    j=i.replace(":","")
    k=j.replace(";","")
    l=k.replace("?","")
    
    b = ((n_palavras_diferentes(separa_palavras(l)))/len(texto.split()))
    

    #


    a=str(separa_frases(str(separa_sentencas(texto))))
    x=a.replace("[","")
    p=x.replace("]","")
    d= str(separa_palavras(p))
    e=d.replace("\\","")
    f=e.replace("'","")
    g=f.lower()
    h=g.replace('"','')
    i=h.replace(",","")
    j=i.replace(":","")
    k=j.replace(";","")
    l=k.replace("?","")
    
    c = ((n_palavras_unicas(separa_palavras(l)))/len(texto.split()))



    #
     
    i=len(texto)-len(texto.replace(".",""))
    j=len(texto)-len(texto.replace(" ",""))
    k=len(texto)-len(texto.replace("!",""))
    l=len(texto)-len(texto.replace("?",""))
    d =  ((len(texto)-(i+k+l))/len(separa_sentencas(texto)))
    e = (len(separa_frases(str(separa_sentencas(texto)))))/(len(separa_sentencas(texto)))
    p=len(texto)-len(texto.replace(",",""))
    m =len(texto)-len(texto.replace(" ",""))
    n=len(texto)-len(texto.replace(":",""))
    o=len(texto)-len(texto.replace(";",""))
    s=len(texto)-len(texto.replace(".",""))
    f = (((len(texto)-(p+n+o+s)))/len (separa_frases((str(separa_sentencas(texto))))))
    a = (len(texto)-(i+j+p+o+n))/len(texto.split())
    z = [a,b,c,d,e,f]
    return z
  


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
    a=[]
    c=[]
    b=ass_cp
    for i in textos:
        a.append (i)
       
    for j in a:
        p = calcula_assinatura(j)
        q =  compara_assinatura(p,b)
     
        c.append(q)

    z=min(c)
    print(c)
    print(z)
    return (c.index(z)+1)
    
        
    






    

