# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='color_plot',
    version='0.1.2',
    description="colorplot",
    author='Yusuke Muraki',
    author_email='',
    install_requires=['numpy', 'pyshp', 'matplotlib', 'geopandas', 'os'],
    url='https://github.com/yusukeMuraki/color_plot',
    license=license,
    packages=['color_plot']
)
