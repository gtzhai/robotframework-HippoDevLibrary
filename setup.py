import re
from os.path import abspath, dirname, join
from setuptools import setup, find_packages


CURDIR = dirname(abspath(__file__))

CLASSIFIERS = '''
Development Status :: 5 - Production/Stable
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 3
Topic :: Software Development :: Testing
Framework :: Robot Framework
Framework :: Robot Framework :: Library
'''.strip().splitlines()

with open(join(CURDIR, 'src', 'HippoDevLibrary', '__init__.py')) as f:
    VERSION = re.search("\n__version__ = '(.*)'", f.read()).group(1)
with open(join(CURDIR, 'README.rst'), 'r', encoding='UTF-8') as f:
    DESCRIPTION = f.read()
with open(join(CURDIR, 'requirements.txt'), 'r', encoding='UTF-8') as f:
    REQUIREMENTS = f.read().splitlines()


setup(
    name             = 'robotframework-HippoDevLibrary-dev',
    version          = VERSION,
    description      = 'Instruments testing library for Robot Framework',
    long_description = DESCRIPTION,
    author           = 'gtzhai',
    author_email     = 'gtzhai@163.com',
    url              = '',
    license          = 'Apache License 2.0',
    keywords         = '',
    platforms        = 'any',
    classifiers      = CLASSIFIERS,
    install_requires = REQUIREMENTS,
    package_dir      = {'': 'src'},
    packages         = find_packages('src')
)
