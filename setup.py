# setup.py
import setuptools
from os.path import abspath, dirname, join

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()

setuptools.setup(
    name='strutils',
    version='0.0.1',
    description='Python compound string utility library',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Dictionairy :: Utilities :: Library',
    ],
    keywords='str utility tZE',
    url='http://github.com/tZE/strutils',
    author='tZE',
    author_email='tze@example.com',
    license='MIT',
    py_modules=['strutils'],
    zip_safe=False)
