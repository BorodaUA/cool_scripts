# Creating tickets.txt
with open('./task_6_lucky_tickets/tickets.txt', 'w') as f:
    for i in range(1, 1000000):
        i = i / 100000
        i = f"{i:.5f}".replace('.', '')
        f.write(f'{i}\n')
