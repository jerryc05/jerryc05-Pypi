from setuptools import setup, find_packages
from jerryc05.__init__ import __version__

long_description = ''
with open("README.md", "r") as readme:
    long_description = readme.read()

github_repo: str = 'https://github.com/jerryc05/jerryc05-Pypi'
#
packages: list = find_packages(
    exclude=['contrib', 'docs', 'tests*'])  # ['jerryc05']

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
    license='agpl-3.0',
    classifiers=[
        'Development Status :: 1 - Planning',
         # 'Development Status :: 2 - Pre-Alpha',
         # 'Development Status :: 3 - Alpha'
         # 'Development Status :: 4 - Beta'
         # 'Development Status :: 5 - Production/Stable'
         # 'Development Status :: 6 - Mature'
         # 'Development Status :: 7 - Inactive'

         'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
         'Natural Language :: English',
        #  'Operating System :: Microsoft :: Windows',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.6',
         'Programming Language :: Python :: 3.7',
         # 'Programming Language :: Python :: 3.8',
         # 'Programming Language :: Python :: Implementation :: CPython'
    ],
    keywords=[
        'jerryc05',
        'tools', ],
    # project_urls={
    #     'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
    #     'Funding': 'https://donate.pypi.org',
    #     'Say Thanks!': 'http://saythanks.io/to/example',
    #     'Source': 'https://github.com/pypa/sampleproject/',
    #     'Tracker': 'https://github.com/pypa/sampleproject/issues',
    # },
    packages=packages,
    install_requires=[
        'colorama',
        # 'requests',
    ],
    python_requires='~=3.6',
    # package_data={
    # If any package contains *.txt files, include them:
    # '': ['*.txt'],
    # And include any *.dat files found in the 'data' subdirectory
    # of the 'mypkg' package, also:
    # 'mypkg': ['data/*.dat'],
    # },
    # data_files=[('my_data', ['data/data_file'])],
    zip_safe=True,
    entry_points={
        'console_scripts': ['jerryc05 = jerryc05.__main__:main'],
    },
)
