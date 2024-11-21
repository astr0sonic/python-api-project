# My project

## Start

Create the virtual environment:

```bash
./create-venv.sh
```

Start:

```bash
./start.sh
```

## Базовый функционал (MVP)

Приложение для работы ToDo-списками.

1. регистрация/авторизация:

```
POST /auth/sign-up - регистрация
POST /auth/sign-in - авторизация
```

2. работа со списками задач:
    1. получение списков
    2. получение списка
    3. создание нового списка
    4. редактирование списка
    5. удаление списка

```
GET /lists - получение списков
GET /lists/{id} - получение списка
POST /lists - создание списка
PUT /lists/{id} - редактирование списка
DELETE /lists/{id} - удаление списка
```

3. работа с задачи:
    1. создание задачи
    2. получение задач списка
    3. получение задачи
    3. редактирование задачи
    4. удаление задачи

```
POST /lists/{id}/tasks
GET /lists/{id}/tasks
GET /tasks/{id}
PUT /tasks/{id}
DELETE /tasks/{id}
```

Сущности:
пользователь, список задач, задача

[Схема БД](https://miro.com/welcomeonboard/WXQzS3B5ZHVEbEJUbktnT0svTHcra2dUV3NLZWdocFR2ZC9oRUFGaGJ4V2tjcnlhdnJOUmRYNVNhUzVDSHFjc1ZCSjRrOGtSdGp4Uy9hNy9CVGdSWFJTNEFra0VZWE5FOWhscEwrb3pXR3JVeFRHdHBKbGs1Vk9uenpyRGw1QzAhZQ==?share_link_id=733472881396)
