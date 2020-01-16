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
#useEnvironmentConfigType = ''
usePath = ''


def MakeSessionID():
    '''
    Make a Session ID in the format of 16 chars long.
    Source: https://stackoverflow.com/questions/817882/unique-session-id-in-python
    '''
    return secrets.token_urlsafe(16)


def ScriptInit():
    print('ScriptInit()')
    #useEnvironmentConfigType


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
    print()
    print('Usage: {} -e <environment-configurationset>'. format(sys.argv[0]))
    print()
    print('\t<environment-configuration>\tContains the environment with the configuration set in format: environment-configuration.')
    print()
    print('Script stopped')
    sys.exit(2)


def main(argv):
    '''
    Main script module
    '''
    useEnvironmentConfig = ''

    # When there are no command line options parsed; show Usage and quit.
    if len(argv) == 0:
        ScriptUsage()

    try:
       opts, args = getopt.getopt(argv, "he:", ["help", "envconfig="])
    except getopt.GetoptError as err:
        print(err)
        ScriptUsage()

    for o, a in opts:
        if o == "-e":
            useEnvironmentConfig = a
        elif o in ("-h", "--help"):
            ScriptUsage()
        else:
            assert False, "Unhandled option"

            
    print('useEnvironmentConfig =', useEnvironmentConfig)

    sessionID = MakeSessionID()
    print('SessionID = ', sessionID)

    config = configparser.ConfigParser()
    config.read('mpspl-git-pull.conf')

    pathLog = config['Config']['PathLog']
    print('Path for log file is {}'.format(pathLog))

    logLevel = logging.DEBUG
    logging.basicConfig(level=logLevel, filename=pathLog, format='%(asctime)s level=%(levelname)s %(message)s')
    logging.info('session=%s action=Start', sessionID)
    logging.info('sessing=%s environmentconfig=%s', sessionID, useEnvironmentConfig)    


    logging.info('session=%s action=End', sessionID)

 
if __name__ == "__main__":
    main(sys.argv[1:])
