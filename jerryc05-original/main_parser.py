
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