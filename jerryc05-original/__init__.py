__version__ = '0.1.7a3'

import urllib.request as u_req
try:
    print(end='Checking for updates...\r')
    with u_req.urlopen('https://pypi.org/pypi/jerryc05/json',
                                timeout=1) as r:
        import json
        js = json.loads(r.read())
        r_latest = js['info']['version']
        latest = r_latest.split('.')
        current = __version__.split('.')
        current_last = current[-1]
        for index, char in enumerate(current_last):
            if char.isalpha():
                current.remove(current_last)
                current.append(f'{int(current_last[:index]) - .5}')
                break
        if current < latest:
            import jerryc05.mod_parser as j_parser
            colored_text = j_parser.colored_text
            colored_text(f'New version {r_latest} is available!!!\n'
                         'Upgrade using command "pip3 install -U jerryc05".\n', 'yellow')
except OSError:
    print('')
