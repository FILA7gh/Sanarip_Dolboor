# сайт магазина одежд

## Старт проекта

Создать .env файл с .env.example и заполнить их необходимыми значениями.

Установить зависимости:
pip install -r requirements.rxt

Активировать виртуальное окружения:
source venv.bin.activate

Накатить миграции:
python manage.py migrate

Создать суперпользователя для доступа к админке:
python manage.py createsuperuser

Запуск приложения:
python manage.py runserver

## Панель администратора
http://localhost:8000/admin/