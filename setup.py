# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='color_plot',
    version='0.1.0',
    description='plot color map from city data',
    long_description=readme,
    author='Yusuke Muraki',
    author_email='',
    install_requires=['numpy', 'shapefile', 'matplotlib', 'geopanads'],
    url='https://github.com/yusukeMuraki/color_plot',
    license=license,
    packages=['color_plot']
)
