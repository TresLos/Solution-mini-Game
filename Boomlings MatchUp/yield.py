def Begin (nameFile):
# mi i mo = matrix int and out
	mi, mo = Lectura (nameFile)
	s1, s2 = len(mi), len(mi[0])
	generador = SimpleGenerator(s1, s2)
	n = generador.next()
	arr = []
# Tot inizialitzat

# Comencem a generar fills
#for i in xrange(n):
	for i in generador:
		arr.append (  RecorNext ( Canvi (mi, i), i, mo, s1, s2 )  )

# El important del programa, el nucli, l'arrel
	while 1:
		for i in arr:
			tmp = i.next()
			if tmp: return tmp
	return "Sorry"

# L'altre
def RecorNext (mi, cami, mo, s1, s2):
	if mi == mo:
		yield [cami]
	generador = Generador(s1, s2, cami)
	n = generador.next()
	arr = []
# Tuti inizialitzated

# Generem fills
	for i in generador:
		arr.append (  RecorNext (Canvi (mi, i), i, mo, s1, s2 )  )

# Lo importan, l'arrel, kernel, root
	while 1:
# El yield abans de generar fills m'asegura de
# no baixar nivells sense control
		yield False
		for i in arr:
			tmp = i.next()
			if tmp: yield [cami] + tmp


# Aparentment funciona exactament com jo voldira :)
def Lectura (File):
	a = [line[:-1].split(' ') for line in open(File)]
	return a[:len(a)/2], a[len(a)/2 +1:]

# Generador	m files		n columnes
# Return	/Position	/Mov	/Direction
def SimpleGenerator (m, n):
	yield (2*m -1)*n -m
	for i in xrange(m):
		for j in xrange(1, n):
			yield (i, j, "R")
	for i in xrange(n):
		for j in xrange(1, m):
			yield (i, j, "D")
def Generador (m, n, cami):
	if cami[2] == 'R':
#		yield 2*m*n -m -n - (n -1)
		yield (m -1)*2*n -m +1
		for i in xrange(cami[0]):
			for j in xrange(1, n):
				yield (i, j, 'R')
		for i in xrange(cami[0] +1, m):
			for j in xrange(1, n):
				yield (i, j, 'R')
		for i in xrange(n):
			for j in xrange(1, m):
				yield (i, j, 'D')
	else:
#		yield 2*m*n -m -n - (m -1)
		yield (n -1)*2*m -n +1
		for i in xrange(m):
			for j in xrange(1, n):
				yield (i, j, 'R')
		for i in xrange(cami[0]):
			for j in xrange(1, m):
				yield (i, j, 'D')
		for i in xrange(cami[0] +1, n):
			for j in xrange(1, m):
				yield (i, j, 'D')

# Em sembla que esta molt corregit i es forza correcte
# serveix per fer canvis de matrius, sense canviar l'original
#	/Position	/Mov	/Direction
def Canvi (mo, i):
#	print i Si mai vols coneixer la grandaria d'aquest, deixa que imprimeixi :)
	q, w, e = i
	if e == 'R':
		m = mo[:] # Aqui no cal copiar tot
		m[q] = m[q][-w:] + m[q][:-w]
		return m
# Down
	m = [row[:] for row in mo]
	z = [i[q] for i in m]
	z = z[-w:] + z[:-w]
	for i in xrange(len(m)):
		m[i][q] = z[i]
	return m

################################################################################################################################
##                                                          PROVES                                                            ##
################################################################################################################################
# [[i]*10 for i in range(10)]


# Gracies a tot aquest codi, descobrim la formuleta magica	/ (2m -1)n -m	/ Deduida fent un parell de cassos, no demostrat per ara
def Count(m, n):
	i = -1
	for a in SimpleGenerator(m, n): i+=1
	return i
def Count2(m, n):
	a = SimpleGenerator(m, n)
	t = a.next()
	i = 0
	for q in a: i+=1
	return (t, i)

def Testeix(m, n):
	a = [0]*m
	for i in xrange(m): a[i] = [0]*n
	for i in xrange(m):
		for j in xrange(n):
			a[i][j] = Count(i, j) - ( (2*i -1)*j -i )
	return a
def Testeix2(m, n):
	a = [0]*m
	for i in xrange(m): a[i] = [0]*n
	for i in xrange(m):
		for j in xrange(n):
			a[i][j] = Count(i, j)
	return a
# Mirem si consideix el nombre de Generador amb el resultat real
def lookGenerator(m, n, cami):
	lola = Generador (m, n, cami)
	t = lola.next()
	i = 0
	for a in lola: i+=1
	return t, i
