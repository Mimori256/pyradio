def add(url_path):

    print('Enter the title and url')

    title = input('Title:')
    url = input('URL: ')

    print('does this stream contain the ICY music imformation?')

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


def config():
  
    print('a - add, r - remove, b - back')
    i = input()

    if i == 'a':
        add()

    if i == 'r':
        remove()

    if i == 'b':
        pass

    else:
        print('Error')
        config()

    main()
    
