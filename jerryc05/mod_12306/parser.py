def station_name(
    station_name_js: str = 'station_name.js',
    train_station_py: str = 'train_station.py'
) -> None:
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
    r'''Parse and format ticket count.

    Args:
        num (str)   : Number of tickets.

    Returns:
        str: \ for '', 0 for '无', 20+ for '有'.

    '''

    return {
        '': '\\',
        '无': '0',
        '有': '20+',
    }.get(num, num)


def colored_text(
    text: str,
    fore: str = 'RESET',
    back: str = 'RESET',
    style: str = 'RESET_ALL'
) -> None:
    r'''Print text in colored format.

    Args:
        text (str)  : Text to format.
        fore (str)  : Foreground color to format, default='RESET'.
        back (str)  : Background color to format, default='RESET'.
        style (str) : Style to format, default='RESET_ALL'.

    Available colors: 
        RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, BLACK, RESET.

    Available styles:
        DIM, NORMAL, BRIGHT, RESET_ALL.
    '''

    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    fores = {
        'RED': Fore.RED,
        'GREEN': Fore.GREEN,
        'YELLOW': Fore.YELLOW,
        'BLUE': Fore.BLUE,
        'MAGENTA': Fore.MAGENTA,
        'CYAN': Fore.CYAN,
        'WHITE': Fore.WHITE,
        'BLACK': Fore.BLACK,
        'RESET': Fore.RESET,
    }
    backs = {
        'RED':  Back.RED,
        'GREEN':  Back.GREEN,
        'YELLOW':  Back.YELLOW,
        'BLUE':  Back.BLUE,
        'MAGENTA':  Back.MAGENTA,
        'CYAN':  Back.CYAN,
        'WHITE':  Back.WHITE,
        'BLACK':  Back.BLACK,
        'RESET':  Back.RESET,
    }
    styles = {
        'DIM': Style.DIM,
        'NORMAL': Style.NORMAL,
        'BRIGHT': Style.BRIGHT,
        'RESET_ALL': Style.RESET_ALL,
    }
    print(
        f'{styles.get(style.upper(),styles["RESET_ALL"]) if style=="RESET_ALL" else ""}'
        f'{fores.get(fore.upper(), fores["RESET"])}'
        f'{backs.get(back.upper(), backs["RESET"])}'
        f'{text}'
    )


if __name__ == "__main__":
    pass
    # colored('test', 'red')
    # colored('test', 'red', 'green', 'bright')
    # station_name('jerryc05/mod_12306/station_name.js',
    #              'jerryc05/mod_12306/train_station.py')
