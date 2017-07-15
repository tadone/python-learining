import time
import sys
import datetime
import getopt
import webbrowser
import subprocess
import random

def usage():
    print('Usage -h --hour and -m --minute')

now = datetime.datetime.now()
urls = open('urls.txt', 'r')


time_disp = str(now.hour) + ':' + str(now.minute)

print('The time now is: {}'.format(now))

#print("This is the name of the script: " + sys.argv[0])
#print("Number of arguments: " + str(len(sys.argv)))
#print("The arguments are: " + str(sys.argv))
#print(str(sys.argv[1:]))

# Read command line args
try:
    opts, args = getopt.getopt(sys.argv[1:], 'h:m:t', ['hour=', 'minute=', 'help'])
except getopt.GetoptError:
    usage()
    print('Error')
    sys.exit(2)

for opt, arg in opts:
    if opt in ('-t', '--help'):
        usage()
        sys.exit(2)
    elif opt in ('-h', '--hour'):
        _hour = int(arg)
    elif opt in ('-m', '--minute'):
        _minute = int(arg)
    else:
        usage()
        sys.exit(2)

run_at = now + datetime.timedelta(minutes=1)
alarm_time = datetime.datetime(year=now.year, month=now.month, day=now.day, hour=_hour, minute=_minute)
print('Alarm set for {}'.format(alarm_time))
#webbrowser.open_new_tab(url='google.com')
#subprocess.Popen(['open', 'alarm.wav'])
while datetime.datetime.now() < alarm_time:
    time.sleep(2)
    print('sleeping for 2 sec')
    print(datetime.datetime.now())

# OSX Calculator
#subprocess.Popen(['open', '/Applications/Calculator.app/'])
print(urls.readlines)
urls.close
