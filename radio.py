import os
import sys
import time

HOME = os.environ['HOME']
url_path = HOME + '.url'

base_path = __file__.replace('radio.py', '')
get_name_path = base_path + 'get_name.out'

if get_name_path == 'get_name.out':
    get_name_path = './' + get_name_path


def clear():
    os.system('clear')


def config_option():
  
    print('a - add, r - remove, b - back')
    s = ('a', 'r', 'b')

    while True:
        i = input()

        if not i in s:
            print ('Error')
            continue

        else:
            return i


def get_radio_list(path):

    title_list = []
    url_list = []
    icy_list = []

    try:
        f = open(path, 'r')
        

    #URL file doesn't exist
    except FileNotFoundError:

        print('Creating .url on your home directory...')

        f = open(path, 'w')
        #Create a url file on the home derectory
        f.write('SmoothJazz.com.pl,http://stream14.shoutcastsolutions.com:8057/256stream,y')
        f.close()

        f = open(path, 'r')


    for line in f.readlines():
        splited_list = line.split(',')

        title_list.append(splited_list[0])
        url_list.append(splited_list[1])
        icy_list.append(splited_list[2].replace('\n',''))

    f.close()

    return (title_list,url_list,icy_list)


def generate_command(url,exist_contents):

    if exist_contents == 'y':
        option = '| ' + get_name_path

    else:
        option = ' >> /dev/null'

    return 'mplayer {} {}'.format(url,option)


def main():

    clear()
    print('PyRadio', end='\n\n')

    title_list, url_list, icy_list = get_radio_list(url_path)
    #All three lists have the same length
    length = len(title_list)

    if length == 0:
        sys.exit('No stream found!')
        
    for i in range(length):

        if i+1 < 10:
            space = ' '

        else:
            #No space
            space = ''

        url_list[i] = url_list[i].replace('\n','')
        print('{} {} {} '.format(space, i+1, title_list[i]))

    print('')
    print('Type the number of a radio station you want to listen')
    print('c - config the url file,  q - quit')
    
    try:
        #select number 
        select = input()
        select = int(select) -1
        
        if select < 0 or select >= len(title_list):
            print('Index Error')
            time.sleep(1)
            main()

    except ValueError:
    
       if select == 'c':

           sys.path.append(base_path)
           import config_module as config

           selection = config_option()

           if selection == 'a':
               config.add()

           elif selection == 'r':
               config.remove(length)

           elif selection == 'b':
               pass

           main()


       elif select == 'q':
           sys.exit('bye')

       else:
           print('Error')
           time.sleep(1)
           main()

    #execute command to play music
    clear()
    print('Loading {}...'.format(title_list[select]))

    command = generate_command(url_list[select],icy_list[select],)
    print('Type Ctrl+C to stop the program')
    os.system(command)

    clear()
    print('Continue?')

    select=input('type y/n: ')

    if select=='y':
        main()

    else:
        sys.exit('bye')

main()
