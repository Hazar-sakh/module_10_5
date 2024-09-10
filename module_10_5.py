from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(f'{name}', 'r') as file:
        line = file.readlines()
        all_data.append(line)


filenames = [f'file {number}.txt' for number in range(1, 5)]

# start = datetime.now()
# for i in filenames:
#     read_info(i)
# finish = datetime.now()
# print(finish - start)

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.now()
        pool.map(read_info, filenames)
    finish = datetime.now()
    print(finish - start)
