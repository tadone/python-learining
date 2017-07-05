import time
import sys
import datetime

def usage():
    print('Usage -h --hour and -m --minute')

now = datetime.datetime.now()
hour = ''
minute = ''

print(str(now.hour) + ':' + str(now.minute))
print("This is the name of the script: " + sys.argv[0])
print("Number of arguments: " + str(len(sys.argv)))
print("The arguments are: " + str(sys.argv))
print(str(sys.argv[1:]))

# Read command line args
opts, args = getopt.getopt(sys.argv[1:], 'h:m:h', ['hour=', 'minute=', 'help'])

for opt, arg in opts:
    if opt in ('-h', '--help'):
        usage()
        sys.exit(2)
    elif opt in ('-h', '--hour'):
        miner_name = arg
    elif opt in ('-m', '--minute'):
        params = arg
    else:
        usage()
        sys.exit(2)
