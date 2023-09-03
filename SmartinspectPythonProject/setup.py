import os
from setuptools import setup, find_packages

# our package constants.
from smartinspectpython.siconst import (
    VERSION
)

# setup constants.
NAME = 'smartinspectPython'
DESCRIPTION = 'SmartInspect Python3 Library'
#VERSION = '0.0.1'   # pulled from package constants above.



# if installing using less than Python v3, then stop the install!
import sys
if sys.version_info < (3,0):
    sys.exit('Sorry, Python < 3.0 is not supported.')

# function to read the contents of the README.md file, and return it to the caller.
def readme(pathName:str):
    with open(pathName) as f:
        return f.read()

# function to build a list of files in a directory.
def getDirFilesList(pathName:str) -> list[str]:
    print(str.format("getting list of files in path \"{0}\" ...", pathName))
    dir_list = os.listdir(pathName)
    files:list[str] = []
    for file in dir_list:                       # process all matches.
        if os.path.isfile(pathName + file):     # only include files (not directories)
            files.append(str(pathName + file))
    return files

# package setup.
setup(
    # basic package information.
    name=NAME,
    version=VERSION,
    author='Todd Lucas',
    author_email='<thlucas@yahoo.com>',
    description=DESCRIPTION,
    # use the README.md markdown file for the description.
    long_description_content_type='text/markdown',
    long_description=readme('README.md'),
    # find and include all packages in the project (anything with an '__init__.py' file).
    packages=find_packages(),
    # place documentation folder named "docs" in the package folder.
    data_files=[
        ('../../smartinspectpython/docs', getDirFilesList('docspdoc/build/')),
        ('../../smartinspectpython/docs/smartinspectpython', getDirFilesList('docspdoc/build/smartinspectpython/')),
    ],
    # set minimum python version requirement.
    python_requires='>3.4.1',
    # set minimum dependencies requirements.
    install_requires=[
        'pycryptodome >= 3.0',
        'pywin32 >= 300 ; platform_system=="Windows"'
    ],
    # set keywords to associate this package with on Pypi.org.
    keywords=['python', 'smartinspect', 'logging', 'trace', 'tracing', 'debugging'],
    # set classifiers to associate this package with on Pypi.org.
    classifiers=[
        'Development Status :: 5 - Production/Stable',
#       'Development Status :: 2 - Pre-Alpha',
#       'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Topic :: Software Development',
        'Topic :: System :: Logging',
        'Natural Language :: English',
        'License :: Free To Use But Restricted',
    ]
    # provide some links to list on the Pypi.org site.
    #project_urls={
    #    'Documentation': 'https://example.com/documentation/',
    #    'GitHub': 'https://github.com/foobar/foobar/',
    #    'Changelog': 'https://github.com/foobar/foobar/blob/master/CHANGELOG.md',
    #},
)