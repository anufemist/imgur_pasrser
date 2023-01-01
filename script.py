import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import string
import random
import urllib
 

files = int(input("Потоков: "))



def download_file(url, destination):
    try:
        start_time = time.time()
        urllib.request.urlretrieve(url, destination)
        r = requests.get(url)
        result = destination + ' ' + str(r.status_code) + " | Время: " + str((time.time() - start_time)) 
        return result
    except requests.exceptions.RequestException as e:
        return e

def runner(name_list):
    threads= []
    with ThreadPoolExecutor(max_workers=(files * 3)) as executor:
        for name in name_list:
            url = " https://i.imgur.com/" + name
            threads.append(executor.submit(download_file, url, name))
            
        for task in as_completed(threads):
            print(task.result()) 


letters_and_digits = string.ascii_letters + string.digits

try:
    while True:
        name_list = []
        for i in range(0, files):
            rand_string1 = ''.join(random.sample(letters_and_digits, 5))
            rand_string2 = ''.join(random.sample(letters_and_digits, 5))
            rand_string3 = ''.join(random.sample(letters_and_digits, 5))

            rand_string1 += ".jpg"
            rand_string2 += ".png"
            rand_string3 += ".gif"

            name_list.append(rand_string1)
            name_list.append(rand_string2)
            name_list.append(rand_string3)
        runner(name_list)
except KeyboardInterrupt:
    print("Выполенине скрипта остановлено пользователем.")