with open('./task_4_file_parser/big_data.txt', 'w+') as f:
    for i in range(100000):
        f.write(f'This is line {i} Cat and Dog \n')
