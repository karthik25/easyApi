import getopt
import sys
import os
from tasks.setter import Setter
from shell import Shell
from helptext import Helptext
from utils.stringutils import Stringutils


optlist, args = getopt.getopt(sys.argv[1:], 'shc:o:')

oapi_url = ''
config_file = ''
ssl_disable = False
help_only = False

for opt, arg in optlist:
    if opt in ['-o']:
        oapi_url = arg
    if opt in ['-c']:
        config_file = arg
    if opt in ['-s']:
        ssl_disable = True
    if opt in ['-h']:
        help_only = True

if config_file != '' and not os.path.isfile(config_file):
    print("easyApi Shell: config file passed is not valid, use the 'set' command to set the required settings")

if oapi_url == "" or help_only:
    Helptext.print_help_text()
else:
    Setter.set_key_value("oapi_url", oapi_url)
    Setter.set_key_value("disable_ssl", ssl_disable)

    if config_file != '' and os.path.isfile(config_file):
        config_dict = Stringutils.config_file_to_dict(config_file)
        Setter.set_multiple_keys(config_dict)

    shell = Shell()
    shell.start()
