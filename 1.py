import time
from time import sleep
import threading



def write_words(word_count , file_name):
    with open(f'{file_name}.txt' , 'a', encoding= 'utf-8' ) as file:
        for i in range(word_count):
            word = f"Какое-то слово № {i+1} "
            file.write(word + '\n')
            i+=i
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}.txt \n')


start_time = time.time()

write_words(10, 'example1')
write_words(30, 'example2')
write_words(200, 'example3')
write_words(100, 'example4')

end_time = time.time()
el_time = (end_time - start_time)
print(el_time.__round__(3))

# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
# 10, example5.txt
# 30, example6.txt
# 200, example7.txt
# 100, example8.txt
# Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
# Также измерьте время затраченное на выполнение функций и потоков.
# Как это сделать рассказано в лекции к домашнему заданию.

thread_1 = threading.Thread(target= write_words, args= (10 , 'example5'))
thread_2 = threading.Thread(target= write_words, args= (30 , 'example6'))
thread_3 = threading.Thread(target= write_words, args= (200 , 'example7'))
thread_4 = threading.Thread(target= write_words, args= (100 , 'example8'))

start_time_THR = time.time()
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
end_time_THR = time.time()
el_time_THR = (end_time_THR - start_time_THR)
print(f'Время потоков:  {el_time_THR.__round__(4)}')