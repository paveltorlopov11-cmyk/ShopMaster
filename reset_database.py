import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db
from werkzeug.security import generate_password_hash


def recreate_database():
    with app.app_context():
        # Удаляем все таблицы
        db.drop_all()

        # Создаем заново
        db.create_all()
        print("База данных успешно пересоздана!")

        # Можно добавить тестовые данные если нужно
        # ...


if __name__ == "__main__":
    recreate_database()