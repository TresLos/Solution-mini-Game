# Aquesta vol tenir lo de l'anterior, i tambe vol aconseguir ser mes facil `de funcionament'
def Begin (n):
# estaria be fer comprovacio de possiblitat
	a = MeitatBrutus (n)
	n = a.index('T')
	print len(a)-1
	for i in a[:n] + Invert (a[n+1:]): print i
def MeitatBrutus (nameFile):
	All, atmp = {}, []
	aIn, aOut = Llegeix (nameFile)
	All[Uneix (aIn[0][0])] = True
	All[Uneix (aOut[0][0])]= False
	m, n = len(aIn[0][0]), len(aIn[0][0][0])
# Tot inizialitzat

# v, variable de gran importancia // matriu
# vf, fix, fix i fix, no canviar, nomes pot esser canviat despres del while
# mov, tot els moviments fins el moment
	while 1:
		while aIn: #quan vuit, surt
			vf, mov = aIn.pop ()
			for i in Generator (m, n):
				v = Canvi (vf, i)
				txt = Uneix (v)
				if All.has_key (txt):
					if not All[txt]:
						for lola, loli in aOut:# em acabat
							if lola == v: return mov + [i,'T'] + loli
						return "Puta merda"# Ha petat, mola muhahahah
				else:
					All[txt] = True
					atmp.append ( (v, mov + [i]) )
		aIn, atmp = atmp, aIn
		while aOut:
			vf, mov = aOut.pop ()
			for i in Generator (m, n):
				v = Canvi (vf, i)
				txt = Uneix (v)
				if All.has_key (txt):
					if All[txt]:
						for lola, loli in aIn:
							if lola == v: return loli + ['T',i] + mov
						return "Merdeta 2"
				else:
					All[txt] = False
					atmp.append ( (v, [i] + mov) )
		aOut, atmp = atmp, aOut
# petits elements paral.lels de gran ajuda
def Llegeix (File):
	a = [line[:-1].split (' ') for line in open (File)]
	return [(a[:len (a) /2], [])], [(a[len (a) /2 +1:], [])]
def Uneix (a): return reduce (lambda x, y: x+y, reduce(lambda x, y: x+y, a))
def Generator (m, n):
	for i in xrange(m):
		for j in xrange(1, n):
			yield (i, j, '>')
	for i in xrange(n):
		for j in xrange(1, m):
			yield (i, j, 'V')
def Canvi (mo, i):
	q, w, e = i
	if e == '>':
		m = mo[:] # Aqui no cal copiar tot
		m[q] = m[q][-w:] + m[q][:-w]
		return m
	m = [row[:] for row in mo]
	z = [i[q] for i in m]
	z = z[-w:] + z[:-w]
	for i in xrange(len(m)):
		m[i][q] = z[i]
	return m
def Invert (a):
	q = []
	for i in a:
		if i[2] == '>': q.append ( (i[0], i[1], '<') )
		else: q.append ( (i[0], i[1], 'A') )
	return q
