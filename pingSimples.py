import os

ip_ou_host = input("Digite o IP ou HOST a ser verificado: ")

os.system('ping -c 6 {}'.format(ip_ou_host))