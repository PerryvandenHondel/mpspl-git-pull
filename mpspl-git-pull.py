#!/usr/bin/python3

'''

mpspl-git-pull.py

Marketplace GIT Pull script

Flow:
    Main()
        MakesessionId()
        ProcessEnvironmentConfig()

'''


'''
Import used modules
'''
import configparser
import getopt
import logging
import os
import secrets # Used in secrets.token_urlsafe(16)
import sys


'''
Global variables
'''

sessionId = ''


def MakeSessionId():
    '''
    
    Make a Session ID in the format of 16 chars long.
    
    Source: https://stackoverflow.com/questions/817882/unique-session-id-in-python
    
    '''
    return secrets.token_urlsafe(16)

    
def ProcessEnvironmentConfig(useEnvironmentConfig):
    '''

    Process the selected Environment Config set
    
    useEnvironmentConfig: Name of the Environment Config, example: gen-shcluster 
    
    '''
    logging.debug('session={} function=ProcessEnvironmentConfig()'.format(sessionId))
    
    currentDir = os.getcwd()
    print('Current working directory is {}'.format(currentDir))
    
    # Read the path to use from the config file.
    useDirectory = config[useEnvironmentConfig]['Directory']
    print('Directory for {} is {}'.format(useEnvironmentConfig, useDirectory))
    logging.debug('session={} currentdir={}'.format(sessionId, currentDir))

    logging.debug('session={} changetodir={}'.format(sessionId, useDirectory))
    print('Change to directory: {}'. format(useDirectory))
    os.chdir(useDirectory)

    # Run the GIT pull command to get all the latest updates.
    resultCode = os.system('git pull')
    if resultCode == 0:
        print('Success, result code: {}'.format(resultCode))
        logging.info('session={} command="git pull" resultcode={}'.format(sessionId, resultCode))

        # Apply the next action after the git pull was successful
        useAction = config[useEnvironmentConfig]['Action']
        print('Run action now {}'.format(useAction))
        resultCode = os.system(useAction)
        if resultCode == 0:
            logging.info('session={} command="run command line {} succes" resultcode={}'.format(sessionId, useAction, resultCode))
            print('Success running {}'.format(useAction))
        else:
            logging.error('session={} command="run command line {} failed" resultcode={}'.format(sessionId, useAction, resultCode))
            print('Failed tun command line {}'.format(useAction))
    else:
        print('Error, result code: {}'.format(resultCode))
        logging.error('session={} command="git pull" resultcode={}'.format(sessionId, resultCode))

    

def ScriptUsage():
    '''

    Show the usage of the program.

    '''
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

    # Generate a unique session ID, make it global across the script.
    global sessionId
    sessionId = MakeSessionId()

    global config
    config = configparser.ConfigParser()
    pathConfig = './mpspl-git-pull.conf'
    config.read(pathConfig)

    pathLog = config['Config']['PathLog']
    print('Path for log file is {}'.format(pathLog))

    logLevel = logging.DEBUG
    logging.basicConfig(level=logLevel, filename=pathLog, format='%(asctime)s level=%(levelname)s %(message)s')

    logging.info('session=%s action=Start', sessionId)
    logging.info('session=%s environmentconfig=%s', sessionId, useEnvironmentConfig)    

    ProcessEnvironmentConfig(useEnvironmentConfig)
       
    logging.info('session=%s action=End', sessionId)
    logging.shutdown() # Last line of main()
 

if __name__ == "__main__":
    main(sys.argv[1:])
