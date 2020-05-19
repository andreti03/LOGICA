letrasProposicionales = [chr(i) for i in range(256, 1000)]

archivo = open("Letras.txt", "w")

count=1
Posiciones=["Arriba","Medio","Abajo"]
Palos=["PA","PB","PC"]
Fichas=["1","2","3"]
Turnos=["1","2","3","4","5","6","7","8"]
i=0
for i in Turnos:
	for F in Fichas:
		for P in Posiciones:
			for PX in Palos:
				if F=="2" and P == "Arriba":
					break
				elif F=="3" and P == "Arriba":
					break
				elif F=="3" and P == "Medio":
					break
				W="("+PX+","+ F +","+ P +","+ i +")"
				archivo.write(W)
				archivo.write("\n")

archivo.close()

myfile = open("Letras.txt","r")
x = myfile.readlines()
myfile.close()

#print(len(letrasProposicionales))
Original={}
Inversa={}
for q in range(len(x)):
	x[q]=x[q].replace("\n","")
	Original[x[q]]=letrasProposicionales[q]
	
for q in range(len(x)):
	x[q]=x[q].replace("\n","")
	Inversa[letrasProposicionales[q]]=x[q]

#print("Original ->",Original)
#print("Inversa ->",Inversa)
#k = Original.get("(PA,3,Abajo,8)")
#print(k)

def Codificacion(s):
	s=s.replace(" ","")
	for q in s:
		p = s.find("(")
		f = s.find(")")
		rem = s[p:f+1]
		if rem=="":
			return s
		l = Original.get(rem)
		s=s.replace(rem,l)
	return s

def traduccion(s):
	for q in s:
		if q in letrasProposicionales:
			rem= Inversa.get(q)
			s=s.replace(q,rem)
	return s


def Decodificar(Dicc):
	#Retorna un string de las interpretaciones verdaderas 
	Sera=[]
	items = Dicc.items()
	res=[]
	for x in items:
		if x[1]==1:
			Sera.append(x[0])

	Sera2=[]
	for q in Sera:
		if q in letrasProposicionales:
			Sera2.append(q)
		else:
			pass
	
	for k in Sera2:
		res.append(k)
	
	for h in range(len(res)):
		res[h]=traduccion(res[h])

	print(len(res))
	return res
		

def Decodificar_CEROS(Dicc):
	#Retorna un string de las interpretaciones verdaderas 
	Sera=[]
	items = Dicc.items()
	res=[]
	for x in items:
		if x[1]==0:
			Sera.append(x[0])

	Sera2=[]
	for q in Sera:
		if q in letrasProposicionales:
			Sera2.append(q)
		else:
			pass

	for k in Sera2:
		res.append(k)

	print(len(res))
	return res