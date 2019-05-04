def station_name(station_name_js='station_name.js',
                 station_name_py='station_name.py') -> None:
    js_list = []
    with open(station_name_js, encoding='utf-8') as __js:
        js: str = __js.read()
        start = js.find("'")
        if start == -1:
            raise SystemError(
                'Parsing js failed: "=" not found in "station_name.js"')
        start += 1
        if js[start] == '@':
            start += 1
        end = js.find("'", start)
        __js_list = js[start:end].split('@')
        for _ in __js_list:
            js_list.append(_.split('|'))
        import operator
        js_list.sort(key=operator.itemgetter(4))

    with open(station_name_py, 'w', encoding='utf-8') as station:
        station.write('def parse(s):\n\tx=((')

        __first_letter = 'a'
        for _ in js_list:
            first_letter = _[4][0]
            while first_letter != __first_letter:
                station.write('),\n(')
                __first_letter = chr(ord(__first_letter) + 1)
            station.write(f'{tuple(_)},\n')

        station.write('))\n'
                      '\tr=[]\n'
                      '\tfor _ in x[ord(s[0])-97]:\n'
                      '\t\tif s in _[4] or s in _[3]:\n'
                      '\t\t\tr.append(_)\n'
                      '\treturn r')


def ticket_count(num: str) -> str:
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


def colored_text(text: str,
                 fore='RESET',
                 back='RESET',
                 style='RESET_ALL') -> None:
    r"""Print text in colored format.

    :param text: Text to format.
    :param fore: Foreground color to format, default='RESET'.
    :param back: Background color to format, default='RESET'.
    :param style: Style to format, default='RESET_ALL'.

    Available colors:
        RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, BLACK, RESET.

    Available styles:
        DIM, NORMAL, BRIGHT, RESET_ALL.
    """

    fore = fore.upper()
    back = back.upper()
    style = style.upper()

    import colorama
    colorama.init(autoreset=True)
    c_fore = colorama.Fore
    fores = {
        'RED': c_fore.RED,
        'GREEN': c_fore.GREEN,
        'YELLOW': c_fore.YELLOW,
        'BLUE': c_fore.BLUE,
        'MAGENTA': c_fore.MAGENTA,
        'CYAN': c_fore.CYAN,
        'WHITE': c_fore.WHITE,
        'BLACK': c_fore.BLACK,
        'RESET': c_fore.RESET,
    }
    if back == 'RESET' and style == 'RESET_ALL':
        print(f'{fores.get(fore.upper(), "")}{text}')
        return

    c_back = colorama.Back
    backs = {
        'RED': c_back.RED,
        'GREEN': c_back.GREEN,
        'YELLOW': c_back.YELLOW,
        'BLUE': c_back.BLUE,
        'MAGENTA': c_back.MAGENTA,
        'CYAN': c_back.CYAN,
        'WHITE': c_back.WHITE,
        'BLACK': c_back.BLACK,
        'RESET': c_back.RESET,
    }
    c_style = colorama.Style
    styles = {
        'DIM': c_style.DIM,
        'NORMAL': c_style.NORMAL,
        'BRIGHT': c_style.BRIGHT,
        'RESET_ALL': c_style.RESET_ALL,
    }
    print(f'{styles.get(style.upper(), "")}'
          f'{fores.get(fore.upper(), "")}'
          f'{backs.get(back.upper(), "")}'
          f'{text}')


# colored_text('red', 'red')
# station_name('jerryc05/mod_12306/station_name.js',
#              'jerryc05/mod_12306/station_name.py')
