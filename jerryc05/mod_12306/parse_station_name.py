def parse(station_name: str = 'station_name.js'):
    js_list: list = []
    with open(station_name, encoding='utf-8') as __js:
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

    with open('train_station.py', 'w', encoding='utf-8') as station:
        from bisect import bisect
        indice = [bisect(js_list, chr(ord('a') + x))
                  for x in range(0, 27)]
        for i in range(0, 26):
            station.write(f'def __{chr(ord("a")+i)}():\n return (')
            for index in range(indice[i], indice[i+1]):
                station.write(f"'{js_list[index]}',\n")
            station.write(')\n')

        station.write('''\
def parse(s)->str:
 from bisect import bisect;
 i=bisect(\
''')


if __name__ == "__main__":
    parse()
