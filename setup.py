#!/usr/bin/env python
import os
from sys import version_info
if version_info < (2, 6):
	from distutils.core import setup
else:
	try:
        	from setuptools import setup, find_packages
	except ImportError:
        	from ez_setup import use_setuptools
        	use_setuptools()
        	from setuptools import setup, find_packages


version = "0.0.5"
data_files_installdir = "/usr/share/doc/vmcatcher-%s/examples/" % (version)
if "VIRTUAL_ENV" in os.environ:
    data_files_installdir = 'doc'

setup(name='vmcatcher_eventHndlExpl',
    version=version,
    description="vmcatcher_eventHndl_ON manages images in fedcloud for OpenNebula",
    author="R Rosende Dopazo",
    author_email="grid-admin@cesga.es",
    url="www.cesga.es",
    scripts=['vmcatcher_eventHndl_ON'],
    # data files modified on 12/06/14 in order to allows virtual environments to be installed still  
#    data_files=[('/usr/share/doc/vmcatcher-%s/examples/'% (version), ['vmcatcher-cron.cfg', 'README.md', 'ChangeLog', 'LICENSE'])]
    data_files=[(data_files_installdir,['vmcatcher-cron.cfg','README.md','ChangeLog','LICENSE'])]
)
