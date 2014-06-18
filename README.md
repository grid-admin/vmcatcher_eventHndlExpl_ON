vmcatcher_eventHndlExpl_ON
=========

CESGA VMcatcher OpenNebula event handler

Current development to adapt vmcatcher to OpenNebula

VMcatcher: https://github.com/hepix-virtualisation/vmcatcher


Requirements
------------

* VMcatcher
* Python 2.5
* qemu-img >= 1.5.0 --`qemu-img-1.7.93-1 / qemu-utils_1.7.93-1` packages can be downloaded for Scientific Linux 6 and Debian 6 OS respectively from the following link: [http://repo.cesga.es/pub/](http://repo.cesga.es/pub/)

Release notes
------------
 * It can be found more information about current release in the following ChangeLog file, [ChangeLog](http://github.com/grid-admin/vmcatcher_eventHndlExpl_ON/blob/master/ChangeLog)

vmcatcher_eventHndl_ON version 0.0.4 incorporates the following features:

 * The image is named as `dc:identifier`
 * Expired images are named as `$dc:identifier TIMESTAMP`. Example: `93084776-1176-4849-95dc-cc7a15f2ce97 2014-06-04_12-54-44_+0200-CEST`
 * Now, when there is an update for a determinted image, vmcatcher_eventHndl_ON disables previous image by configuring this image with user `oneadmin` and group `oneadmin`,
 * and change its permissions in order to only user `oneadmin` can access to it. If it is possible, it also disables this previous image. Also, it configures the new version for the image 
 * with the same user, group and permissions which had been configured for its previous image. Also, if previous image had been disabled, the new version for the image is disabled. 
 * The new opperation for vmcatcher_eventHndl_ON is the following:

1. Site admin will subscribe to an image list
2. The first image is downloaded and registered, it should not be made public. It is up to the site administrator the decision of making public the image.
3. Image lives in the cloud, VMs are launched
4. VMcatcher receives an update for a determined image
5. VMcatcher_eventHndl_ON will:

   A) Read metadata of the existing `$dc:identifier` image and **remember** owner, group, permissions and enabled/disabled status

   B) Chown & chmod the old/previous image to `oneadmin:oneadmin 700`

   C) Rename the old image to `$dc:identifier_$timestamp`

   D) Register the new image and name it as `$dc:identifier`

   E) Apply the metadata **remembered in A point**

=====

To create RPM package use:
$ python setup.py bdist_rpm --release rc${BUILD_NUMBER} --requires "vmcatcher"

For more information or any help, you can contact us in the following e-mail address: grid-admin[at]cesga[dot]es
