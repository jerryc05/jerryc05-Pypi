B=list
V=tuple
A=str
L=None
K=int
J=input
G=print
F=len
def query_city(d_city,a_city):
	Q=' ';H='';import jerryc05.mod_12306.station_name;M=jerryc05.mod_12306.station_name.parse;B=d_city.lower();I=[];import operator as N;O=N.itemgetter
	while F(I)<2:
		A=L
		while not A or not A[0][0]:
			while not B or not 96<ord(B[0])<123:B=J(f"Invalid argument: Expected letters but found {B}, retry: ")
			A=M(B)
			if not A:A=[(H,H,H,'--- NO RESULT! ---',H,H)]
			A.sort(key=O(3));G('+-----+--------------------+------+--------------+\n| No. |    STATION NAME    | CODE |   CHN NAME   |\n+-----+--------------------+------+--------------+')
			for (P,D) in enumerate(A):G(f"| {P+1:3} | {D[3]:18} | {D[2]:4} | {D[1]:{12-F(D[1])+D[1].count(' ')}} |")
			G('+-----+--------------------+------+--------------+')
			if not A[0][0]:A=L;B=J(f'City name "{B}" not found, retry: ')
		E=K(J('Index number: '))-1
		while not 0<=E<F(A):E=K(J('Index number invalid, retry: '))-1
		C=A[E];G(f"""Chosen station name:
+-----+--------------------+------+--------------+
| {E+1:3} | {C[3]:18} | {C[2]:4} | {C[1]:{12-F(C[1])+C[1].count(" ")}} |
+-----+--------------------+------+--------------+

""");I.append((C[1],C[2]));B=a_city.lower()
	return I
def main(args=L):
	H=args;E='0';D='\\'
	if not H:H=[]
	T=F(H)
	if T<3:raise SystemError(f"Missing argument: Expected 3 but found {T}.")
	A=H[2]
	while not F(A)==10 or not K(A[:4])>2018 or not 0<K(A[5:7])<13 or not 0<K(A[8:])<32:
		if F(A)==8:A=f"{A[:4]}-{A[4:6]}-{A[6:8]}"
		else:A=J(f'Date "{A}" invalid, retry: ')
	W,X=query_city(H[0],H[1]);import urllib.request
	with urllib.request.urlopen(f"https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={A}&leftTicketDTO.from_station={W[1]}&leftTicketDTO.to_station={X[1]}&purpose_codes=ADULT")as Y:
		import json;G('+-------+-------+-------+-------+-------+-------+-------+---------+---------+------+------+\n| TRAIN | START |  END  | TOTAL |  VIP  |  1ST  |  2ND  |  SOFT-  |  HARD-  | HARD | NONE |\n|  NO.  | TIME: | TIME: | TIME: | CLASS | CLASS | CLASS | SLEEPER | SLEEPER | SEAT | SEAT |\n+-------+-------+-------+-------+-------+-------+-------+---------+---------+------+------+');import jerryc05.mod_12306.mod_parser;C=jerryc05.mod_12306.mod_parser.ticket_count;U=jerryc05.mod_12306.mod_parser.colored_text;L=json.loads(Y.read())['data']['result']
		if not L:L='|||-----|||||-----|-----|-----|||||||||||||||||||||||',
		for Z in L:
			B=Z.split('|');a=B[3];b=B[8];c=B[9];d=B[10];M=C(B[32]);N=C(B[31]);I=C(B[30]);O=C(B[23]);P=C(B[28]);Q=C(B[29]);R=C(B[26]);S=f"| {a:5} | {b:5} | {c:5} | {d:^5} | {M:^5} | {N:^5} | {I:^5} | {O:^7} | {P:^7} | {Q:^5}| {R:^5}|"
			if not I==D and not I==E:U(S,'green',style='bright')
			elif(M==D or M==E)and(N==D or N==E)and(I==D or I==E)and(O==D or O==E)and(P==D or P==E)and(Q==D or Q==E)and(R==D or R==E):U(S,'red',style='dim')
			else:G(S)
		G('+-------+-------+-------+-------+-------+-------+-------+---------+---------+------+------+')