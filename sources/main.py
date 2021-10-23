import math
import random
import os
import time
import sys
import subprocess


def non_menu():
    os.system('clear')
    print('//______________________')
    print('//     ___       ___    ')
    print('//     |  |      |  |   ')
    print('//     |__|      |__|   ')
    print('//                      ')
    print('//       ----------     ')
    print('//______________________')
    print('')

    print('locating \'NETCAT\'..')
    time.sleep(2)
    if os.path.dirname('/usr/bin/ncat'):
        print('netcat[YES]')
        time.sleep(1.5)
    else:
        print('ERROR, NEED NETCAT TO RUN!!!')
        time.sleep(0.75)
        print('Installing..')
        time.sleep(1)
        os.system('sudo apt install ncat')

    print('locating \'PYTHON3\'..')
    time.sleep(2)
    if os.path.dirname('/usr/bin/python3'):
        print('python3[YES]')
        time.sleep(1.5)
    else:
        print('ERROR, NEED PYTHON3 TO RUN!!!')
        time.sleep(0.75)
        print('Installing..')
        time.sleep(1)
        os.system('sudo apt install python3')
    print('locating \'GNOME-TERMINAL\'..')
    time.sleep(2)
    if os.path.dirname('/usr/bin/gnome-terminal'):
        print('gnome-terminal[YES]')
        time.sleep(1.5)
    else:
        print('GNOME-TERMINAL not installed, pass[YES]')
        time.sleep(0.75)
    print('Type \'netcon\' in your terminal to execute this!')
    time.sleep(3)

    menu()

def mean_menu():
    os.system('clear')
    print('//______________________')
    print('//      \/        \/    ')
    print('//     |  |      |  |   ')
    print('//     |__|      |__|   ')
    print('//      ____________    ')
    print('//      \/\/\/\/\/\/    ')
    print('//______________________')
    print('')

    print('1 | NETCAT CHAT [ncat]')
    print('2 | NETCAT REVERSE SHELL [ncat shell]')
    print('3 | SEND FILE [ncat/file]')
    print('4 | QUIT')

    Opt = input('>> ')
    if Opt == '1':
        chat()
        mean_menu()
    elif Opt == '2':
        reverse_tcp()
        mean_menu()
    elif Opt == '3':
        file_share()
        mean_menu()
    elif Opt == '4':
        print('Exiting..')
        time.sleep(0.5)
        print('Bye!')
        time.sleep(2)
        sys.exit()
    else:
        print('Unknown Command..')
        time.sleep(1.25)
        mean_menu()

def chat():
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')

    print('1. Create Room')
    print('2. Join Room')

    Opt = input('>> ')
    if Opt == '1':
        print('Creating Command..')
        time.sleep(1.5)
        print('What port do you wan\'t to run chat on?')
        serv = input('>> ')
        print('What Username Do you Want?')
        user = input('>> ')
        os.system('clear')
        print('Running..')
        print(f'PORT NUMBER: {serv}')
        print(f'USERNAME: {user}')
        time.sleep(1)
        print('Chat Number: #')
        time.sleep(0.75)
        print('-------------------------')
        os.system(f'mawk -W interactive \'$0="{user}: "$0\' | nc -l -p {serv}')
        print('\nDone!')
        time.sleep(1.5)
    elif Opt == '2':
        print('Creating Command..')
        time.sleep(1.5)
        print('What IP is the host running on?')
        ip = input('>> ')
        print('What port is the chat on?')
        serv = input('>> ')
        print('What Username Do you Want?')
        user = input('>> ')
        os.system('clear')
        print('Running..')
        print(f'IP ADDRESS: {ip}')
        print(f'PORT NUMBER: {serv}')
        print(f'USERNAME: {user}')
        time.sleep(1)
        print('Chat Number: #')
        time.sleep(0.75)
        print('-------------------------')
        os.system(f'mawk -W interactive \'$0="{user}: "$0\' | nc {ip} {serv}')
        print('\nDone!')
        time.sleep(1.5)
    else:
        print('Unknown Command..')
        time.sleep(1.5)
        chat()

def reverse_tcp():
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')

    print('1 | Connect to shell')
    print('2 | Create Shell Server')

    Opt = input('>> ')

    if Opt == '2':
        print('Creating Command..')
        time.sleep(1.5)
        print('What port do you wan\'t to run bash on?')
        serv = input('>> ')
        print('PLEASE LEAVE USER BLANK, THANK YOU')
        user = input('>> ')
        os.system('clear')
        print('Running..')
        print(f'PORT NUMBER: {serv}')
        time.sleep(1)
        print('Chat Number: #')
        time.sleep(0.75)
        print('-------------------------')
        os.system(f'nc -e /bin/bash -l -p {serv}')
        print('\nDone!')
        time.sleep(1.5)
    elif Opt == '1':
        print('Creating Command..')
        time.sleep(1.5)
        print('What port is the shell on?')
        serv = input('>> ')
        print('What is your Username?')
        user = input('>> ')
        print('What is the IP?')
        ip = input(">> ")
        os.system('clear')
        print('Running..')
        print(f'PORT NUMBER: {serv}')
        print(f'USERNAME: {user}')
        print(f'IP ADDRESS: {ip}')
        time.sleep(1)
        print('Chat Number: #')
        time.sleep(0.75)
        print('-------------------------')
        os.system(f'nc {ip} {serv}')
        print('\nDone!')
        time.sleep(1.5)

def file_share():
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')

    print('1 | Send a File')
    print('2 | Recieve a File')
    Opt = input('>> ')

    if Opt == '1':
        print('Please link file, include directory please')
        File = input('>> ')
        time.sleep(1)
        print('What is the Port to send on?')
        serv = input('>> ')
        print(f'FILE: {File}')
        time.sleep(0.75)
        print('Running..')
        os.system(f'ncat -l -p {serv} > {File}')
        time.sleep(2)
        os.system('clear')
        print('Done!')
        time.sleep(1.7)
    elif Opt == '2':
        print('What is the port number?')
        serv = input('>> ')
        print('What is the IP?')
        ip = input('>> ')
        print('What is the File you want to Download?')
        File = input('>> ')
        os.system('clear')
        print(f'PORT NUMBER: {serv}')
        print(f'IP NUMBER: {ip}')
        print('Running..')
        time.sleep(1.5)
        os.system(f'ncat {ip} {serv} > {File}')
    else:
        print('Unknown Command..')
        time.sleep(1.75)
        file_share()


def menu():
    os.system('clear')
    print('//______________________')
    print('//     ___       ___    ')
    print('//     |  |      |  |   ')
    print('//     |__|      |__|   ')
    print('//                      ')
    print('//       ----------     ')
    print('//______________________')
    print('')

    print('1 | NETCAT CHAT [ncat]')
    print('2 | NETCAT REVERSE SHELL [ncat shell]')
    print('3 | SEND FILE [ncat/file]')
    print('4 | QUIT')

    Opt = input('>> ')
    if Opt == '1':
        chat()
        menu()
    elif Opt == '2':
        reverse_tcp()
        menu()
    elif Opt == '3':
        file_share()
        menu()
    elif Opt == '4':
        print('Exiting..')
        time.sleep(0.5)
        print('Bye!')
        time.sleep(2)
        sys.exit()
    elif Opt == 'iMean!':
        mean_menu()
    else:
        print('Unknown Command..')
        time.sleep(1.25)
        menu()

def check():
    if os.path.isfile("sources/.check"):
        menu()
    else:
        os.system('touch sources/.check')
        non_menu()
check()
