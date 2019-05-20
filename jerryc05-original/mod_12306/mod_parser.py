def station_name(
				station_name_js='station_name.js',
				station_name_py='station_name.py'
) -> None:
	_open = open

	js_list = []
	with _open(station_name_js, encoding='utf-8') as __js:
		js = __js.read()
		start = js.find("'")
		if start == -1:
			raise SystemError(
				'Parsing js failed: "=" not found in "station_name.js"'
			)
		start += 1
		if js[start] == '@':
			start += 1
		end = js.find("'", start)
		__js_list = js[start:end].split('@')
		for _ in __js_list:
			js_list.append(_.split('|'))
		import operator
		js_list.sort(key=operator.itemgetter(4))

	with _open(station_name_py, 'w', encoding='utf-8') as station:
		station.write('def parse(s):\n\tx=((')

		__first_letter = 'a'
		for _ in js_list:
			first_letter = _[4][0]
			while first_letter != __first_letter:
				station.write('),\n(')
				__first_letter = chr(ord(__first_letter) + 1)
			station.write(f'{tuple(_)},\n')

		station.write(
			'))\n'
			'\tr=[]\n'
			'\tfor _ in x[ord(s[0])-97]:\n'
			'\t\tif s in _[4] or s in _[3]:\n'
			'\t\t\tr.append(_)\n'
			'\treturn r'
		)


def ticket_count(num='?') -> str:
	r"""Parse and format ticket count.

	:param num: Number of tickets
	:return: ''->'\', '无'->'0', '有'->' 20+'
	"""

	if num == '':
		return '\\'
	if num == '无':
		return '0'
	if num == '有':
		return ' 20+'
	else:
		return num

# station_name('jerryc05/mod_12306/station_name.js',
#              'jerryc05/mod_12306/station_name.py')