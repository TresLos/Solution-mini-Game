# gracies a la colaboracio de la gran idea d'en Martin, segurament podre guanyar un repte que m'he possat
# Es una proposta per a millorar les prestacions del yield
# Versio 0.1.0 jajajajajja - la 0.0.0 era el yield -

#angita, gracies
#raise suelta un error, como una exception except
#assert algo = noseque algo is loquesea

import Queue

def Begin (n):
# estaria be fer comprovacio de possiblitat
	a = Brutus(n)
	print len (a)
	return a

# in  \approx True
# out \approx False
def Brutus (nameFile):
	All = {}
	qIn, qOut, qtmp = Queue.Queue (), Queue.Queue (), Queue.Queue ()
	vIn, vOut = Llegeix (nameFile)
	All[Union (vIn)] = True
	All[Union(vOut)] = False
	qIn.put ((vIn, []))
	qOut.put((vOut,[]))
# Tot inicialitzat, tinc previst que aquest sigui un segon metode
# on al inicial fer una comprovacio del que es vol fer es possible


# vIn, matriu de proves
# mov, tots els moviments fins a llavors
# tM,  temporal matriu del canvi fet per i
# tN,  temporal next matriu, nomes se fa anar un cop ja se sap que se te la solucio
	while 1:
		while not qIn.empty ():
			vIn, mov = qIn.get ()
			for i in Generator (vIn): # Per cada fill:
				tM = Canvi (vIn, i)
				if All.has_key( Union(tM)): # Comprovar si ja existeix
					if not All[ Union(tM)]:# ja em acabat
						while not qOut.empty ():
							tN = qOut.get ()
							if tN[0] == tM: return mov + [i] + tN[1]
						print 'Ha petat tot'# Si ha arribat aqui, la cosa va molt malament
						return "Puta merda"
				else:
					All[Union (tM)] = True
					qtmp.put ((tM, mov + [i]))
# Ara el qIn esta buit
		qIn, qtmp = qtmp, qIn

# Si tingues l'apartat 2, serie exactament el doble de rapid

################################################################################################################################
##                                                          AJUDA                                                             ##
################################################################################################################################
# copy past del yield
def Llegeix (File):
	a = [line[:-1].split (' ') for line in open (File)]
	return a[:len (a) /2], a[len (a) /2 +1:]

# copy past del yield
def Canvi (mo, i):
	q, w, e = i
	if e == 'R':
		m = mo[:] # Aqui no cal copiar tot
		m[q] = m[q][-w:] + m[q][:-w]
		return m
	m = [row[:] for row in mo]
	z = [i[q] for i in m]
	z = z[-w:] + z[:-w]
	for i in xrange(len(m)):
		m[i][q] = z[i]
	return m
def Generator (t):
	m, n = len(t), len(t[0])
	for i in xrange(m):
		for j in xrange(1, n):
			yield (i, j, "R")
	for i in xrange(n):
		for j in xrange(1, m):
			yield (i, j, "D")
def Union (a): return reduce (lambda x, y: x+y, reduce(lambda x, y: x+y, a))
################################################################################################################################
##                                                        Experiments                                                         ##
################################################################################################################################
# Putada, no accepta llistes, llavors he de plantejar un altre sistema xD
