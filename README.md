vmcatcher_eventHndlExpl_ON
=========

CESGA VMcatcher OpenNebula event handler

Actually development to adapt vmcatcher to OpenNebula

VMcatcher: https://github.com/hepix-virtualisation/vmcatcher


Requirements
------------

* VMcatcher
* Python 2.5
* qemu-img >= 1.5.0

=====

To create RPM package use:
$ python setup.py bdist_rpm --release rc${BUILD_NUMBER} --requires "vmcatcher"


For more info or any help contact in: grid-admin[at]cesga[dot]es
