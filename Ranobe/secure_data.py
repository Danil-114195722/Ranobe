import os
from dotenv import load_dotenv


# загрузка переменных окружения
load_dotenv()

# имя БД
DB_NAME = os.getenv('MYSQL_DATABASE')
# имя юзера
DB_USER = os.getenv('DB_USER')
# пароль юзера
DB_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD')
# ip БД
DB_HOST = os.getenv('DB_HOST')
# порт
PORT = os.getenv('PORT')
# сокет БД
DB_SOCKET = os.getenv('DB_SOCKET')

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(' ')
DEBUG = True if os.getenv('DEBUG') == 'True' else False

# Django key
DJANGO_SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
# путь на сайте к админке
ADMIN_URL = os.getenv('ADMIN_URL')
