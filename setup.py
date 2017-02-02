# from distutils.core import setup
from setuptools import setup
import os
import glob

setup( name='org-e',
    version='0.4',
    author='rsnk',
    author_email='rsnk96@gmail.com',
    description='Declutter your folders and organize them neatly',
    install_requires=['PyQt5'],
    url='https://github.com/rsnk96/OrgE',
    packages=['OrgE'],
    package_data={'OrgE':glob.glob(os.path.join('OrgE','images','*'))},
    include_package_data=True,
    entry_points={'console_scripts': ['org-e=OrgE.__main__:main'], },
)