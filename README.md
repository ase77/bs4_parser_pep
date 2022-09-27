# Парсер Python
## Описание:
### whats-new:
-Собирает важные изменения между основными версиями Python
-Соберает ссылки на статьи о нововведениях
-Достаёт из статей справочную информацию (имя автора или редактора статьи)
-Сохраняет результат в табличном виде в csv-файл или выводит в терминал
### latest-versions:
-Собирает информацию о версиях Python
-Находит номера, статусы и ссылки на документацию
-Сохраняет результат в табличном виде в csv-файл или выводит в терминал
### download:
-Скачивает архив с документацией на актуальную версию Python
### pep:
-Собирает данные обо всех документах PEP
-Сравнивает статус на странице PEP со статусом в общем списке
-Считает количество PEP в каждом статусе и общее количество PEP
-Сохраняет результат в табличном виде в csv-файл или выводит в терминал

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:ase77/bs4_parser_pep.git

cd bs4_parser_pep/src
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv

source venv/bin/activate

python3 -m pip install --upgrade pip
```

Установить зависимости из файла `requirements.txt`:

```
pip install -r requirements.txt
```

## Аргументы командной строки:
```
positional arguments:
  {whats-new,latest-versions,download,pep}
                        Режимы работы парсера

optional arguments:
  -h, --help            show this help message and exit
  -c, --clear-cache     Очистка кеша
  -o {pretty,file}, --output {pretty,file}
                        Дополнительные способы вывода данных
```
