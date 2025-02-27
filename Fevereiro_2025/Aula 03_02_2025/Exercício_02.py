rede_base = '198.168.0.1'

print('A rede é:', rede_base)
print('\nA lista de IPs é :')

for sequencia in range(1, 11): 
    ip = f'198.168.0.{sequencia}'
    print(ip)