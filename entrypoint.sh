#!/bin/sh
echo "Ожидание MySQL..."
while ! nc -z mysql_db 3306; do sleep 1; done
echo "MySQL запущен."

echo "Запускаем бота..."
exec python bot/main.py