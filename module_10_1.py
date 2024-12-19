import time
import threading

def write_words(word_count, file_name):
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(word_count + 1):
        file.write('Какое-то слово: ')
        file.write(str(i))
        file.write('\n')
        time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_func = time.time() # Фиксация времени начала для выполнения ф-ций по очереди
file_1 = write_words(10, 'example1.txt')
file_2 = write_words(30, 'example2.txt')
file_3 = write_words(200, 'example3.txt')
file_4 = write_words(100, 'example4.txt')
stop_func = time.time()
print(f'Работа потоков {stop_func - start_func}')

start_thread = time.time() # Фиксация времени начала для выполнения 4 потоков одновременно
file_5 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
file_6 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
file_7 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
file_8 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
file_5.start()
file_6.start()
file_7.start()
file_8.start()
file_5.join()
file_6.join()
file_7.join()
file_8.join()
stop_thread = time.time()
print(f'Работа потоков {stop_thread - start_thread}')
