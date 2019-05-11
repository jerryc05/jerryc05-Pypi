__version__ = '0.1.7a0'

import urllib.request

with urllib.request.urlopen('https://pypi.org/project/jerryc05/', timeout=1
                            ) as r:
    r_read: bytes = r.read()
    start = r_read.find(b'package-header__name')
    start = r_read.find(b'c05', start) + 4
    end = r_read.find(b'\n', start)
    latest = r_read[start:end].decode().split('.')

    current = __version__.split('.')
    current_last = current[-1]
    for i in range(0, len(current_last)):
        if current_last[i].isalpha():
            current.remove(current_last)
            current.append(f'{int(current_last[:i]) - .5}')
            break
    if current < latest:
        import jerryc05.mod_12306.mod_parser
        colored_text = jerryc05.mod_12306.mod_parser.colored_text
        colored_text(f'New version {".".join(latest)} is available!!!\n'
              'Upgrade using command "pip3 install -U jerryc05".\n','yellow')
