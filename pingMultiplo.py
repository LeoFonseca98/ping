import os

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print()
        print('Verificando o ip: ', ip)
        os.system('ping  -c 4 {}'.format(ip))

