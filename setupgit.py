#!/usr/bin/env python

# adopted from setupgit.sh used in mongrel2

import sys
from subprocess import call


call('git config push.default tracking'.split())
call('git config branch.autosetuprebase always'.split())

if call('git flow init -d'.split()) == 0:
  print "Configuring git flow for this repository..."
else:
  print "************************************"
  print "You need gitflow installed to use it on pyjs"
  print "Please see: https://github.com/nvie/gitflow"
  sys.exit(1)
sys.exit(0)

