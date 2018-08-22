FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true

RUN mkdir /src
RUN mkdir /static

WORKDIR /src
ADD ./src /src

RUN pip3 install -r requirements.txt

CMD python3 manage.py collectstatic --no-input; python3 manage.py migrate; ./wait-for-it.sh -t 60 db:5432 -- gunicorn romnum.wsgi -b 0.0.0.0:8000

