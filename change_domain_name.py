#!/usr/bin/env python3

import subprocess

domain_name = input("write the domain name (e.g schoolname.pef.local): ")

subprocess.call(["echo", domain_name, "> /etc/hostname"])
subprocess.call(["reboot"])
