# Need this to configure our package- give any background information so it can be identififed further down the line
# To describe out module: who wrote it, owns it, version, email, url to business, background info etc.
# Background to application/package
# E.G
# version="1.0"
# description="Python app"
# author="Benas Jasilionis"
# url="https://www.python.org"

from setuptools import  setup

setup(name="app") #every package needs at least a name

#to install every app in a folder do = pip install .