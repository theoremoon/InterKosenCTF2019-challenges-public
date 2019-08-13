FROM php:7.3-apache

RUN apt update -y && apt install -y sqlite3
ADD challenge/ /var/www/
WORKDIR /var/www/
RUN chown -R www-data .
