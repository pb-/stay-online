# stay-online.py

Makes sure your Raspberry Pi stays online. WiFi stacks can be a bit funny sometimes, so it's good to invoke an old German proverb,

> Alles gut macht der Reboot.

This program tests for a usable internet connection, defined as _being able to establish a TCP connection with FAANG_, and reboots the machine if that repeatedly fails.


## Installation

Requires Python 3.

Move `stay-online.py` to `/home/pi/stay-online.py` and install the service unit with:

```
sudo cp stay-online.service /etc/systemd/system
sudo systemctl enable stay-online
```
