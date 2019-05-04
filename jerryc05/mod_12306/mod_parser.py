L=print
H=open
J='RESET_ALL'
E=str
D='RESET'
C=''
def station_name(station_name_js='station_name.js',station_name_py='station_name.py'):
	P='@';O="'";N='utf-8';F=[]
	with H(station_name_js,encoding=N)as I:
		B=I.read();A=B.find(O)
		if A==-1:raise SystemError('Parsing js failed: "=" not found in "station_name.js"')
		A+=1
		if B[A]==P:A+=1
		J=B.find(O,A);K=B[A:J].split(P)
		for C in K:F.append(C.split('|'))
		import operator as L;F.sort(key=L.itemgetter(4))
	with H(station_name_py,'w',encoding=N)as D:
		D.write('def parse(s):\n\tx=((');G='a'
		for C in F:
			M=C[4][0]
			while M!=G:D.write('),\n(');G=chr(ord(G)+1)
			D.write(f"{tuple(C)},\n")
		D.write('))\n\tr=[]\n\tfor _ in x[ord(s[0])-97]:\n\t\tif s in _[4] or s in _[3]:\n\t\t\tr.append(_)\n\treturn r')
def ticket_count(num):
	A=num
	if A==C:return'\\'
	if A=='无':return'0'
	if A=='有':return' 20+'
	else:return A
def colored_text(text,fore=D,back=D,style=J):
	V='BLACK';U='WHITE';T='CYAN';S='MAGENTA';R='BLUE';Q='YELLOW';P='GREEN';O='RED';G=style;F=back;E=fore;E=E.upper();F=F.upper();G=G.upper();import colorama as H;H.init(autoreset=True);A=H.Fore;K={O:A.RED,P:A.GREEN,Q:A.YELLOW,R:A.BLUE,S:A.MAGENTA,T:A.CYAN,U:A.WHITE,V:A.BLACK,D:A.RESET}
	if F==D and G==J:L(f"{K.get(E.upper(),'')}{text}");return
	B=H.Back;M={O:B.RED,P:B.GREEN,Q:B.YELLOW,R:B.BLUE,S:B.MAGENTA,T:B.CYAN,U:B.WHITE,V:B.BLACK,D:B.RESET};I=H.Style;N={'DIM':I.DIM,'NORMAL':I.NORMAL,'BRIGHT':I.BRIGHT,J:I.RESET_ALL};L(f"{N.get(G.upper(),'')}{K.get(E.upper(),'')}{M.get(F.upper(),'')}{text}")