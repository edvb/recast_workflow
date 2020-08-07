from setuptools import setup

extras_require = {}
extras_require['test'] = { 'pytest~=3.5' }

setup(extras_require=extras_require)
