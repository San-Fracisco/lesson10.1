from time import sleep
from datetime import datetime
from threading import Thread

time_start = datetime.now()

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i} \n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

threads = []
for word_count, file_name in [(10, "example1.txt"), (30, "example2.txt"), (200, "example3.txt"), (100, "example4.txt")]:
    thread = Thread(target=write_words, args=(word_count, file_name))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

time_and = datetime.now()
time_result = time_and - time_start
print(f'Работа потоков {time_result}')

time_start = datetime.now()

threads = [Thread(target=write_words, args=(10, "example5.txt")),
          Thread(target=write_words, args=(30, "example6.txt")),
          Thread(target=write_words, args=(200, "example7.txt")),
          Thread(target=write_words, args=(100, "example8.txt"))]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

time_and = datetime.now()
time_result = time_and - time_start
print(f'Работа потоков {time_result}')


