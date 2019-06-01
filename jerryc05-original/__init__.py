# avoid using ".postN" and ".devN" postfix
__version__ = '0.2a0'

# check for update
print(end='Checking for updates...\r')

import urllib.request as u_req

try:
    with u_req.urlopen('https://pypi.org/pypi/jerryc05/json', timeout=1) as r:
        import json
        import jerryc05.main_parser as j_parser

        colored_text = j_parser.colored_text

        js = json.loads(r.read())
        r_latest = js['info']['version']
        latest = r_latest.split('.')
        current = __version__.split('.')
        current_last = current[-1]
        for index, char in enumerate(current_last):
            if char.isalpha():
                current.remove(current_last)
                # version number before a/b/rc notation
                current.append(f'{int(current_last[:index]) - .5}')
                # version number  after a/b/rc notation
                current.append(current_last[index + 1:])
                break
        if current < latest:

            colored_text(
                f'New version {r_latest} is available!!!\n'
                'Upgrade using command "pip3 install -U jerryc05".\n',
                'yellow')
        else:
            colored_text('Version up to date! Well done :)\r', 'green')
except OSError:
    print(end='Cannot connect to PyPI repository :(\r')
