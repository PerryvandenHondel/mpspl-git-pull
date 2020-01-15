#!/usr/bin/python3

#
# mpspl-git-pull.py
#
# Marketplace GIT Pull script
#
# Flow:
#       Main()
#           ScriptInit()
#               MakeSessionID()
#           ScriptRun()
#           ScriptDone()
#           


#
# Import all modules
#
import configparser
import getopt
import logging
import os
import secrets
import sys


#
# Global variables
#
pathConfig = './mpspl-git-pull.conf'
sessionID = ''
useEnvironmentConfigType = ''
usePath = ''


def MakeSessionID():
    #
    # Make a Session ID in the format of 16 chars long.
    # Source: https://stackoverflow.com/questions/817882/unique-session-id-in-python
    #
    return secrets.token_urlsafe(16)


def ScriptInit():
    print('ScriptInit()')
    nonlocal useEnvironmentConfigType

    sessionID = MakeSessionID()

    print('Generated token: {}'.format(sessionID))

    config = configparser.ConfigParser()
    config.read('mpspl-git-pull.conf')

    print('useEnvironmentConfigType=', useEnvironmentConfigType)
    usePath = config['gen-shcluster']['Path']
    print('Path for {}: {}'.format(useEnvironmentConfigType, usePath))
    

def ScriptRun():
    print('ScriptRun()')
    print('')


def ScriptDone():
    print('ScriptDone()')
    # Everthing OK at the end
    sys.exit(0)


def ScriptUsage():
    print('Usage: {} -s <environment-configurationtype>'. format(sys.argv[0]))
    print()
    print('\t<environment-configurationtype>\tContains the environment with the configuration type.')
    print()
    print('Script stopped')
    sys.exit(2)


def main(argv):
    print("hello mpspl-git-pull from main()")

    try:
        opts, args = getopt.getopt(argv, "he:")
    except getopt.GetOptError:
        ScriptUsage()

    for opt, arg in opts:
        if opt == '-h':
            ScriptUsage()
        elif opt in ("-e"):
            useEnvironmentConfigType = arg
            print('useEnvironmentConfigType=', useEnvironmentConfigType)

    ScriptInit()
    #ScriptRun()
   # ScriptDone()


if __name__ == "__main__":
    main(sys.argv[1:])
