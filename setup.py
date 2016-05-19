import os
from setuptools import setup, find_packages

# Establish a consistent base directory relative to the setup.py file
os.chdir(os.path.abspath(os.path.dirname(__file__)))

setup(
    name='myapp',
    version='0.0.1',
    description='Alias Sync API',
    long_description='{0}'.format(open('README.rst').read()),
    author='Stephen Lowrie',
    install_requires=["falcon"],
    packages=find_packages(exclude=('tests*', 'docs')),
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ))
