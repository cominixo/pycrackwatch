from distutils.core import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='pycrackwatch',
    version='1.0.0',
    author='cominixo',
    author_email='lucasdutraluza@gmail.com',
    long_description=long_description,
    description='A Python wrapper for the CrackWatch API',
    packages=[
        'pycrackwatch',
    ],
)
