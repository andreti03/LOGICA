letrasProposicionales = [chr(i) for i in range(256, 1000)]
conectivos = ['Y', 'O', '>',"@"]
#letrasProposicionales = [chr(i) for i in range(97, 106)]


class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula

	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def String2Tree(A):
	# Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
	# Input: - A, lista de caracteres con una formula escrita en notacion polaca inversa
	#        - letrasProposicionales, lista de letras proposicionales
	#        - conectivos, lista de conectivos
	# Output: formula como tree
	pila = []
	for c in A:
		# print("Examinando " + str(c))
		if c in letrasProposicionales:
			# print(u"El símbolo es letra proposicional")
			pila.append(Tree(c, None, None))
		elif c == '-':
			# print("Negamos")
			formulaAux = Tree(c, None, pila[-1])
			del pila[-1]
			pila.append(formulaAux)
		elif c in conectivos:
			# print("Unimos mediante conectivo")
			formulaAux = Tree(c, pila[-1], pila[-2])
			del pila[-1]
			del pila[-1]
			pila.append(formulaAux)
		else:
			print(u"Hay un problema: el símbolo " + str(c) + " no se reconoce")
	return pila[-1]

