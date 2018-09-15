from distutils.core import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='pycrackwatch',
    version='1.0.0',
    author='cominixo',
    author_email='lucasdutraluza@gmail.com',
    long_description=long_description,
    install_requires=[
        'requests==2.19.1'
    ],
    description='A Python wrapper for the CrackWatch API',
    packages=[
        'pycrackwatch',
    ],
)
