__version__ = '0.1.6'

import urllib.request

with urllib.request.urlopen('https://pypi.org/project/jerryc05/') as r:
    r_read: bytes = r.read()
    start = r_read.find(b'package-header__name')
    start = r_read.find(b'c05', start) + 4
    end = r_read.find(b'\n', start)
    latest = r_read[start:end].decode('utf-8')

    current = __version__.split('.')
    current_last = current[-1]
    for _ in range(0, len(current_last)):
        if current_last[_].isalpha():
            current.remove(current_last)
            current.append(f'{int(current_last[:_]) - .1}')
            break
    if current < latest.split('.'):
        print(f'New version {latest} available!!!\n'
              'Type "pip3 install -U jerryc05" to upgrade.')
