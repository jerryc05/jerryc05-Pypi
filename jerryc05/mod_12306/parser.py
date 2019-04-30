def station_name(station_name_js: str = 'station_name.js',
                 train_station_py: str = 'train_station.py') -> None:
    js_list: list = []
    with open(station_name_js, encoding='utf-8') as __js:
        js: str = __js.read()
        start = js.find("'")
        if start == -1:
            raise AssertionError(
                'Parsing js failed: "=" not found in "station_name.js"')
        start += 1
        if js[start] == '@':
            start += 1
        end = js.find("'", start)
        js_list = js[start:end].split('@')
        js_list.sort()

    with open(train_station_py, 'w', encoding='utf-8') as station:
        station.write('def parse(s)->list:\n\tx=((')
        alpha: str = 'a'
        for x in js_list:
            first = x[0]
            if first != alpha:
                station.write('),(')
                alpha = first
            station.write(f"'{x}',\n")
        station.write('''))
\tfrom bisect import bisect as b
\tr,i=[],b(x,(s[0],))
\tfor t in x[i]:
\t\tif s in t:
\t\t\tr.append(t.split('|'))
\treturn r\
''')


def ticket_count(num: str) -> str:
    return {
        '': '\\',
        '无': '0',
        '有': '20+',
    }.get(num, num)


if __name__ == "__main__":
    # station_name('jerryc05/mod_12306/station_name.js',
    #              'jerryc05/mod_12306/train_station.py')
