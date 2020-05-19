import Codificacion as C
import Algoritmos as A

def REGLA1():
	archivo = open("primero.txt", "w")

	count=1
	
	Posiciones=["Arriba","Medio","Abajo"]
	Palos=["PA","PB","PC"]
	Fichas=["F1","F2","F3"]
	Turnos=["1","2","3","4","5","6","7","8"]
	"""
	Posiciones=["Arriba","Medio"]
	Palos=["PA","PB"]
	Fichas=["F1","F2"]
	Turnos=["1"]
	"""
	i=0
	while i<8:
		for F in Fichas:
			for P in Posiciones:
				for PX in Palos:
					if F=="F2" and P == "Arriba":
						break
					elif F=="F3" and P == "Arriba":
						break
					elif F=="F3" and P == "Medio":
						break
					W="-( "+PX+", "+ F +", "+ P +", T"+ Turnos[i] +")"+"@"
					archivo.write(W)
					archivo.write("\n")
		i+=1

	archivo.close()

	myfile = open("primero.txt","r")
	x = myfile.readlines()
	archivo = open("Regla_1.txt", "w")
	archivo.seek(0)


	for q in x:
		k=q.find("T")
		j=q.find("@")
		t = q[1:j] 

		h=""
		for P in Posiciones:
			for PX in Palos:
				e=q[7:9]
				if e=="F2" and P == "Arriba":
					break
				elif e=="F3" and P == "Arriba":
					break
				elif e=="F3" and P == "Medio":
					break
				elif e=="F2" and P == "Arriba":
					break
				elif e=="F2" and P == "Arriba":
					break
				elif e=="F3" and P == "Medio":
					break

				h= h+"( "+PX+", "+ e +", "+ P +", "+ q[k:k+2] +")"
		count=0
		h=h.replace(t,"")
		for c in h:
			if c=="P":
				count+=1

		W = h+ "O"*(count-1) +q.replace("\n","")
		W = W.replace("F","")
		W = W.replace("T","")
		W = W.replace(" ","")
		archivo.write(W)


	archivo.close()
	myfile.close()

	myfile = open("Regla_1.txt","r")
	fin = myfile.read()
	fin=fin.replace("\n","")
	myfile.close()
	con=-1
	for q in range(len(fin)):
		if fin[q]=="@":
			con+=1
	print("="*30+"   REGLA 1 EJECUNTANDO   "+"="*50)
	fin=fin+"Y"*con
	print("="*30+"   REGLA 1 ORIGINAL FINALIZADA   "+"="*42)
	print(fin)
	print("="*30+"   REGLA 1 CODIFICADA  FINALIZADA  "+"="*40)
	res = C.Codificacion(fin)
	print(res)
	print("="*30+"   REALIZANDO String2Tree.... (SEA PACIENTE) "+"="*30)
	TR1=A.String2Tree(res)
	print("="*30+"   String2Tree FINALIZADO!   "+"="*46)
	print("="*30+"   REALIZANDO INORDER .... (SEA PACIENTE)   "+"="*31)
	INR1=A.Inorder(TR1)
	print(INR1)
	print("="*30+"   INORDER FINALIZADO    "+"="*50)
	TR= C.traduccion(INR1)
	print(TR)
	print("="*30+"   REGLA 1 FINALIZADA    "+"="*50+"\n"*3)
	return res


def REGLA2(): #No levitación
	#Posiciones=["Arriba","Medio","Abajo"]
	Palos=["PA","PB","PC"]
	#Fichas=["1","2","3"]
	Turnos=["1","2","3","4","5","6","7","8"]


	vacio_abajo=[] #Abajo está vacío si ni F1 ni F2 ni F3 están abajo. Se itera por palo y por turno
	for T in Turnos:
		for PX in Palos:
			W="("+PX+","+"1, Abajo, "+T+" )-("+PX+","+"2, Abajo, "+T+")-("+PX+","+"3, Abajo, "+T+")-YY"
			vacio_abajo.append(W)

	vacio_medio=[]

	for T in Turnos:
		for PX in Palos:
			W="("+PX+","+"1, Medio, "+T+" )-("+PX+","+"2, Medio, "+T+")-Y"
			vacio_medio.append(W)


	vacio_arriba=[]
	for T in Turnos:
		for PX in Palos:
			W="("+PX+","+"1, Arriba, "+T+" )-"
			vacio_arriba.append(W)
	k="("+"PC"+","+"1,Arriba, "+"7"+" )-("+"PC"+","+"2, Medio, "+"7"+")->"
	#k="("+"PC"+","+"1,Arriba, "+"7"+" )-("+"PC"+","+"2, Medio, "+"7"+")>"
	it=0
	aux=[]

	while it<len(vacio_abajo): #Todas la listas tienen la misma lengitud
		v1=vacio_abajo[it]
		v2=vacio_medio[it]
		v3=vacio_arriba[it]

		W="{2}{1}Y{0}>".format(v1,v2,v3)
		aux.append(W)
		it+=1
	aux.append(k)
	#Regla2="{23}{22}{21}{20}{19}{18}{17}{16}{15}{14}{13}{12}{11}{10}{9}{8}{7}{6}{5}{4}{3}{2}{1}{0}YYYYYYYYYYYYYYYYYYYYYYY".format(aux[0],aux[1],aux[2],aux[3],aux[4],aux[5],aux[6],aux[7],aux[8],aux[9],aux[10],aux[11],aux[12],aux[13],aux[14],aux[15],aux[16],aux[17],aux[18],aux[19],aux[20],aux[21],aux[22],aux[23])
	Regla2="{24}{23}{22}{21}{20}{19}{18}{17}{16}{15}{14}{13}{12}{11}{10}{9}{8}{7}{6}{5}{4}{3}{2}{1}{0}YYYYYYYYYYYYYYYYYYYYYYYY".format(aux[0],aux[1],aux[2],aux[3],aux[4],aux[5],aux[6],aux[7],aux[8],aux[9],aux[10],aux[11],aux[12],aux[13],aux[14],aux[15],aux[16],aux[17],aux[18],aux[19],aux[20],aux[21],aux[22],aux[23],aux[24])
	



	"""	
	it=0
	Regla_2_lista=[]
	while it<len(vacio_abajo): #todos tienen la misma longitud, así que no hay ningún problema
		if it==0:
			prop=vacio_abajo[it]+"YY"+vacio_medio[it]+vacio_arriba[it]+"YY>" 
			#prop="("+x+"(p)Y"
			Regla_2_lista.append(prop)

		elif it==len(vacio_abajo)-1:
			prop=vacio_abajo[it]+"YY"+vacio_medio[it]+vacio_arriba[it]+"YY>"
			#prop="(q))"
			Regla_2_lista.append(prop)

		else:
			prop=vacio_abajo[it]+"YY"+vacio_medio[it]+vacio_arriba[it]+"YY>"
			#prop="(r))Y"
			Regla_2_lista.append(prop)
		it+=1
	#print(len(Regla_2_lista))
	"""
	archivo=open("Regla_2.txt","w")
	#Regla2="" #AQUÍ SE GUARDA TODA LA REGLA SIN CODIFICAR
	#Pasar toda la regla a un archivo txt
	#for prop in Regla_2_lista:
	#	Regla2+=prop
	#	prop = prop.replace(" ","")
	#	archivo.write(prop)
	archivo.write(Regla2)
	archivo.close()
	
	myfile = open("Regla_2.txt","r")
	fin = myfile.read()
	fin=fin.replace("\n","")
	myfile.close()
	#con=-1
	#for q in range(len(fin)):
	#	if fin[q]==">":
	#		con+=1
	print("="*30+"   REGLA 2 EJECUNTANDO   "+"="*50)
	#fin=fin+"Y"*con
	print("="*30+"   REGLA 2 ORIGINAL  FINALIZADA  "+"="*42)
	#print(fin)
	print("="*30+"   REGLA 2 CODIFICADA  FINALIZADA  "+"="*40)
	res = C.Codificacion(fin)
	#print(res)
	print("="*30+"   REALIZANDO String2Tree.... (SEA PACIENTE) "+"="*30)
	TR2=A.String2Tree(res)
	print("="*30+"   String2Tree FINALIZADO!   "+"="*46)
	print("="*30+"   REALIZANDO INORDER .... (SEA PACIENTE)   "+"="*31)
	INR2=A.Inorder(TR2)
	#print(INR2)
	print("="*30+"   INORDER FINALIZADO    "+"="*50)
	TR=C.traduccion(INR2)
	#print(TR)
	print("="*30+"   REGLA 2 FINALIZADA   "+"="*51+"\n"*3)
	return res



def REGLA3(): #No mayor sobre menor
	archivo=open("Regla_3.txt", "w")
	Posiciones=["Arriba","Medio","Abajo"]
	Palos=["PA","PB","PC"]
	Fichas=["1","2","3"]
	Turnos=["1","2","3","4","5","6","7","8"]

	lis=[]
	for T in Turnos:
		for PX in Palos:
			l1="("+PX+",1,Abajo,"+T+")"
			l2="("+PX+",2,Medio,"+T+")"

			W="{1}-{0}>".format(l1,l2)
			#W="(("+PX+",1,Abajo,"+T+")<>-("+PX+",2,Medio,"+T+"))"
			lis.append(W)
	#for p in lista_aux:
	#    print(p)
	Regla3="{23}{22}{21}{20}{19}{18}{17}{16}{15}{14}{13}{12}{11}{10}{9}{8}{7}{6}{5}{4}{3}{2}{1}{0}YYYYYYYYYYYYYYYYYYYYYYY".format(lis[0],lis[1],lis[2],lis[3],lis[4],lis[5],lis[6],lis[7],lis[8],lis[9],lis[10],lis[11],lis[12],lis[13],lis[14],lis[15],lis[16],lis[17],lis[18],lis[19],lis[20],lis[21],lis[22],lis[23])

	archivo.write(Regla3)
	archivo.close()

	myfile = open("Regla_3.txt","r")
	fin = myfile.read()
	fin=fin.replace("\n","")
	myfile.close()
	#con=-1
	#for q in range(len(fin)):
	#	if fin[q]=="@":
	#		con+=1

	print("="*30+"   REGLA 3 EJECUNTANDO   "+"="*50)
	#fin=fin+"Y"*con
	print("="*30+"   REGLA 3 ORIGINAL    "+"="*52)
	#print(fin)
	print("="*30+"   REGLA 3 CODIFICADA    "+"="*50)
	res = C.Codificacion(fin)
	#print(res)
	print("="*30+"   REALIZANDO String2Tree.... (SEA PACIENTE) "+"="*30)
	TR3=A.String2Tree(res)
	print("="*30+"   String2Tree FINALIZADO!   "+"="*46)
	print("="*30+"   REALIZANDO INORDER .... (SEA PACIENTE)   "+"="*31)
	INR3=A.Inorder(TR3)
	#print(INR3)
	print("="*30+"   INORDER FINALIZADO    "+"="*50)
	print("="*30+"   REGLA 3 FINALIZADA    "+"="*50+"\n"*3)
	return res



def REGLA4(): #Un movimiento por turno
	Posiciones=["Arriba","Medio","Abajo"]
	Palos=["PA","PB","PC"]
	Fichas=["F1","F2","F3"]
	Turnos=["1","2","3","4","5","6","7","8"]

	#M1,N
	M1N=[]
	i=0
	while i<7:
		for PX in Palos:
			for P in Posiciones:
				l1="("+PX+", 1, "+P+", "+Turnos[i]+")"
				l2="("+PX+", 1, "+P+", "+Turnos[i+1]+")"

				#W="({0}@{1})".format(l1,l2) #No movimiento: (PA,1,Arriba,1)@(PA,1,Arriba,2) para que no haya movimiento la ficha debe estar en la misma situaci�n en el turno n y en el turno n+1
				W="{1}{0}@".format(l1,l2)
				M1N.append(W)
		i+=1

	cont=0
	M1Ndef=[]
	#print(len(M1N))=63
	while cont<63:
		m0=M1N[cont]
		m1=M1N[cont+1]
		m2=M1N[cont+2]
		m3=M1N[cont+3]
		m4=M1N[cont+4]
		m5=M1N[cont+5]
		m6=M1N[cont+6]
		m7=M1N[cont+7]
		m8=M1N[cont+8]

		#Se unen todos los iff con Y, por ejemplo (((PA,1,Arriba,1)@(PA,1,Arriba,2))Y((PB,1,Arriba,1)@(PB,1,Arriba,2)))
		prop="{8}{7}{6}{5}{4}{3}{2}{1}{0}YYYYYYYY".format(m0,m1,m2,m3,m4,m5,m6,m7,m8)

		M1Ndef.append(prop)
		cont+=9
	"""
	CO= C.Codificacion(M1Ndef[6])
	T= A.String2Tree(CO)
	I= A.Inorder(T)
	TR= C.traduccion(I)
	print("M1n :",TR)
	"""
	#LISTO M1N
	#==================================================================================================================
	#M2N
	#Para este hay otras Posiciones
	Posiciones2=["Medio","Abajo"]

	M2N=[]

	i=0
	while i<7:
		for PX in Palos:
			for P in Posiciones2:
				letra1="("+PX+", 2, "+P+", "+Turnos[i]+")"
				letra2="("+PX+", 2, "+P+", "+Turnos[i+1]+")"

				W="{1}{0}@".format(letra1,letra2) #Igual que en M1N, pero con la ficha 2

				M2N.append(W)
		i+=1

	cont=0
	M2Ndef=[]
	while cont<42:
		letra1=M2N[cont]
		letra2=M2N[cont+1]
		letra3=M2N[cont+2]
		letra4=M2N[cont+3]
		letra5=M2N[cont+4]
		letra6=M2N[cont+5]

		prop="{5}{4}{3}{2}{1}{0}YYYYY".format(letra1,letra2,letra3,letra4,letra5,letra6)

		#prop="((((("+M2N[cont]+"Y"+M2N[cont+1]+")Y"+M2N[cont+2]+")Y"+M2N[cont+3]+")Y"+M2N[cont+4]+")Y"+M2N[cont+5]+")"
		#prop="("+M2N[cont]+"Y("+M2N[cont+1]+"Y("+M2N[cont+2]+"Y("+M2N[cont+3]+"Y("+M2N[cont+4]+"Y("+M2N[cont+5]+")))))"
		M2Ndef.append(prop)
		cont+=6
	"""
	CO= C.Codificacion(M2Ndef[0])
	T= A.String2Tree(CO)
	I= A.Inorder(T)
	TR= C.traduccion(I)
	print("M1n :",TR)
	"""
	#Listo M2N
	#==================================================================================================
	#M3N

	#Para este hay otras Posiciones
	Posiciones3=["Abajo"]
	M3N=[]

	i=0
	while i<7:
		for PX in Palos:
			for P in Posiciones3:
				letra1="("+PX+", 3, "+P+", "+Turnos[i]+")"
				letra2="("+PX+", 3, "+P+", "+Turnos[i+1]+")"

				W="{1}{0}@".format(letra1,letra2) #Igual que en M1N pero con la ficha 3
				M3N.append(W)
		i+=1

	cont=0
	M3Ndef=[]
	#print(len(M3N))=21
	while cont<21:
		l1=M3N[cont]
		l2=M3N[cont+1]
		l3=M3N[cont+2]

		prop="{2}{1}{0}YY".format(l1,l2,l3)

		M3Ndef.append(prop)
		cont+=3

	#Listo M3N
	#==============================================================================================

	#UNIR LAS REGLAS

	regla=[]
	r=0
	archivo=open("Regla_4.txt","w")
	while r<7: #Todas las listas tienen esta longitud
		m1=M1Ndef[r]
		m2=M2Ndef[r]
		m3=M3Ndef[r]

		#Si hay movimiento de la ficha 1 en el turno n, entonces no se mueven ni la ficha 2 ni la ficha 3
		#Y
		#Si hay movimiento de la ficha 2 en el turno n, entonces no se mueven ni la ficha 1 ni la ficha 3
		#Y
		#Si hay movimiento de la ficha 3 en el turno n, entonces no se mueven ni la ficha 1 ni la ficha 2

		prop="{8}{7}Y{6}->{5}{4}Y{3}->{2}{1}Y{0}->YY".format(m1,m2,m3,m2,m1,m3,m3,m1,m2)

		regla.append(prop)
		r+=1
	"""
	CO= C.Codificacion(regla[0])
	T= A.String2Tree(CO)
	I= A.Inorder(T)
	TR= C.traduccion(I)
	print("R1 :",TR)
	"""
	#Se unen todos los movimientos por turno creados anteriormente con una Y
	Regla4="{6}{5}{4}{3}{2}{1}{0}YYYYYY".format(regla[0],regla[1],regla[2],regla[3],regla[4],regla[5],regla[6])

	archivo.write(Regla4)

	archivo.close()
	myfile = open("Regla_4.txt","r")
	fin = myfile.read()
	fin=fin.replace("\n","")
	myfile.close()

	print("="*30+"   REGLA 4 EJECUNTANDO   "+"="*50)
	print("="*30+"   REGLA 4 ORIGINAL FINALIZADA   "+"="*42)
	#print(fin)
	print("="*30+"   REGLA 4 CODIFICADA  FINALIZADA  "+"="*40)
	res = C.Codificacion(fin)
	#print(res)
	print("="*30+"   REALIZANDO String2Tree.... (SEA PACIENTE) "+"="*30)
	TR4=A.String2Tree(res)
	print("="*30+"   String2Tree FINALIZADO!   "+"="*46)
	print("="*30+"   REALIZANDO INORDER .... (SEA PACIENTE)   "+"="*31)
	INR4=A.Inorder(TR4)
	#print(INR4)
	print("="*30+"   INORDER FINALIZADO    "+"="*50)
	print("="*30+"   REGLA 4 FINALIZADA    "+"="*50+"\n"*3)
	return res
	

   #=======================================regla 5================================================
def REGLA5(): #Solo se mueve el de arriba de la torre
	Posiciones=["Arriba","Medio","Abajo"]
	Palos=["PA","PB","PC"]
	Fichas=["F1","F2","F3"]
	Turnos=["1","2","3","4","5","6","7","8"]

	#M1,N no se necesita en esta regla


	#==================================================================================================================
	#M2N

	#M2N

	#Para este hay otras Posiciones
	Posiciones2=["Medio","Abajo"]

	M2N=[]

	i=0
	while i<7:
		for PX in Palos:
			for P in Posiciones2:
				W="("+PX+", 2, "+P+", "+Turnos[i+1]+")("+PX+", 2, "+P+", "+Turnos[i]+")@"
				M2N.append(W)
		i+=1

	cont=0
	prop=""
	M2Ndef=[]
	while cont<42:
		prop=M2N[cont]+M2N[cont+1]+M2N[cont+2]+M2N[cont+3]+M2N[cont+4]+M2N[cont+5]+"YYYYY"
		M2Ndef.append(prop)
		prop=""
		cont+=6


	#Listo M2N
	#==================================================================================================
	#M3N

	#Para este hay otras Posiciones
	Posiciones3=["Abajo"]
	M3N=[]

	i=0
	while i<7:
		for PX in Palos:
			for P in Posiciones3:
				W="("+PX+", 3, "+P+", "+Turnos[i+1]+")("+PX+", 3, "+P+", "+Turnos[i]+")@"#OJO
				M3N.append(W)
		i+=1

	cont=0
	prop=""
	M3Ndef=[]
	#print(len(M3N))=21
	while cont<21:
		prop=M3N[cont]+M3N[cont+1]+M3N[cont+2]+"YY"
		M3Ndef.append(prop)
		prop=""
		cont+=3
	


	#==============================================================================================

	#UNIR LAS REGLAS
	Nturnos=["1","2","3","4","5","6","7"]

	regla=[]
	i=0

	while i<7:
		for T in Nturnos:
			for PX in Palos:
				f1a="("+PX+", 1, Arriba, "+T+")"
				f1m="("+PX+", 1, Medio, "+T+")"
				f2b="("+PX+", 2, Abajo, "+T+")"
				f2m="("+PX+", 2, Medio,"+T+")"
				f3b="("+PX+", 3, Abajo, "+T+")"
				m2=M2Ndef[i]
				m3=M3Ndef[i]

				pp="{7}{6}Y{5}{4}{3}YY>{2}{1}{0}Y>Y".format(f2b,f1m,m2,f3b,f2m,f1a,m2,m3)
				#pp=M2Ndef[i]+"("+PX+", 1, Medio, "+T+")("+PX+", 2, Abajo, "+T+")Y>"
				#pp+=M3Ndef[i]+M2Ndef[i]+"YYY"+"("+PX+", 1, Arriba, "+T+")("+PX+", 2, Medio,"+T+")("+PX+", 3, Abajo, "+T+")YY>"
				regla.append(pp)
			i+=1

	Regla5="{20}{19}{18}{17}{16}{15}{14}{13}{12}{11}{10}{9}{8}{7}{6}{5}{4}{3}{2}{1}{0}YYYYYYYYYYYYYYYYYYYY".format(regla[0],regla[1],regla[2],regla[3],regla[4],regla[5],regla[6],regla[7],regla[8],regla[9],regla[10],regla[11],regla[12],regla[13],regla[14],regla[15],regla[16],regla[17],regla[18],regla[19],regla[20])

	archivo=open("Regla_5.txt","w")

	archivo.write(Regla5)

	archivo.close()

	myfile = open("Regla_5.txt","r")
	fin = myfile.read()
	fin=fin.replace("\n","")
	myfile.close()

	print("="*30+"   REGLA 5 EJECUNTANDO   "+"="*50)
	print("="*30+"   REGLA 5 ORIGINAL FINALIZADA   "+"="*42)
	#print(fin)
	print("="*30+"   REGLA 5 CODIFICADA  FINALIZADA   "+"="*39)
	res = C.Codificacion(fin)
	#print(res)
	print("="*30+"   REALIZANDO String2Tree.... (SEA PACIENTE) "+"="*30)
	TR5=A.String2Tree(res)
	print("="*30+"   String2Tree FINALIZADO!   "+"="*46)
	print("="*30+"   REALIZANDO INORDER .... (SEA PACIENTE)   "+"="*31)
	INR5=A.Inorder(TR5)
	#print(INR5)
	print("="*30+"   INORDER FINALIZADO    "+"="*50)
	print("="*30+"   REGLA 5 FINALIZADA    "+"="*50+"\n"*3)
	return res

def REGLA6(): #No mayor sobre menor
	archivo=open("Regla_6.txt", "w")
	Posiciones=["Arriba","Medio","Abajo"]
	Palos=["PA","PB","PC"]
	Fichas=["1","2","3"]
	Turnos=["1","2","3","4","5","6","7","8"]

	lis=[]
	for T in Turnos:
		for PX in Palos:
			for F in Fichas:
				for P in Posiciones:#W="("+PX+",1,medio,"+T+")<>-("+PX+",2,Medio,"+T+")"
					if P =="Arriba":
						pass
					elif P =="Medio" and F=="3": 
						pass
					elif F == "1" and P == "Medio":
						l1="("+PX+","+F+",Medio,"+T+")"
						l2="("+PX+","+"2,Medio,"+T+")"
						W="{1}-{0}>".format(l1,l2)
						lis.append(W)
					elif F == "2" and P == "Medio":
						l1="("+PX+","+F+",Medio,"+T+")"
						l2="("+PX+","+"1,Medio,"+T+")"
						W="{1}-{0}>".format(l1,l2)
						lis.append(W)
					elif F == "1" and P == "Abajo":
						l1="("+PX+","+F+",Abajo,"+T+")"
						l2="("+PX+","+"2,Abajo,"+T+")"
						l3="("+PX+","+"3,Abajo,"+T+")"
						W="{2}{1}O-{0}>".format(l1,l2,l3)
						lis.append(W)
					elif F == "2" and P == "Abajo":
						l1="("+PX+","+F+",Abajo,"+T+")"
						l2="("+PX+","+"1,Abajo,"+T+")"
						l3="("+PX+","+"3,Abajo,"+T+")"
						W="{2}{1}O-{0}>".format(l1,l2,l3)
						lis.append(W)
					elif F == "3" and P == "Abajo":
						l1="("+PX+","+F+",Abajo,"+T+")"
						l2="("+PX+","+"1,Abajo,"+T+")"
						l3="("+PX+","+"2,Abajo,"+T+")"
						W="{2}{1}O-{0}>".format(l1,l2,l3)
						lis.append(W)
	regla=""
	for q in lis:
		regla=regla+q
	regla=regla+"Y"*(len(lis)-1)
	archivo.write(regla)
	archivo.close()
	
	myfile = open("Regla_6.txt","r")
	fin = myfile.read()
	fin=fin.replace("\n","")
	myfile.close()


	print("="*30+"   REGLA 6 EJECUNTANDO   "+"="*50)
	#fin=fin+"Y"*con
	print("="*30+"   REGLA 6 ORIGINAL    "+"="*52)
	#print(fin)
	print("="*30+"   REGLA 6 CODIFICADA    "+"="*50)
	res = C.Codificacion(fin)
	#print(res)
	print("="*30+"   REALIZANDO String2Tree.... (SEA PACIENTE) "+"="*30)
	TR6=A.String2Tree(res)
	print("="*30+"   String2Tree FINALIZADO!   "+"="*46)
	print("="*30+"   REALIZANDO INORDER .... (SEA PACIENTE)   "+"="*31)
	INR6=A.Inorder(TR6)
	#print(INR6)
	print("="*30+"   INORDER FINALIZADO    "+"="*50)
	TR = C.traduccion(INR6)	
	#print(TR)
	print("="*30+"   REGLA 6 FINALIZADA    "+"="*50+"\n"*3)
	return res
"""
#REGLA 7 NO ES NECESARIA
def REGLA7(): #En cada turno se debe mover al menos una ficha
	Posiciones=["Arriba","Medio","Abajo"]
	Palos=["PA","PB","PC"]
	Fichas=["F1","F2","F3"]
	Turnos=["1","2","3","4","5","6","7","8"]

	#M1,N
	M1N=[]
	i=0
	while i<7:
		for PX in Palos:
			for P in Posiciones:
				l1="("+PX+", 1, "+P+", "+Turnos[i]+")"
				l2="("+PX+", 1, "+P+", "+Turnos[i+1]+")"

				#No movimiento: (PA,1,Arriba,1)@(PA,1,Arriba,2) para que no haya movimiento la ficha debe estar en la misma situaci�n en el turno n y en el turno n+1
				W="{1}{0}@".format(l1,l2)
				M1N.append(W)
		i+=1

	cont=0
	M1Ndef=[]
	#print(len(M1N))=63
	while cont<63:
		m0=M1N[cont]
		m1=M1N[cont+1]
		m2=M1N[cont+2]
		m3=M1N[cont+3]
		m4=M1N[cont+4]
		m5=M1N[cont+5]
		m6=M1N[cont+6]
		m7=M1N[cont+7]
		m8=M1N[cont+8]

		#Se unen todos los iff con Y, por ejemplo (((PA,1,Arriba,1)@(PA,1,Arriba,2))Y((PB,1,Arriba,1)@(PB,1,Arriba,2)))
		prop="{8}{7}{6}{5}{4}{3}{2}{1}{0}YYYYYYYY".format(m0,m1,m2,m3,m4,m5,m6,m7,m8)

		M1Ndef.append(prop)
		cont+=9 #Se unen de a palo (3 posibilidades) y de a posición (3 posibilidades). En total 9 iff

	#LISTO M1N
	#==================================================================================================================
	#M2N
	#Para este hay otras Posiciones
	Posiciones2=["Medio","Abajo"]

	M2N=[]

	i=0
	while i<7:
		for PX in Palos:
			for P in Posiciones2:
				letra1="("+PX+", 2, "+P+", "+Turnos[i]+")"
				letra2="("+PX+", 2, "+P+", "+Turnos[i+1]+")"

				W="{1}{0}@".format(letra1,letra2) #Igual que en M1N, pero con la ficha 2 y sus respectivas posiciones posibles

				M2N.append(W)
		i+=1

	cont=0
	M2Ndef=[]
	while cont<42:
		letra1=M2N[cont]
		letra2=M2N[cont+1]
		letra3=M2N[cont+2]
		letra4=M2N[cont+3]
		letra5=M2N[cont+4]
		letra6=M2N[cont+5]

		prop="{5}{4}{3}{2}{1}{0}YYYYY".format(letra1,letra2,letra3,letra4,letra5,letra6)

		#prop="((((("+M2N[cont]+"Y"+M2N[cont+1]+")Y"+M2N[cont+2]+")Y"+M2N[cont+3]+")Y"+M2N[cont+4]+")Y"+M2N[cont+5]+")"
		#prop="("+M2N[cont]+"Y("+M2N[cont+1]+"Y("+M2N[cont+2]+"Y("+M2N[cont+3]+"Y("+M2N[cont+4]+"Y("+M2N[cont+5]+")))))"
		M2Ndef.append(prop)
		cont+=6 #Se unen de a palo (3 posib.) y de a posición (2 posibil.). En totales 6 iff 


	#Listo M2N
	#==================================================================================================
	#M3N

	#Para este hay otras Posiciones
	Posiciones3=["Abajo"]
	M3N=[]

	i=0
	while i<7:
		for PX in Palos:
			for P in Posiciones3:
				letra1="("+PX+", 3, "+P+", "+Turnos[i]+")"
				letra2="("+PX+", 3, "+P+", "+Turnos[i+1]+")"

				W="{1}{0}@".format(letra1,letra2) #Igual que en M1N pero con la ficha 3
				M3N.append(W)
		i+=1

	cont=0
	M3Ndef=[]
	#print(len(M3N))=21
	while cont<21:
		l1=M3N[cont]
		l2=M3N[cont+1]
		l3=M3N[cont+2]

		prop="{2}{1}{0}YY".format(l1,l2,l3)

		M3Ndef.append(prop)
		cont+=3 #Se unen de a palo (3 posib.) y de a posición (1 posibil.). En totales 3 iff 

	#Listo M3N
	#==============================================================================================

	#UNIR LAS REGLAS

	regla=[]
	r=0
	archivo=open("Regla_7.txt","w")
	while r<7: #Todas las listas tienen esta longitud
		m1=M1Ndef[r]
		m2=M2Ndef[r]
		m3=M3Ndef[r]

		#Si hay movimiento de la ficha 1 en el turno n, entonces no se mueven ni la ficha 2 ni la ficha 3
		#Y
		#Si hay movimiento de la ficha 2 en el turno n, entonces no se mueven ni la ficha 1 ni la ficha 3
		#Y
		#Si hay movimiento de la ficha 3 en el turno n, entonces no se mueven ni la ficha 1 ni la ficha 2
		prop="{2}-{1}-{0}-OO".format(m1,m2,m3)

		regla.append(prop)
		r+=1

	#Se unen todos los movimientos por turno creados anteriormente con una Y
	Regla4="{6}{5}{4}{3}{2}{1}{0}YYYYYY".format(regla[0],regla[1],regla[2],regla[3],regla[4],regla[5],regla[6])

	archivo.write(Regla4)

	archivo.close()
	myfile = open("Regla_7.txt","r")
	fin = myfile.read()
	fin=fin.replace("\n","")
	myfile.close()

	print("="*30+"   REGLA 7 EJECUNTANDO   "+"="*50)
	print("="*30+"   REGLA 7 ORIGINAL FINALIZADA   "+"="*42)
	print(fin)
	print("="*30+"   REGLA 7 CODIFICADA  FINALIZADA  "+"="*40)
	res = C.Codificacion(fin)
	#print(res)
	print("="*30+"   REALIZANDO String2Tree.... (SEA PACIENTE) "+"="*30)
	TR4=A.String2Tree(res)
	print("="*30+"   String2Tree FINALIZADO!   "+"="*46)
	print("="*30+"   REALIZANDO INORDER .... (SEA PACIENTE)   "+"="*31)
	INR4=A.Inorder(TR4)
	#print(INR4)
	print("="*30+"   INORDER FINALIZADO    "+"="*50)
	print("="*30+"   REGLA 7 FINALIZADA    "+"="*50+"\n"*3)
	return res
"""


def con_ini():
	print("="*30+"   CONDICION INICIAL EJECUTANDO    "+"="*29+"===========")
	ini="(PA,1,Arriba,1)"+"(PA,2,Medio,1)"+"(PA,3,Abajo,1)"+"YY"
	#ini="(PA,1,Arriba,1)"+"(PA,2,Medio,1)"+"Y"

	res= C.Codificacion(ini)
	print("="*30+"   REALIZANDO String2Tree.... (SEA PACIENTE) "+"="*30)
	TRI=A.String2Tree(res)
	print("="*30+"   String2Tree FINALIZADO!   "+"="*46)
	print("="*30+"   REALIZANDO INORDER .... (SEA PACIENTE)   "+"="*31)
	INRI=A.Inorder(TRI)
	#print(INRI)
	print("="*30+"   INORDER FINALIZADO    "+"="*50)
	print("="*30+"   CONDICION INICIAL FINALIZADA    "+"="*29+"==========="+"\n"*3)
	return res

def con_fin():
	print("="*30+"   CONDICION FINAL EJECUTANDO    "+"="*29+"=============")
	fin="(PC,1,Arriba,8)"+"(PC,2,Medio,8)"+"(PC,3,Abajo,8)"+"YY"
	res= C.Codificacion(fin)
	print("="*30+"   REALIZANDO String2Tree.... (SEA PACIENTE) "+"="*30)
	TRF=A.String2Tree(res)
	print("="*30+"   String2Tree FINALIZADO!   "+"="*46)
	print("="*30+"   REALIZANDO INORDER .... (SEA PACIENTE)   "+"="*31)
	INF=A.Inorder(TRF)
	#print(INF)
	print("="*30+"   INORDER FINALIZADO    "+"="*50)
	print("="*30+"   CONDICION FINAL FINALIZADA    "+"="*31+"==========="+"\n"*3)
	return res
"""
#REGLA FINAL CON REGLA7
def REGLA():
	R1 = REGLA1()
	R2 = REGLA2()
	R3 = REGLA3()
	R4 = REGLA4()
	R5 = REGLA5()
	R6 = REGLA6()
	R7 = REGLA7()
	IN = con_ini()
	FIN= con_fin()
	R= IN+R1+R2+R3+R4+R5+R6+R7+FIN+"YYYYYYYY"
	print("="*30+"   REGLA FINAL EJECUNTANDO   "+"="*46)
	print("="*30+"   REALIZANDO String2Tree.... (SEA PACIENTE) "+"="*30)
	TRF=A.String2Tree(R)
	print("="*30+"   String2Tree FINALIZADO!   "+"="*46)
	print("="*30+"   REALIZANDO INORDER .... (SEA PACIENTE)   "+"="*31)
	INRF=A.Inorder(TRF)
	#print(INRF)
	print("="*30+"   INORDER FINALIZADO    "+"="*50)
	print("="*30+"   REGLA FINAL SE HA CREADO     "+"="*43+"\n"*3)
	return R
"""

def REGLA():
	R1 = REGLA1()
	R2 = REGLA2()
	R3 = REGLA3()
	R4 = REGLA4()
	R5 = REGLA5()
	R6 = REGLA6()
	IN = con_ini()
	FIN= con_fin()
	R= IN+R1+R2+R3+R4+R5+R6+FIN+"YYYYYYY"
	print("="*30+"   REGLA FINAL EJECUNTANDO   "+"="*46)
	print("="*30+"   REALIZANDO String2Tree.... (SEA PACIENTE) "+"="*30)
	TRF=A.String2Tree(R)
	print("="*30+"   String2Tree FINALIZADO!   "+"="*46)
	print("="*30+"   REALIZANDO INORDER .... (SEA PACIENTE)   "+"="*31)
	INRF=A.Inorder(TRF)
	#print(INRF)
	print("="*30+"   INORDER FINALIZADO    "+"="*50)
	print("="*30+"   REGLA FINAL SE HA CREADO     "+"="*43+"\n"*3)
	return R
#=====Revision=====
#REGLA1()
#x= C.traduccion("(Ă>-(((((((ĈOć)OĆ)Oą)OĄ)Oă)Oā)OĀ)))")
#print(x)
#REGLA2()
#REGLA3()
#REGLA4()
#REGLA5()
#REGLA6()
#REGLA7()
#REGLA()
#con_ini()
#con_fin()
#x=String2Tree("ihgfedcbOOOOOOO-a>")
#x=A.String2Tree("f-e-d-YYc-b-a-YY>")
#x=A.String2Tree("fedOO-cbaOO->")
#x=A.String2Tree("b-a@")
#x=A.String2Tree("ģđ@ĢĐ@ġď@ĠĎ@ĝċ@ğč@ĜĊ@ĞČ@ěĉ@YYYYYYYYĀĉďYY>ĠĎ@ĝċ@ğč@ĜĊ@ĞČ@ěĉ@YYYYYăČY>Y")
#y=A.Inorder(x)
#print(y)
"""
ČYă>ĉ@ěYČ@ĞYĊ@ĜYč@ğYċ@ĝYĎ@ĠYďYĉYĀ>ĉ@ěYČ@ĞYĊ@ĜYč@ğYċ@ĝYĎ@ĠYď@ġYĐ@ĢYđ@ģ

ČYă>ĉ@ěYČ@ĞYĊ@ĜYč@ğYċ@ĝYĎ@Ġ


ďYĉYĀ>ĉ@ěYČ@ĞYĊ@ĜYč@ğYċ@ĝYĎ@ĠYď@ġYĐ@ĢYđ@ģ

ģđ@ĢĐ@ġď@ĠĎ@ĝċ@ğč@ĜĊ@ĞČ@ěĉ@YYYYYYYYĀĉďYY>ĠĎ@ĝċ@ğč@ĜĊ@ĞČ@ěĉ@YYYYYăČY>Y


-(PC,1, Abajo, 8 )Y-(PC,2, Abajo, 8)Y-(PC,3, Abajo, 8)>-(PC,1, Medio, 8 )Y-(PC,2, Medio, 8)Y-(PC,1, Arriba, 8 )
"""