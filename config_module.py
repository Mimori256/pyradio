import os

HOME = os.environ['HOME']
url_path = HOME + '.url'


def add():

    print('Enter the title and url')

    title = input('Title:')
    url = input('URL: ')

    print('does the stream contain the ICY music imformation?')

    while(1):

        select = input('y/n ')       

        if select == 'y' or select =='n':
            break

        else:
            print('Error')
        
    with open(url_path,'a') as f:
        f.write('{},{},{}\n'.format(title,url,select))

    stations_list = []

    with open(url_path,'r') as f:

        for line in f.readlines():
            stations_list.append(line)

    #sort radio stations by name (alphabet order)
    stations_list.sort()

    with open(url_path,'w') as f:
    
        for station in stations_list:
            f.write(station)

    print('complete')


def remove(length):

    while True:

        i = int(input('Select the index of the stream you want to delete'))

        if i > 0 and i < length:
            break

        else:
            print('Error')
            continue

    with open(url_path, 'r') as f:

        stream_list = ['0']

        for s in f.readlines():
            stream_list.append(s)

    stream_list.pop(i)
    stream_list.pop(0)

    with open(url_path, 'w') as f:

        for s in stream_list:
            f.write(s)

    print('Complete')

    return 0
