Онлайн платформа торговой сети электроники

Веб-приложение с API интерфейсом и админ-панелью.

Описание проекта

Сеть должна представлять собой иерархическую структуру из трех уровней:
завод;
розничная сеть;
индивидуальный предприниматель.
Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии). Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети, т. е. завод всегда находится на уровне 0, а если розничная сеть относится напрямую к заводу, минуя остальные звенья, ее уровень — 1. Если в цепочке есть завод, то он всегда находится на 0 уровне, это значит что розничная сеть или ИП в этом случае будут находиться на 1 или 2 уровнях соостветственно (например завод - ип - розничная сеть). Возможна ситуация, когда в цепочке нету завода (например розничная сеть - ип - ип), в этом случае на 0 уровне будут находится ИП или розничная сеть. Максимальное количество уровней в иерархии - 3 (0, 1 , 2), это значит, что в цепочке может быть не более трех звеньев.

Реализация

В проекте представлены три приложения: пользователи, продукты и поставщики (звенья сети).
Реализован набор представлений CRUD для всех моделей (пользователь, продукт, поставщик). Так же все данные отображаются и в админ панели. Все эндпоинты, за исключением регистрации нового пользователя защищены от доступа неактивного пользователя, т к неактивный пользователь не может получить JWT токен при авторизации. Для модели supplier отсуттвоет возможность явно указать уровень иерархии, т к он присваевается автоматически на основании отношению каждого звена сети к предыдущему. Так же отсутствует возможность изменить сумму задолжности через API. Задолжность перед постовщиком можно обнулить по специально кнопке, расположенной в админ панели. Так же для модели supplier настроена валидации и фильтрация данных. В админ панели у модели поставщика выводится ссылка на предыдущего поставщика.

Инструкция по запуску

Клонируем репозиторий

Устанавливаем виртуальное окружение
python3 -m venv env 

Запускаем виртуальное окружение
source env/bin/activate

Устанавливаем библиотеки
pip install -r requirements.txt

Создаем базу данных в PgAdmin

Создаем файл <.env> и заполняем его по шаблону

Выполнить миграции

python manage.py makemigrations
python manage.py migrate

Создаем superuser 
python manage.py csu
login: admin password: 111

Запускаем проект
python manage.py runserver

Технические требования
Python 3.8+
Django 3+
DRF 3.10+
PostgreSQL 10+
