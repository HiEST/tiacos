def myreadln(f):
	tmp = ''
	out = ''
	while tmp <> '\n':
		tmp = f.read(1)
		if tmp == '':
			break
		out = out + tmp
	return out

print 'Starting the program'

s = 'example.pdb'

f = open( s, 'r')
print 'File '+s+' openend'


myf = myreadln(f)
while (myf <> ''):
	if myf[:4] == 'ATOM' :
		print myf, f.tell()
	myf = myreadln(f)

