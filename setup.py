from setuptools import setup, find_packages

import remontnik


setup(
    name='remontnik',
    version='0.1',
    url='https://github.com/reddi/remontnik/',
    license='MIT',
    author='Eugene Chekalov',
    author_email='evgchekalov@gmail.com',
    description='Test task for remontnik.ru',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'requests >= 2.18.4',
    ],
    entry_points={
        'console_scripts': ['remontnik = remontnik.cli:cli']
    },
)
