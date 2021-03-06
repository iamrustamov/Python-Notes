# if __ name__ == "__ main__"

Когда интерпретатор Python читает исходный файл, он исполняет весь найденный в нем код. Перед тем, как начать выполнять команды, он определяет несколько специальных переменных. Например, если интерпретатор запускает некоторый модуль (исходный файл) как основную программу, он присваивает специальной переменной __ **name**__ значение "__ **main__**". Если этот файл импортируется из другого модуля, переменной __ **name**__ будет присвоено имя этого модуля.

В случае с вашим сценарием, предположим, что код исполняется как основная функция, например:

```bash
python threading_example.py
```

После задания специальный переменных интерпретатор выполнит инструкцию **import** и загрузит указанные модули. Затем он проанализирует блок **def**, создаст объект-функцию и переменную под названием **myfunction**, которая будет указывать на этот объект.

Затем он прочтет инструкцию **if**, «поймёт», что **__ name__** эквивалентен **"__ main__"**, и выполнит указанный блок.

Одна из причин делать именно так – тот факт, что иногда вы пишете модуль (файл с расширением **.py**), предназначенный для непосредственного исполнения. Кроме того, он также может быть импортирован и использован из другого модуля. Производя подобную проверку, вы можете сделать так, что код будет исполняться только при условии, что данный модуль запущен как программа, и запретить исполнять его, если его хотят импортировать и использовать функции модуля отдельно.

Дополнительно см. [эту страницу](http://ibiblio.org/g2swap/byteofpython/read/module-name.html).

### Что означает "threading_example в данный момент импортируется из другого модуля"?

Это означает, что кем-то в каком-либо файле **.py** (или в ходе интерактивной Python-сессии) используется выражение **import threading_example**. Противоположный этому случай – пользователь использует выражение **python threading_example.py** или **./threading_example.py**, и т. д.. В последнем случае, **threading_example.py** запущен как основная программа. В первом же случае он запущен как-то иначе (чтобы понять, ищите вызов вида **import threading_example**).

Полезные источники US: [What does if **__ name__** == “**__ main__**”: do?](https://stackoverflow.com/questions/419163/what-does-if-name-main-do/419185#419185)
