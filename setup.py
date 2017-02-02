# from distutils.core import setup
from setuptools import setup, find_packages
import os
import glob

setup( name='org-e',
    version='0.5',
    author='rsnk',
    author_email='rsnk96@gmail.com',
    description='Organizes files into folders based on type, declutters your life',
    url='https://github.com/rsnk96/org-e',
    packages=find_packages(),
    package_data={'OrgE':[os.path.join('images', 'org-e bg.jpg'), os.path.join('images', 'org-e logo.PNG')]},
    install_requires=['PyQt5'],
    entry_points={'console_scripts': ['org-e=OrgE.__main__:main'], },
    keywords = ['clutter','declutter','organize','sort'],
)