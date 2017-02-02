from distutils.core import setup
import py2exe, os

# setup(console=['org_e.py'])
Mydata_files = [('images', [os.path.join('images','Org-E bg.PNG'), os.path.join('images','Org-E Logo.png')])]
setup(
    # options = {'py2exe': {'includes':['sip', 'PyQt4.QtCore', 'PyQt4.QtGui']}},
    options = {'py2exe': {'includes':['sip'], 'bundle_files': 1, 'compressed': True}},
    scripts = ['shell_script.sh'],
    data_files = Mydata_files,
    windows = [{'script': "org_e.py", 'icon_resources': [(0, os.path.join('images','Org-E_Logo.ico'))]}],
    zipfile = None,
)
