from setuptools import setup

setup(
    name='viral-amplicons',
    version='0.1',
    description='Find amplicons for viral metagenomics',
    url='http://github.com/Ellmen/viral-amplicons',
    author='Isaac Ellmen',
    author_email='isaac.ellmen@uwaterloo.ca',
    packages=['amplicons'],
    install_requires=[
        'cogent3',
        'primerprospector @ git+https://github.com/Ellmen/primerprospector3'
    ],
    entry_points={
        'console_scripts': ['amplicons=amplicons.command_line:main'],
    }
)
