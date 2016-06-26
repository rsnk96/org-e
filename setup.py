from distutils.core import setup
import py2exe, os, sys

# setup(console=['org_e.py'])
Mydata_files = [('images', ['Org-E bg.PNG'])]
setup(
    options = {'py2exe': {'bundle_files': 2, 'compressed': True}},
    data_files = Mydata_files,
    windows = [{'script': "org_e.py", 'icon_resources': [(0, 'Org.ico')]}],
    zipfile = None,
)