import os
import glob
import time

delay = int(input("Задержка: "))
try:
    while True:
        try:
            for x in glob.glob("*.*"):
                statinfo = os.stat(str(x))
                if statinfo.st_size != 503:
                    pass
                else:
                    os.remove(x)
                    print("Файл: " + str(x) + " успешно удалён")
            raise ValueError("Пустых файлов не найденов")
        except:
            print("Пустые файлы удалены. Повтор через", delay, "секунд.")
            time.sleep(delay)
except KeyboardInterrupt:
    print("Выполенине скрипта остановлено пользователем.")
