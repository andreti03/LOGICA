"""RUTINA DPLL Y UNIT PROPAGATE"""

import copy
def is_unit_cl(lista): #Clausula unitaria es aquella en la que solo hay un átomo
    for l in lista:
        if len(l) == 1:
            return True
        elif len(l) == 2 and l[0]== "-":
            return True
    return False


def complemento(n): #El complemento de un átomo es su negación
	x = n
	if x[0] == '-': #Si es negativo, p. ej. -p, se retorna p
		return x[1]
	else: #Si es positivo, p. ej. p, se retorna -p
		return '-' + x


def unit_propagate(S, I):
    #Input: S, un conjunto de formaClausal (Se toma de Tseitin), I, un dicc de interpretaciones (generalmente entra vacío)
    #Output: S, el conjunto de formaClausal modificado, e I, el dicc de interps. modificado
    c_vacia = []
    aux = is_unit_cl(S)
    while(c_vacia not in S and aux):
        for n in S:
            if len(n) == 1:
                l = n[0]
            elif len(n) == 2 and n[0] == "-":
                l = n[0] + n[1]
        T = []
        for y in S:
            if l not in y:
                T.append(y)
        S = copy.deepcopy(T)
        for w in S:
            if complemento(l) in w:
                w.remove(complemento(l))
        if l[0] == '-':
            I[l[1]] = 0
        else:
            I[l] = 1
        aux = is_unit_cl(S)
    return S, I

def DPLL(S, I):
    #Input: S, un conjunto de formaClausal (Se toma de Tseitin), I, un dicc de interpretaciones (generalmente entra vacío)
    #Output: S, el conjunto de formaClausal modificado, Satisfacible/Insatisfacible, e I, el dicc de interps. modificado
    print(len(I)) #Para ver si funciona
    #1: UnitPropagate
    S, I = unit_propagate(S, I)
    #2: Si la clausula vacía está en S->insatisfacible
    c_vacia = []
    if c_vacia in S:
        return "Insatisfacible", {}

    #2: Si S es un conjunto vacío-> Satisfacible
    elif len(S) == 0:
        return "Satisfacible", I

    #4: tomamos un literal no asignado en l
    l = ""
    for clausula in S:
        for literal in clausula:
            if literal not in I.keys():
                l = literal
                break
    lBarra = complemento(l)

    if l == "":
        #print("Error: ya se obtuvo una interpretacion")
        return None
    #5: Definimos S' (S1P) como S sin las clausulas que tienen a l y sin -l de las clausulas restantes
    S1P = copy.deepcopy(S)
    S1P = [clausula for clausula in S1P if not l in clausula]

    for c in S1P:
        if lBarra in c:
            c.remove(lBarra)
    Ip = copy.deepcopy(I)

    #6:Añadimos a I el valor para el que se cumple que VI(l)=1
    if l[0] == '-':
        Ip[l[1]] = 0 #si l es positivo, I(l)=1
    else:
        Ip[l] = 1 #si l es negativo, I(l)=0

    #7: Hacer unitPropagate, y si retorna Satisfacible e I, retornar eso mismo
    S1, I1 = DPLL(S1P, Ip)

    if S1 == "Satisfacible":
        return S1, I1
    #8: Si no retorna satisfacible
    else:
    #9: Definimos S'' (S2P) como S sin las clausulas que contienen a -l y eliminando l de las restantes
        S2P = copy.deepcopy(S)
        for clausula in S2P:
            if complemento(l) in clausula:
                S2P.remove(clausula)
        for clausula in S2P:
            if l in clausula:
                clausula.remove(l)

    #10: Aumentamos I con las interpretaciones que cumplan que V(-l)=1
        Ipp = copy.deepcopy(I)
        if l[0] == '-':
            Ipp[l[1]] = 1
        else:
            Ipp[l] = 0
    #11: Retornamos DPLL de (S'',I'')
        return DPLL(S2P, Ipp)

def conjunto_de_formulas(FNC): #Al final no se utilizó
    #INPUT: Una formula en FNC, p. ejemplo pOqYqOiO-r
    #OUTPUT: lista con la clausulas, p. ejemplo: [pq,qi-r]
    l_claus=[]
    lista=FNC.split("Y")
    for item in lista:
        item=item.replace("O","")
        l_claus.append(item)
    return l_claus
