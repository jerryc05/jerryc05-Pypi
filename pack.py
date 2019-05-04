import os
import subprocess

import python_minifier

exclude = ('station_name.py',)

for dir_path, _, file_names in os.walk('jerryc05-original'):
    if 'cache' in dir_path:
        continue
    new_dir_path = dir_path.replace('jerryc05-original', 'jerryc05')
    if not os.path.isdir(new_dir_path):
        os.mkdir(new_dir_path)
    for file_name in file_names:
        with open(f'{dir_path}/{file_name}', 'r', encoding='utf-8') as f1, \
                open(f'{new_dir_path}/{file_name}', 'w+', encoding='utf-8') as f2:
            f2.write(python_minifier.minify(
                f1.read(),
                remove_literal_statements=True,
                rename_globals=True,
                preserve_globals=[
                    'main',
                    'query_city',
                    'station_name',
                    'ticket_count',
                    'colored_text',
                ]
            ) if '.py' == file_name[-3:] and
                 file_name not in exclude else f1.read())
print('Minify done!!')

processes = [
    subprocess.Popen(r'rmdir dist  /s /q', shell=True),
    subprocess.Popen(r'rmdir build /s /q', shell=True)
]
for p in processes:
    p.wait()

subprocess.call(r'python setup.py bdist_wheel', shell=True)
subprocess.Popen(r'rmdir build /s /q', shell=True)
for _, _, file_names in os.walk('dist'):
    subprocess.call(fr'python -m pip install -U --pre --force-reinstall dist/{file_names[0]}',
                    shell=True)
    break
subprocess.call(r'twine upload -u jerryc05 dist\*', shell=True)
input('All done!!')
