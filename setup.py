from setuptools import setup

extras_require = {}
extras_require['test'] = { 'pytest~=3.5' }
extras_require['build'] = { 'sphinx~=3.2.1' }

setup(extras_require=extras_require)
