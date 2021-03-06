FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true

RUN mkdir /src
RUN mkdir /static

WORKDIR /src
ADD ./src /src

RUN pip3 install -r requirements.txt
#RUN pytest

CMD pytest && python3 manage.py makemigrations; python3 manage.py migrate; python3 manage.py collectstatic --no-input; ./wait-for-it.sh -t 60 db:5432 -- gunicorn romnum.wsgi -b 0.0.0.0:8000

