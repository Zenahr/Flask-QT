import sys
from setuptools import setup, find_packages

#Distribute py wheels
#python3 setup.py bdist_wheel sdist
#twine check dist/*
#cd dist 
#twine upload *

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Flask-QT',
    version='0.1.0',
    author='Zenahr Barzani',
    author_email='zenmatica@gmail.com',
    packages=['flaskqt'],
    scripts=['examples/demo.py'],
    url='https://github.com/Zenahr/Flask-QT/',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    description='FlaskQT allow you to run flask-powered, cross-platform desktop applications.',
    long_description=open('README.md').read(),
    install_requires=requirements,
    python_requires='>=3.7',
)