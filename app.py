# Модуль ОС для получения данных о файлах
import os
# Модуль для текущего времени
from datetime import datetime
# МОдуль для вывода имени из командной строки
import getpass

# Вывводим приветствие с именем пользователя и текущую дату:
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print (f"Hello, {getpass.getuser()}!\nCurrent time: {current_datetime}")

# Рекурсивный подсчет количества файлов в папках и внутри подпапок
import os
path = input('Введите папку: ')  #   пользователь вводит путь в консоли
if path !='':
    count = 0
    for root,dirs, files in os.walk(path) :  
        count += len(files)       
    print('количество файлов в указанном пути:', count)
    size_of_file  = os.stat(path).st_size  
else:
    count = 0
    for root,dirs, files in os.walk('/mnt/c') :  # mnt/c в WSL2 это аналог пути корневой папки это C:\ с т.з.Windows 
        count += len(files)       
    print('количество файлов по умолчанию — в корневом каталоге:', count)


# Сортировка посчитанных файлов от бельшего к меньшему и вывод первых 10:

print('Топ-10 файлов по размеру в указанном пути:')

list_of_files = filter( lambda x: os.path.isfile 
                       (os.path.join(path, x)), 
                        os.listdir(path) ) 
  
# Sort list of file names by size  
list_of_files = sorted( list_of_files,
                        
                        key =  lambda x: -os.stat
                       (os.path.join(path, x)).st_size)[:10] 
# Iterate over sorted list of file  
# names and print them along with size one by one  
for name_of_file in list_of_files: 
    path_of_file = os.path.join(path, name_of_file) 
    size_of_file  = os.stat(path_of_file).st_size  
    print( path, name_of_file, ' : ', size_of_file, 'КБ')


#/mnt/c/Users/59o/Documents/ДО
# wsl.localhost\Ubuntu-24.04\home\olga\Documents\ДО
# python app.py