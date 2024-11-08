#!/bin/sh

# Применение миграций
echo "Применение миграций..."
python manage.py migrate

# Сбор статических файлов
echo "Сбор статических файлов..."
python manage.py collectstatic --noinput

# Запуск сервера
echo "Запуск сервера..."
uvicorn adminpanel.asgi:application --host 0.0.0.0 --port 8000 --forwarded-allow-ips "*" --proxy-headers --workers 4