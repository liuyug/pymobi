#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import sys

from distutils.core import setup
import distutils.command.install_scripts

from pymobi import __name__ as __appname__
from pymobi import __version__
from pymobi import __license__
from pymobi import __author__
from pymobi import __email__


class my_install(distutils.command.install_scripts.install_scripts):
    """ remove script ext """
    def run(self):
        distutils.command.install_scripts.install_scripts.run(self)
        if sys.platform != 'win32':
            for script in self.get_outputs():
                if script.endswith(".py"):
                    new_name = script[:-3]
                    if os.path.exists(new_name):
                        os.remove(new_name)
                    os.rename(script, new_name)
        return

with open('README.rst') as f:
    long_description = f.read()

setup(
    name=__appname__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    license=__license__,
    url='https://github.com/liuyug/pymobi.git',
    description='Mobipocket tools',
    long_description=long_description,
    platforms=['noarch'],
    packages=[
        'pymobi',
    ],
    package_dir={'pymobi': 'pymobi'},
    data_files=[(
        'share/pymobi', [
            'README.rst',
            'MANIFEST.in',
        ]
    )],
    scripts=['unpackmobi.py', 'infomobi.py', 'removesrcs.py', 'titlemobi.py'],
    cmdclass={"install_scripts": my_install},
)
