#!/usr/bin/env python3
#https://learn.adafruit.com/pi-thermal-printer/pi-setup-part-3
import argparse
import serial
MAX_WIDTH=35
DELIM=' '
def format_sagacious_words(str):
    '''
    ascii chars only,
    string to array of lines <= MAX_WIDTH
    ''' 
    if len(str) == 0:
        return(None)
    r=[]
    tray = ''.join([char for char in str if 32 <= ord(char) <= 126])
    #Find DELIM closest to MAX_WIDTH
    while len(tray) >= MAX_WIDTH:
        delim_pos = tray[:MAX_WIDTH].rfind(DELIM)
        #If no DELIM, use MAX_WIDTH
        if delim_pos == -1: delim_pos = MAX_WIDTH
        r.append(tray[:delim_pos+1])
        tray = tray[delim_pos+1:]
    #handle last line
    r.append(tray)
    return(r)
def print_sagacious_words(wisdom):
    if len(wisdom) == 0:
        return(None)
    for line in wisdom:
        line = line+'\n'
        ser.write(line.encode())
    #ser.write('\n'.encode()*3)
    content = b"\x1B\x64\x05\x1B\x6D"
    print(content)
    ser.write(content)
def main():
    '''
    Yea, you shouldn't have to go to this much trouble to get VS Code to recognize your virtual environment.
     The folder is right there in the directory you opened VS Code in. The VS Code team should address this if they truly want to
     support Python. It cant possibly be that hard'''
    parser = argparse.ArgumentParser(description='Print sagacious words to...')
    parser.add_argument('-p','--port',
                        type=str,
                        metavar='port',
                        help='Serial port for output. Default: ttyAMA0',
                        default='ttyUSB0')
    args = parser.parse_args()
    global ser
    ser=serial.Serial('/dev/{}'.format(args.port), 38400, timeout=5)
   
    #sagacious_words = 
    #sagacious_words = sagacious_words.strip('\n')

    while True:
        sagacious_words = input("Enter string\n")
        print_sagacious_words(format_sagacious_words(sagacious_words))
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting")
