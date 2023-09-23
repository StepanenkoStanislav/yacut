# Сервис укорачивания ссылок YaCut

## Описание проекта

Проект YaCut ассоциирует длинную пользовательскую ссылку с 
короткой, которую предлагает сам пользователь или предоставляет
сервис. 

## Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

В директории _yacut_ необходимо создать файл _.env_
(Пример находится в yacut/example.env), где необходимо указать:
```
FLASK_APP=yacut - определяем, как запустить приложение

FLASK_ENV=production - определяем режим работы (production или development)

SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/' - указываем секретный ключ (это должна
быть длинная строка из символов, символы unicode поддерживаются)

SQLALCHEMY_DATABASE_URI=sqlite:///db.sqlite3 - указываем БД

FLASK_RUN_HOST=127.0.0.1 - указываем хост

FLASK_RUN_PORT=5000 - указываем порт
```

### Запуск

Находясь в директории _yacut_ введите в терминале команду
```commandline
flask run
```
По умолчанию проект будет доступен по адресу http://127.0.0.1:5000

Описание ендпоинтов API по умолчанию будет доступно по адресу 
http://127.0.0.1:5000/api/docs

### Примеры запросов

- POST запрос к /api/id/ - создание короткой ссылки
```
{
  "url": "https://docs.python.org/3/whatsnew/3.11.html",
  "custom_id": "whatsnew"
}
```
Ответ
```
{
  "url": "https://docs.python.org/3/whatsnew/3.11.html",
  "short_link": "whatsnew"
}
```

- GET запрос к /api/id/{short_id}/ - получение исходной ссылки

Ответ на запрос /api/id/whatsnew/
```
{
  "url": "https://docs.python.org/3/whatsnew/3.11.html"
}
```

## Технологии

В проекте используются следующие технологии:
- Python 3.7
- Flask 2.0.2
- SQLAlchemy 1.4.29

## Автор

[Степаненко Станислав](https://t.me/tme_zoom)
