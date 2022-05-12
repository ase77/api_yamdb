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
## Reviews:

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
```

Полуение отзыва по id:

```
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/

{
    "id": 0,
    "text": "string",
    "author": "string",
    "score": 1,
    "pub_date": "2019-08-24T14:15:22Z"
}
```

Добавить новый отзыв. Пользователь может оставить только один отзыв на произведение:

```
POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/

{
    "text": "string",
    "score": 1
}
```

Частичное обновление отзыва по id:

```
PATCH http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/

{
    "text": "string",
    "score": 1
}
```

Удаление отзыва по id:

```
DELETE http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/

```

## Comments:

Получение списка всех комментариев к отзыву:

```
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/

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
                "pub_date": "2019-08-24T14:15:22Z"
            }
        ]
    }
]
```

Получение комментария к отзыву по id:

```
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/

{
    "id": 0,
    "text": "string",
    "author": "string",
    "pub_date": "2019-08-24T14:15:22Z"
}
```

Добавление комментария к отзыву:

```
POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/

{
    "text": "string"
}
```

Частичное обновление комментария к отзыву по id:

```
PATCH http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/

{
    "text": "string"
}
```

Удаление комментария к отзыву по id:

```
DELETE http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/

```
