B=list
U=tuple
A=str
L=None
K=int
J=input
H=print
G=len
def query_city(d_city,a_city):
	Q=' ';F='';import jerryc05.mod_12306.station_name;M=jerryc05.mod_12306.station_name.parse;B=d_city.lower();I=[];import operator as N;O=N.itemgetter
	while G(I)<2:
		A=L
		while not A or not A[0][0]:
			while not B or not 96<ord(B[0])<123:B=J(f"Invalid argument: Expected letters but found {B}, retry: ")
			A=M(B)
			if not A:A=[(F,F,F,'--- NO RESULT! ---',F,F)]
			A.sort(key=O(3));H('+-----+--------------------+------+--------------+\n| No. |    STATION NAME    | CODE |   CHN NAME   |\n+-----+--------------------+------+--------------+')
			for (P,D) in enumerate(A):H(f"| {P+1:3} | {D[3]:18} | {D[2]:4} | {D[1]:{12-G(D[1])+D[1].count(' ')}} |")
			H('+-----+--------------------+------+--------------+')
			if not A[0][0]:A=L;B=J(f'City name "{B}" not found, retry: ')
		E=K(J('Index number: '))-1
		while not 0<=E<G(A):E=K(J('Index number invalid, retry: '))-1
		C=A[E];H(f"""Chosen station name:
+-----+--------------------+------+--------------+
| {E+1:3} | {C[3]:18} | {C[2]:4} | {C[1]:{12-G(C[1])+C[1].count(" ")}} |
+-----+--------------------+------+--------------+

""");I.append((C[1],C[2]));B=a_city.lower()
	return I
def main(args=L):
	F='0';E='\\';C=args
	if not C:C=[]
	if G(C)<3:raise SystemError(f'Missing argument: Expected "<d_city> <a_city> <date>" but found {C}.')
	A=C[2]
	while not G(A)==10 or not K(A[:4])>2018 or not 0<K(A[5:7])<13 or not 0<K(A[8:])<32:
		if G(A)==8:A=f"{A[:4]}-{A[4:6]}-{A[6:8]}"
		else:A=J(f'Date "{A}" invalid, retry: ')
	V,W=query_city(C[0],C[1]);import urllib.request
	with urllib.request.urlopen(f"https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={A}&leftTicketDTO.from_station={V[1]}&leftTicketDTO.to_station={W[1]}&purpose_codes=ADULT")as X:
		import json;H('+-------+-------+-------+-------+-------+-------+-------+---------+---------+------+------+\n| TRAIN | START |  END  | TOTAL |  VIP  |  1ST  |  2ND  |  SOFT-  |  HARD-  | HARD | NONE |\n|  NO.  | TIME: | TIME: | TIME: | CLASS | CLASS | CLASS | SLEEPER | SLEEPER | SEAT | SEAT |\n+-------+-------+-------+-------+-------+-------+-------+---------+---------+------+------+');import jerryc05.mod_12306.mod_parser;D=jerryc05.mod_12306.mod_parser.ticket_count;T=jerryc05.mod_12306.mod_parser.colored_text;L=json.loads(X.read())['data']['result']
		if not L:L='|||-----|||||-----|-----|-----|||||||||||||||||||||||',
		for Y in L:
			B=Y.split('|');Z=B[3];a=B[8];b=B[9];c=B[10];M=D(B[32]);N=D(B[31]);I=D(B[30]);O=D(B[23]);P=D(B[28]);Q=D(B[29]);R=D(B[26]);S=f"| {Z:5} | {a:5} | {b:5} | {c:^5} | {M:^5} | {N:^5} | {I:^5} | {O:^7} | {P:^7} | {Q:^5}| {R:^5}|"
			if not I==E and not I==F:T(S,'green',style='bright')
			elif(M==E or M==F)and(N==E or N==F)and(I==E or I==F)and(O==E or O==F)and(P==E or P==F)and(Q==E or Q==F)and(R==E or R==F):T(S,'red',style='dim')
			else:H(S)
		H('+-------+-------+-------+-------+-------+-------+-------+---------+---------+------+------+')