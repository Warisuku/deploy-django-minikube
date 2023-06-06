FROM python:3.11.2-alpine3.17

COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./headers.conf /etc/nginx/headers.conf
COPY ./run.py /run.py

ENV LISTEN_PORT=8000
ENV APP_HOST=app
ENV APP_PORT=8080

USER root

RUN echo "http://dl-cdn.alpinelinux.org/alpine/v3.17/main" > /etc/apk/repositories && \
    echo "http://dl-cdn.alpinelinux.org/alpine/v3.17/community" >> /etc/apk/repositories && \
    apk add --update --no-cache nginx gettext && \
    mkdir -p /run/nginx && \
    mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    mkdir -p /etc/nginx/conf.d && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.py && \
    chown -R nginx:nginx /etc/nginx

VOLUME /vol/static

USER nginx

CMD ["/usr/bin/env", "python", "/run.py"]
