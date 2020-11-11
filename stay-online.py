from random import choice
from subprocess import run, DEVNULL
from time import sleep
from os import execlp

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


sleep(300)  # give things time to settle in and avoid a tight reboot loop

while True:
    if not online():
        for _ in range(3):
            sleep(10)
            if online():
                break
        else:
            reboot()

    sleep(60)
