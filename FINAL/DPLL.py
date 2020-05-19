"""FUNCIONES UNITPROPAGATE Y DPLL"""

def conjunto_de_formulas(FNC):
    #INPUT: Una formula en FNC, p. ejemplo pOqYqOiO-r
    #OUTPUT: lista con la clausulas, p. ejemplo: [pq,qi-r]
    l_claus=[]
    lista=FNC.split("Y")
    for item in lista:
        item=item.replace("O","")
        l_claus.append(item)
    return l_claus

#print(conjunto_de_formulas("pOqYqOiO-rY-sOz"))

def unitPropagate(S,I):
    #INPUT: S, lista de clausulas e I, dicc de interpretaciones
    #OUTPUT: S, lista de clausulas e I, dicc de interpretaciones (MODIFICADOS)
    unitaria = False
    C = []

    while len(S)!=0:
        for claus in S:
            if len(claus)==1: #Si es una clausula unitaria (positiva)
                l = claus
                unitaria = True
                break
            elif (len(claus)==2 and claus[0]=='-'): #Si es una clausula unitaria (negativa)
                l = claus
                unitaria = True
                break
        if unitaria == True: #Se van a buscar las clausulas que tengan el unitario
            C = S[:]
            count = 0
            for cl2 in S:
                C[count]=cl2
                for ctdr in range(len(cl2)):
                    if len(l) == 1:#Positiva
                        if (cl2[ctdr] == '-' and cl2[ctdr+1] == l):#Si en la clausula elegida se encuentra la negación del unitario
                            leng = len(cl2)
                            C[count] = C[count].replace('-'+C[count][ctdr+1],'')#Se borra la negación de la clausula
                            if len(C[count])<leng:
                                break
                        elif cl2[ctdr] == l: #Si se encuentra la unitaria, se borra
                            C.remove(C[count])
                            count-=1

                    elif len(l) == 2:#Negativa
                        if cl2[ctdr] == l[1]:
                            leng = len(cl2)
                            C[count]= C[count].replace(C[count][ctdr],'')#Si se encuentra la positiva, se elimina de la clausula
                            if len(C[count])<leng:
                                break
                        elif (cl2[ctdr] == '-' and cl2[ctdr+1] == l[1]):
                            C.remove(C[count])#Si se encuentra la negativa se elimina
                            count-=1
                            break

                count+=1
            S = C[:] #S es una copia de C con las nuevas claususlas
            if len(l) == 1:
                I[l[0]]=1
            elif len(l)==2:
                I[claus[1]]=0
            unitaria=False
        else:
            break
    return S,I

#Prueba de la función
#print(unitPropagate(["-p-q","-rpq","-r"],{}))


def DPLL(S,I):
    #INPUT: S, lista de clausulas e I, dicc de interpretaciones
    #OUTPUT: "Satisfacible" o "insatisfacible" y dicc de interpretaciones

    #1: UnitPropagate
    S,I = unitPropagate(S,I)
    #2: Si la clausula vacía está en S-> insatisfacible
    clau_vacia = ""
    if clau_vacia in S:
        return "Insatisfacible" ,{}
    #3: Si S es un conjunto vacío-> Satisfacible
    elif len(S)==0:
        return "Satisfacible" ,I
    #4:tomamos un literal no asignado en l
    SP = S[:]
    count = 0
    for claus in S:
        SP[count] = claus
        for i in range(len(claus)):
            if claus[i] not in I.keys():
                if claus[i] != '-':
                    l = claus[i]
                    break
        break
    #5: Definimos S' (SP) como S sin las clausulas que tienen a l y sin -l de las clausulas restantes
    for claus in S:
        for i in range(len(claus)):
            if len(l) == 1:
                if (claus[i] == '-' and claus[i+1] == l): #Si encontramos la negación->se elimina de la clausula
                    leng = len(claus)
                    SP[count] = SP[count].replace('-'+SP[count][i+1],'')
                    if len(SP[count])<leng:
                        break
                elif claus[i] == l: #Si encontramos el literal-> se elimina de SP
                    SP.remove(SP[count])
                    count-=1
        count+=1
    #6:Añadimos a I el valor para el que se cumple que VI(l)=1
    S = SP[:]
    if len(l) == 1:
        I[l]=1 #si l es positivo, I(l)=1
    elif len(l)==2:
        I[l]=0 #si l es negativo, I(l)=0

    #7: Hacer unitPropagate, y si retorna Satisfacible e I, retornar eso mismo
    S,I = unitPropagate(S,I)
    if len(S)==0:
        return "Satisfacible" ,I
    #8: Si no retorna satisfacible
    else:
    #9: Definimos S'' (S2P) como S sin las clausulas que contienen a -l y eliminando l de las restantes
        S2P = SP[:]
        count = 0
        for claus in S:
            S2P[count] = claus
            for i in range(len(claus)):
                if claus[i] not in I.keys():
                    if claus[i] != '-':
                        l = claus[i]
                        break
            break
        for claus in S:
            S2P[count] = claus
            for i in range(len(claus)):
                if len(l)==1:
                    if claus[i] == l:

                        leng = len(claus)
                        S2P[count] = S2P[count].replace(S2P[count][i],'')
                        if len(S2P[count])<leng:
                            break
                    elif (claus[i] == '-' and claus[i+1] == l):
                        S2P.remove(S2P[count])
                        count-=1
                        break

    #10: Aumentamos I con las interpretaciones que cumplan que V(-l)=1
            count+=1
        S = S2P[:]
        if len(l)==1:
            I[l]=0
        elif len(l)==2:
    #11: Retornamos DPLL de (S'',I'')
            I[l]=1
        return DPLL(S2P,I)

#Prueba de la función
#print(DPLL(["p-qr","-pq-r","-p-qr","-p-q-r"],{}))
