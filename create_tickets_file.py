# Creating tickets.txt
with open('tickets.txt', 'w') as f:
    for i in range(100000, 1000000):
        f.write(f'{i}\n')
