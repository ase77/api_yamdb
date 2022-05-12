# Проект YaMDb
## Описание:
Проект YaMDb собирает отзывы пользователей на произведения по категориям: «Книги», «Фильмы», «Музыка». 

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram2plus.git

cd kittygram2plus
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env

source env/bin/activate

python3 -m pip install --upgrade pip
```

Установить зависимости из файла `requirements.txt`:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

После запуска проекта, документация к API будет доступна по адресу:


[http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## Примеры запросов к API:

Получение списка всех отзывов:

```
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/

[
{
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
            {
                "id": 0,
                "text": "string",
                "author": "string",
                "score": 1,
                "pub_date": "2019-08-24T14:15:22Z"
            }
        ]
    }
]

