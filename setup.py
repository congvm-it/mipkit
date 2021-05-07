from setuptools import setup, find_packages
from os import path

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

__version__ = '1.4.3'

setup(
    name='mipkit',
    version=__version__,
    description='mipkit',
    packages=find_packages(),
    # package_data={'mipkit': ['faces/*']},
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    author='congvm',
    author_email='congvm.it@gmail.com',
    license='MIT',
    zip_safe=True,
    install_requires=requirements,
    include_package_data=True,
    classifiers=(
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ),
)
