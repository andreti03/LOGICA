import Generador_Reglas as G
import Algoritmos as A
import Codificacion as C
import FNC as F
import DPLL as D
import Gran_grafico as GF
import sys

letrasProposicionales = [chr(i) for i in range(256, 400)]

# Solicita condicion inicial
#W={"ď":1,"ĉ":1,"Ā":1,"Ə":1,"Ɖ":1,"ƀ":1} #//CONDICIONES INICIAL Y FINAL
W={}
print("Creando reglas...")
reglas = G.REGLA()                                                                                  #////  GOOD ////
#reglas = G.REGLA1()+G.REGLA2()+G.REGLA3()+G.REGLA5()+G.con_ini()+G.con_fin()+"YYYYY"               #////EXPLOTA////
#reglas = G.con_ini()+G.con_fin()+"Y"                                                               #////  GOOD ////
#reglas = G.con_ini()+G.con_fin()+G.REGLA1()+"YY"                                                   #////  GOOD ////
#reglas = G.con_ini()+G.con_fin()+G.REGLA1()+G.REGLA2()+"YYY"                                       #////  GOOD ////
#reglas = G.con_ini()+G.REGLA1()+G.REGLA2()+G.REGLA3()+G.con_fin()+"YYYY"                           #////EXPLOTA////
#reglas = G.con_ini()+G.con_fin()+G.REGLA1()+G.REGLA2()+G.REGLA5()+"YYYY"                           #////  GOOD ////
#reglas = G.con_ini()+G.con_fin()+G.REGLA1()+G.REGLA2()+G.REGLA4()+"YYYY"                           #////  GOOD ////
#reglas = G.REGLA1()+G.REGLA2()+G.REGLA3()+G.REGLA4()+G.con_ini()+G.con_fin()+G.REGLA5()+"YYYYYY"   #////  GOOD ////
#reglas = G.REGLA6()+G.REGLA1()+"Y"                                                                                  #////  GOOD ////

T = A.String2Tree(reglas)
#print(T)
IT = A.Inorder(T)
#TR= C.traduccion(IT)
#print(TR)
#print(IT)
TS = F.Tseitin(IT,letrasProposicionales)
#print(TS)
CL= F.formaClausal(TS)
#print(CL)
l=D.conjunto_de_formulas(TS)
print(len(CL))
#print(l)
print("#"*60)
Respuesta=D.DPLL(CL,W)
#print(Respuesta)
ID = Respuesta[1]
I = C.Decodificar(ID)
#I = C.Decodificar_CEROS(ID)
print("="*30 + "RESPUESTA"+"="*30)
print(I)

print('Visualizaciones guardadas')
print('Terminado!')

res= GF.CodGraf(I)

GF.fin(res)