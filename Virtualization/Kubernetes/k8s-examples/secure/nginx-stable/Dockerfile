# docker build --tag rezroo/nginx:1.14 .
FROM nginx:stable

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./default.conf /etc/nginx/conf.d/default.conf

RUN touch /var/run/nginx.pid && \
  chown -R www-data:www-data /var/run/nginx.pid && \
  chown -R www-data:www-data /var/cache/nginx

#USER www-data
#USER 33:33

VOLUME /var/www

