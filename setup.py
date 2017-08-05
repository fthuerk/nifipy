"""
pyranger setup module
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nifipy',
    version='0.1.0',
    description='A Nifi REST wrapper and command line tool',
    long_description=long_description,
    url='https://github.com/condla/nifipy',
    author='Stefan Kupstaitis-Dunkler',
    author_email='stefan.dun@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='REST client wrapper apache nifi',
    packages=find_packages(),
    install_requires=['requests', 'plac'],
    extras_require={ },
    package_data={},
    data_files=[],

    entry_points={
        'console_scripts': [
            'nifipy=nifipy:__main__',
        ],
    },
)
