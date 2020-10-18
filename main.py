import getopt
import sys
from shell import Shell

optlist, args = getopt.getopt(sys.argv[1:], 'o:')

oapi_url = ''

for opt, arg in optlist:
    if opt in ['-o']:
        oapi_url = arg

shell = Shell()
shell.start()
