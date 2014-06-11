#!/usr/bin/env python
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

setup(name='vmcatcher_eventHndlExpl',
    version=version,
    description="vmcatcher_eventHndl_ON manages images in fedcloud for OpenNebula",
    author="R Rosende Dopazo",
    author_email="grid-admin@cesga.es",
    url="www.cesga.es",
    scripts=['vmcatcher_eventHndl_ON'],
    data_files=[('/usr/share/doc/vmcatcher-%s/examples/'% (version), ['vmcatcher-cron.cfg', 'README.md', 'ChangeLog'])]
)
