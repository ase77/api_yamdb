<a id="anchor"></a>
# Проект YaMDb

Командный проект.
Возглавлял команду разработчиков и отвечал за модели, view и эндпойнты для:
  * произведений,
  * категорий,
  * жанров;
  * реализовал импорт данных из csv файлов.

## Описание:

Проект YaMDb собирает отзывы пользователей на произведения по категориям: «Книги», «Фильмы», «Музыка».
Произведению может быть присвоен жанр из списка предустановленных.
Пользователи оставляют к произведениям отзывы, оставляют комментарии к отзывам и ставят произведению оценку, из пользовательских оценок формируется рейтинг.

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

Загрузить данные из файлов `csv` в базу данных:

```
python3 manage.py load_csv
```

Запустить проект:

```
python3 manage.py runserver
```

После запуска проекта, документация к API будет доступна по адресу:


[http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## Примеры запросов к API:
## Auth:

Регистрация нового пользователя, получение кода подтверждения на переданный `email`:

`POST http://127.0.0.1:8000/api/v1/auth/signup/`
```
{
    "email": "string",
    "username": "string"
}
```

Получение JWT-токена в обмен на `username` и `confirmation_code`:

`POST http://127.0.0.1:8000/api/v1/auth/token/`
```
{
    "username": "string",
    "confirmation_code": "string"
}
```

## Categories:

Получение списка всех категорий:

`GET http://127.0.0.1:8000/api/v1/categories/`
```
[
    {
        "count": 0,
        "next": "string",
        "previous": "string",
        "results": [
            {
                "name": "string",
                "slug": "string"
            }
        ]
    }
]
```

Добавление новой категории. Поле `slug` каждой категории должно быть уникальным:

`POST http://127.0.0.1:8000/api/v1/categories/`
```
{
    "name": "string",
    "slug": "string"
}
```

Удаление категории:

`DELETE http://127.0.0.1:8000/api/v1/categories/{slug}/`

## Genres:

Получение списка всех жанров:

`GET http://127.0.0.1:8000/api/v1/genres/`
```
[
    {
        "count": 0,
        "next": "string",
        "previous": "string",
        "results": [
            {
                "name": "string",
                "slug": "string"
            }
        ]
    }
]
```

Добавление жанра. Поле `slug` каждого жанра должно быть уникальным:

`POST http://127.0.0.1:8000/api/v1/genres/`
```
{
    "name": "string",
    "slug": "string"
}
```

Удаление жанра:

`DELETE http://127.0.0.1:8000/api/v1/genres/{slug}/`

## Titles:

Получение списка всех произведений:

`GET http://127.0.0.1:8000/api/v1/titles/`
```
[
    {
        "count": 0,
        "next": "string",
        "previous": "string",
        "results": [
            {
                "id": 0,
                "name": "string",
                "year": 0,
                "rating": 0,
                "description": "string",
                "genre": [
                    {
                        "name": "string",
                        "slug": "string"
                    }
                ],
                "category": {
                    "name": "string",
                    "slug": "string"
                }
            }
        ]
    }
]
```

Получение информации о произведении:

`GET http://127.0.0.1:8000/api/v1/titles/{titles_id}/`
```
{
    "id": 0,
    "name": "string",
    "year": 0,
    "rating": 0,
    "description": "string",
    "genre": [
        {
            "name": "string",
            "slug": "string"
        }
    ],
    "category": {
        "name": "string",
        "slug": "string"
    }
}
```

Добавление произведения (требуется указать уже существующие категорию и жанр):

`POST http://127.0.0.1:8000/api/v1/titles/`
```
{
    "name": "string",
    "year": 0,
    "description": "string",
    "genre": [
        "string"
    ],
    "category": "string"
}
```

Частичное обновление информации о произведении:

`PATCH http://127.0.0.1:8000/api/v1/titles/{titles_id}/`
```
{
    "name": "string",
    "year": 0,
    "description": "string",
    "genre": [
        "string"
    ],
    "category": "string"
}
```

Удаление произведения:

`DELETE http://127.0.0.1:8000/api/v1/titles/{titles_id}/`

## Reviews:

Получение списка всех отзывов:

`GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/`
```
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

`GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/`
```
{
    "id": 0,
    "text": "string",
    "author": "string",
    "score": 1,
    "pub_date": "2019-08-24T14:15:22Z"
}
```

Добавить новый отзыв. Пользователь может оставить только один отзыв на произведение:

`POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/`
```
{
    "text": "string",
    "score": 1
}
```

Частичное обновление отзыва по id:

`PATCH http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/`
```
{
    "text": "string",
    "score": 1
}
```

Удаление отзыва по id:

`DELETE http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/`

## Comments:

Получение списка всех комментариев к отзыву:

`GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/`
```
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

`GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/`
```
{
    "id": 0,
    "text": "string",
    "author": "string",
    "pub_date": "2019-08-24T14:15:22Z"
}
```

Добавление комментария к отзыву:

`POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/`
```
{
    "text": "string"
}
```

Частичное обновление комментария к отзыву по id:

`PATCH http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/`
```
{
    "text": "string"
}
```

Удаление комментария к отзыву по id:

`DELETE http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/`

## Users:

Получение данных своей учетной записи:

`GET http://127.0.0.1:8000/api/v1/users/me/`
```
{
    "username": "string",
    "email": "user@example.com",
    "first_name": "string",
    "last_name": "string",
    "bio": "string",
    "role": "user"
}
```

Изменение данных своей учетной записи (поля `email` и `username` должны быть уникальными):

`PATCH http://127.0.0.1:8000/api/v1/users/me/`
```
{
    "username": "string",
    "email": "user@example.com",
    "first_name": "string",
    "last_name": "string",
    "bio": "string"
}
```

Получение списка всех пользователей:

`GET http://127.0.0.1:8000/api/v1/users/`
```
[
    {
        "count": 0,
        "next": "string",
        "previous": "string",
        "results": [
            {
                "username": "string",
                "email": "user@example.com",
                "first_name": "string",
                "last_name": "string",
                "bio": "string",
                "role": "user",
            }
        ]
    }
]
```

Получение пользователя по `username`:

`GET http://127.0.0.1:8000/api/v1/users/{username}/`
```
{
    "username": "string",
    "email": "user@example.com",
    "first_name": "string",
    "last_name": "string",
    "bio": "string",
    "role": "user"
}
```

Добавление пользователя (поля `email` и `username` должны быть уникальными):

`POST http://127.0.0.1:8000/api/v1/users/`
```
{
    "username": "string",
    "email": "user@example.com",
    "first_name": "string",
    "last_name": "string",
    "bio": "string",
    "role": "user"
}
```

Изменение данных пользователя по `username`:

`PATCH http://127.0.0.1:8000/api/v1/users/{username}/`
```
{
    "username": "string",
    "email": "user@example.com",
    "first_name": "string",
    "last_name": "string",
    "bio": "string",
    "role": "user"
}
```

Удаление пользователя по `username`:

`DELETE http://127.0.0.1:8000/api/v1/users/{username}/`

[__В начало__](#anchor) :point_up:
