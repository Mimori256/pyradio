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

    name_option = ''

    if exist_contents == 'y':
        name_option = get_name_path

    return 'mplayer.exe {} | {}'.format(url,name_option)


def main():

    clear()
    print('PyRadio', end='\n\n')

    title_list, url_list, icy_list = \
                                                   get_radio_list(url_path)
        
    for i in range(len(title_list)):

        if i+1 < 10:
            space = ' '

        else:
            #No space
            space = ''

        url_list[i] = url_list[i].replace('\n','')
        print('{} {} {} '.format(space, i+1, title_list[i]))

    print('')
    print('Type the number of a station')
    print('config - config the url file,  q - quit')
    
    try:
        #select number 
        select = input()
        select = int(select) -1
        
        if select < 0 or select >= len(title_list):
            print('Index Error')
            time.sleep(1)
            main()

    except ValueError:
    
       if select == 'config':

           sys.path.append(base_path)
           import config_module as config

           config.config(url_path)
           main()

       elif select == 'q':
           sys.exit()

       else:
           print('Error')
           time.sleep(1)
           main()

    #execute command to play music
    clear()
    print('Loading {}...'.format(title_list[select]))

    command = generate_command(url_list[select],icy_list[select],)
    os.system(command)

    print('Continue y/n')

    select=input()

    if select=='y':
        main()

    else:
        print('bye')
        sys.exit()


if __name__ == '__main__':
    main()
