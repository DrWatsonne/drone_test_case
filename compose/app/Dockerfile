FROM python:3.7.6-alpine3.11

ENV USR_LOCAL_BIN=/usr/local/bin/  \
    PROJECT_ROOT=/app

ENV PYTHONPATH=$PYTHONPATH:$PROJECT_ROOT

ENV RUNTIME_PACKAGES \
    libev \
    pcre \
    postgresql-dev \
    libmagic \
    libjpeg

ENV BUILD_PACKAGES \
    libev-dev \
    git \
    build-base \
    pcre-dev \
    gcc \
    linux-headers \
    libc-dev \
    musl-dev \
    jpeg-dev \
    zlib-dev

RUN mkdir $PROJECT_ROOT/ && \
    mkdir $PROJECT_ROOT/run && \
    mkdir $PROJECT_ROOT/wsgi

COPY ./Pipfile ./Pipfile.lock $PROJECT_ROOT/
WORKDIR $PROJECT_ROOT

RUN pip install --upgrade wheel pip pipenv \
    && apk --no-cache add --virtual build-deps $BUILD_PACKAGES \
    && apk --no-cache add $RUNTIME_PACKAGES \
    && set -ex && pipenv install --deploy --system --dev \
    && apk del build-deps

COPY ./src $PROJECT_ROOT

COPY ./compose/app/start_uwsgi $USR_LOCAL_BIN/

RUN sed -i 's/\r//' $USR_LOCAL_BIN/start_uwsgi \
    && chmod +x $USR_LOCAL_BIN/start_uwsgi

COPY ./compose/app/uwsgi.ini $PROJECT_ROOT/wsgi

EXPOSE 8000

CMD ["start_uwsgi"]