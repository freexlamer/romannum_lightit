# Конвертер римских и арабских чисел

## Установка и запуск в Docker с помощью docker-compose.
### Утсановка:
* создать файл `django.env` 
* сгенерировать SECRET_KEY (например так https://gist.github.com/ndarville/3452907 ) и записать  его в переменную `DJANGO_SECRET_KEY` в `django.env` 
* `docker-compose build`

### Запуск:
* `docker-compose up -d`
* Открыть в браузере `http://localhost:8000/`

### Завершение работы:
* `docker-compose down`

## Установка и запуск с использованием `pipenv`.
### Утсановка:
* `cd src`
* создать файл `.env`
* сгенерировать SECRET_KEY (например так https://gist.github.com/ndarville/3452907 ) и записать  его в переменную `DJANGO_SECRET_KEY` в `.env`
* `DEBUG_MODE=True` в `.env`
* `DJANGO_ALLOWED_HOST=*` в `.env`
* `cp romnum/settings.py.pipenv romnum/settings.py`
* `pip3 install pipenv`
* `pipenv --python 3` (в системе должен быть установлен python версии 3, но ниже 3.7)
* `pipenv install`
* `pipenv run manage.py migrate`

### Запуск:
* `cd src`
* `pipenv run python manage.py runserver 0.0.0:8000`
* Открыть в браузере `http://localhost:8000/`

### Завершение работы:
* CTRL-C


