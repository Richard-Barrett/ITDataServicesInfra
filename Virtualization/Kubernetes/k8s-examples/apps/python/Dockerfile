# https://github.com/realpython/django-redis-cache
# https://realpython.com/caching-in-django-with-redis/

From python:3.4-alpine3.7

#RUN apk add --no-cache git mercurial \
#    && go get github.com/random/library/that/I/use/ \
#    && apk del git mercurial
RUN apk add --no-cache git

RUN git clone https://github.com/realpython/django-redis-cache.git
WORKDIR django-redis-cache
RUN git checkout tags/1
RUN pip install -r requirements.txt
RUN python manage.py makemigrations cookbook
RUN python manage.py migrate
RUN python manage.py createsuperuser
RUN python manage.py loaddata cookbook/fixtures/cookbook.json

CMD python manage.py runserver

