# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages
from telescopy.version import __version__

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


setup(
    name='telescopy',
    version=__version__,
    description='Simulate astronomical observations',
    long_description=readme,
    author='Kieran Leschinski',
    author_email='kieran.leschinski@univie.ac.at',
    url='https://github.com/astronomyk/TelescoPy',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
    # packages=find_packages()
)
