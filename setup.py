from setuptools import find_packages, setup
import os.path as os_path
from jerryc05.__init__ import __version__

readme = 'README.md'
if os_path.isfile(readme):
	with open(readme, 'r', encoding='utf-8') as readme:
		long_description = readme.read()
else:
	long_description = ''

github_repo = 'https://github.com/jerryc05/jerryc05-Pypi'

# https://packaging.python.org/guides/distributing-packages-using-setuptools/#setup-args
setup(
	name='jerryc05',
	version=__version__,
	description='A software collection developed by @jerryc05',
	long_description=long_description,
	long_description_content_type="text/markdown",
	author='Jerry Chen',
	author_email='jerryc05@qq.com',
	url=github_repo,
	# download_url=f'{github_repo}/releases',
	# license='gpl-3.0',
	classifiers=(
		# 'Development Status :: 1 - Planning',
		'Development Status :: 2 - Pre-Alpha',
		# 'Development Status :: 3 - Alpha'
		# 'Development Status :: 4 - Beta'
		# 'Development Status :: 5 - Production/Stable'
		# 'Development Status :: 6 - Mature'
		# 'Development Status :: 7 - Inactive'

		'Environment :: Console',
		'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		# 'Programming Language :: Cython',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: Implementation :: CPython',
		'Programming Language :: Python :: Implementation :: PyPy',
	),
	keywords=(
		'jerryc05',
		'tools',
	),
	# project_urls={
	#     'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
	#     'Funding': 'https://donate.pypi.org',
	#     'Say Thanks!': 'http://saythanks.io/to/example',
	#     'Source': 'https://github.com/pypa/sampleproject/',
	#     'Tracker': 'https://github.com/pypa/sampleproject/issues',
	# },
	packages=(find_packages(exclude=(
		'contrib',
		'docs',
		'tests*',
		'jerryc05-original',
		'jerryc05-original.*',
	))),
	# package_data={
	#     # If any package contains *.txt files, include them:
	#     '': ['*.txt'],
	#     # And include any *.dat files found in the 'data' subdirectory
	#     # of the 'mypkg' package, also:
	#     'mypkg': ['data/*.dat'],
	# },
	install_requires=(
		'colorama',
		# 'docopt',
		# 'requests',
	),
	python_requires='~=3.6',
	# data_files=[('my_data', ['data/data_file'])],
	zip_safe=True,
	entry_points={
		'console_scripts': (
			'jerryc05 = jerryc05.__main__:main',
		),
	},
)