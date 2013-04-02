from vmcatcher.__version__ import version
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
            
setup(name='vmcatcher_eventHndlExpl_ON',
    version=version,
    description="vmcatcher_eventHndlExpl_ON manages images in fedcloud",
    author="R Rosende Dopazo",
    author_email="rrosende@cesga.es",
    url="www.cesga.es",
    
    data_files=[('/usr/share/doc/vmcatcher-%s' % (version), ['vmcatcher_eventHndlExpl_ON']),
		('/usr/share/doc/vmcatcher-%s/examples/'% (version), ['vmcatcher-cron.cfg'])]
)