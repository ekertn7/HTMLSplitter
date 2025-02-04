# Скрипт для разделения HTML на фрагменты определенной длины

[Условие задачи](/statement.pdf)

## Структура проекта

```
.
├── README.md
├── app
│   ├── argument_parser
│   │   └── argument_parser.py  # парсер аргументов командной строки
│   ├── exceptions
│   │   └── exceptions.py       # исключения
│   └── html_splitter
│       └── html_splitter.py    # скрипт
├── config.py                   # конфиг файл
├── pyproject.toml              # poetry requirements
├── pytest.ini                  # конфиг для pytest
├── split_msg.py                # точка входа
└── tests
    └── test_split_message.py
```

## Скачивание

```
git clone git@github.com:ekertn7/TestTaskMadDevs.git
cd TestTaskMadDevs
```

## Установка и запуск скрипта через poetry

```
poetry install --with dev
poetry run python split_msg.py --max-len=1024 source.html
```

Бонус: можно запустить с помощью шебанга:

```
echo "#\!$(poetry env info --path)/bin/python\n$(cat split_msg.py)" > split_msg.py
./split_msg.py --max-len=1024 source.html
```

## Запуск тестов через poetry

```
poetry run pytest -v
```
