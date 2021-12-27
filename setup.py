from setuptools import setup

setup(
    name='module_alex1',
    version='0.1.0',    
    description='Useful functions for statistics.',
    author='Alex Shchelochkov',
    packages=['module_alex1'],
    install_requires=['numpy>=1.9.0'],

    classifiers=[ 
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
    ],
)