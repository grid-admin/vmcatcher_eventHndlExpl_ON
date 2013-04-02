FEDCLOUD DEMO FOR EGI TECHNICAL FORUM

For run this script you must install:

python
StratusLab client tools The instructions for this are on the webpage https://wiki.egi.eu/wiki/Fedcloud-tf:WorkGroups:VM_Marketplace#Register_an_image_with_the_EGI.eu_Marketplace. They point to the tar.gz, but there are also RPMs available in the yum repositories, see http://yum.stratuslab.eu/
Before run it you must configure certpath and capath variables in script

certpath="~/.globus"
capath="/etc/grid-security/certificates"
Usage:

$python fedcloud.py http://marketplace.egi.eu
$./fedcloud.py http://marketplace.egi.eu
For debug purposes:

$python fedcloud.py http://marketplace.egi.eu --debug
$./fedcloud.py http://marketplace.egi.eu --debug
For untrusted hosts certificates:

$python fedcloud.py http://marketplace.egi.eu --insecure=
$./fedcloud.py http://marketplace.egi.eu --insecure=
Example: python fedcloud.py http://marketplace.egi.eu --insecure=kth.se,cesga --debug
