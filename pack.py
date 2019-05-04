import os

import python_minifier

for dir_path, _, file_names in os.walk('jerryc05/'):
    new_dir_path = dir_path.replace('jerryc05', 'jerryc05-minify')
    for file_name in file_names:
        with open(f'{dir_path}{file_name}', 'r', encoding='utf-8') as f1,\
                open(f'{new_dir_path}{file_name}', 'w', encoding='utf-8') as f2:
            f2.write(python_minifier.minify(f1.read()))

# root = 'jerryc05-minify/'
# path = [root]
# file = os.listdir(root)
# (dirpath, dirnames, filenames) in os.walk(mypath)
# while path:
#     current_path = path.pop()
#     while file:
#         with open(file.pop(), 'w+', encoding='utf-8') as f:
#             f.write(python_minifier.minify(f.read()))
