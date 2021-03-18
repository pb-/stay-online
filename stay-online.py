from random import choice
from subprocess import run, DEVNULL
from time import sleep
from os import execlp

def syslog(msg):
    try:
        run(['logger', '-t', 'stay-online', msg])
    except:
        pass


def online():
    host = choice([
        'facebook.com',
        'amazon.com',
        'apple.com',
        'netflix.com',
        'google.com',
    ])

    return run([
        'timeout', '-s', 'KILL', '3', 'nc', '-z', host, '443'
    ], stdout=DEVNULL, stderr=DEVNULL).returncode == 0


def reboot():
    execlp('reboot', 'reboot')


syslog('started, waiting to settle in')
sleep(300)  # give things time to settle in and avoid a tight reboot loop
syslog('active')

while True:
    if not online():
        for i in range(3):
            syslog('probe failed (#{})'.format(i + 1))
            sleep(10)
            if online():
                syslog('recovered!')
                break
        else:
            syslog('GET TO THE CHOPPA')
            reboot()

    sleep(60)
