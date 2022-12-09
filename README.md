# drf

# Инструкция по поднятию

Скачать данный репозиторий:

    git clone https://github.com/BondarenkoDV/drf.git

Ввести следующие команды в терминал:

    docker-compose build
    docker-compose up -d

Выполнить миграции Django:

    python manage.py migrate

[Список тикетов](127.0.0.1:8000/app/api/token/tickets_list/)
