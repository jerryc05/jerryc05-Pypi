if __name__ == "__main__":
	import os
	import shutil
	import sys
	import multiprocessing as mp
	import python_minifier

	rmtree = shutil.rmtree
	rmtree('jerryc05', True)

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
				f2.write(
					python_minifier.minify(
						f1.read(),
						remove_literal_statements=True,
						rename_globals=True,
						preserve_globals=[
							'main',
							'station_name',
							'ticket_count',
							'colored_text',
						]
					) if '.py' == file_name[-3:] and file_name not in exclude
					else f1.read()
				)
	print('Shrinking finished!!')

	rmtree = shutil.rmtree
	mp.Process(target=rmtree, args=('dist', True)).start()
	mp.Process(target=rmtree, args=('build', True)).start()

	argv = sys.argv
	argv.append('bdist_wheel')  # do not delete import setup
	import setup

	mp.Process(target=rmtree, args=('build', True)).start()

	# noinspection PyProtectedMember
	import pip._internal as pip

	for dir_path, _, file_names in os.walk('dist'):
		pip.main(
			fr'install -U --pre --force-reinstall dist/{file_names[0]}'.split())
		break

	import twine.__main__ as twine

	argv[1:] = r'upload --verbose -u jerryc05 dist\*'.split()
	twine.main()
	input('All done!!')