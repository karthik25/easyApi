import getopt
import sys
from tasks.setter import Setter
from shell import Shell
from helptext import Helptext


optlist, args = getopt.getopt(sys.argv[1:], 'sho:')

oapi_url = ''
ssl_disable = False
help_only = False

for opt, arg in optlist:
    if opt in ['-o']:
        oapi_url = arg
    if opt in ['-s']:
        ssl_disable = True
    if opt in ['-h']:
        help_only = True

if oapi_url == "" or help_only:
    Helptext.print_help_text()
else:
    Setter.set_key_value("oapi_url", oapi_url)
    Setter.set_key_value("disable_ssl", ssl_disable)
    shell = Shell()
    shell.start()
