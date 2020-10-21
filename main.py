import getopt
import sys
from tasks.setter import Setter
from shell import Shell

optlist, args = getopt.getopt(sys.argv[1:], 'so:')

oapi_url = ''
ssl_disable = False

for opt, arg in optlist:
    if opt in ['-o']:
        oapi_url = arg
    if opt in ['-s']:
        ssl_disable = True

if oapi_url == "":
    print("Open API url is required")
else:
    Setter.set_key_value("oapi_url", oapi_url)
    Setter.set_key_value("disable_ssl", ssl_disable)
    shell = Shell()
    shell.start()
