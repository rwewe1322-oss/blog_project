# Blog Project

Учебный проект — блог на Django. Позволяет добавлять и просматривать посты.

## Стек технологий
- Python 3.12
- Django 6.1
- PostgreSQL
- Docker

## Как запустить
1. Клонировать репозиторий:
   `git clone https://github.com/rwewe1322-oss/blog_project.git`
2. Собрать Docker-образ:
   `docker build -t blog_app .`
3. Запустить контейнер:
   `docker run -p 8000:8000 blog_app`
4. Открыть в браузере:
   `http://127.0.0.1:8000/`

## Автор
Даниил Костенко
