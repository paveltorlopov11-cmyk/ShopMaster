import sys
import os

# Добавляем текущую директорию в путь для импорта app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, Product, User
from werkzeug.security import generate_password_hash
from datetime import datetime


def seed_database():
    with app.app_context():
        # Очистка существующих данных (опционально)
        Product.query.delete()

        # Тестовые товары
        products = [
            # Электроника
            Product(
                name="Смартфон Samsung Galaxy S23",
                description="Флагманский смартфон с камерой 50 Мп, 8ГБ ОЗУ, 256ГБ памяти",
                price=79999.99,
                category="Электроника",
                stock=15,
                image_filename="smartphone.jpg"
            ),
            Product(
                name="Ноутбук ASUS VivoBook 15",
                description="15.6 дюймов, Intel Core i5, 8ГБ ОЗУ, 512ГБ SSD",
                price=54999.99,
                category="Электроника",
                stock=8,
                image_filename="laptop.jpg"
            ),
            Product(
                name="Наушники Sony WH-1000XM5",
                description="Беспроводные наушники с шумоподавлением, 30 часов работы",
                price=29999.99,
                category="Электроника",
                stock=25,
                image_filename="headphones.jpg"
            ),
            Product(
                name="Умные часы Apple Watch Series 9",
                description="45 мм, GPS, Always-On дисплей, мониторинг здоровья",
                price=44999.99,
                category="Электроника",
                stock=12,
                image_filename="smartwatch.jpg"
            ),

            # Одежда
            Product(
                name="Джинсы Levi's 501",
                description="Классические прямые джинсы, 100% хлопок",
                price=5999.99,
                category="Одежда",
                stock=40,
                image_filename="jeans.jpg"
            ),
            Product(
                name="Куртка зимняя The North Face",
                description="Теплая зимняя куртка с пуховым утеплителем, водонепроницаемая",
                price=12999.99,
                category="Одежда",
                stock=18,
                image_filename="jacket.jpg"
            ),
            Product(
                name="Футболка мужская Nike Dri-FIT",
                description="Спортивная футболка с технологией отвода влаги",
                price=2499.99,
                category="Одежда",
                stock=60,
                image_filename="tshirt.jpg"
            ),
            Product(
                name="Платье вечернее Zara",
                description="Элегантное вечернее платье, длина миди",
                price=8999.99,
                category="Одежда",
                stock=22,
                image_filename="dress.jpg"
            ),

            # Книги
            Product(
                name="Книга 'Мастер и Маргарита'",
                description="Михаил Булгаков, коллекционное издание",
                price=1499.99,
                category="Книги",
                stock=35,
                image_filename="book1.jpg"
            ),
            Product(
                name="Книга 'Python для начинающих'",
                description="Полное руководство по программированию на Python",
                price=2999.99,
                category="Книги",
                stock=28,
                image_filename="book2.jpg"
            ),
            Product(
                name="Книга 'Гарри Поттер и философский камень'",
                description="Дж. К. Роулинг, иллюстрированное издание",
                price=2499.99,
                category="Книги",
                stock=45,
                image_filename="book3.jpg"
            ),

            # Бытовая техника
            Product(
                name="Холодильник Samsung Side by Side",
                description="Объем 620 литров, No Frost, инверторный компрессор",
                price=89999.99,
                category="Бытовая техника",
                stock=5,
                image_filename="fridge.jpg"
            ),
            Product(
                name="Стиральная машина LG",
                description="Загрузка 8 кг, прямым приводом, паровая обработка",
                price=45999.99,
                category="Бытовая техника",
                stock=9,
                image_filename="washing_machine.jpg"
            ),
        ]

        # Добавляем товары в базу
        for product in products:
            db.session.add(product)

        # Создаем тестового пользователя если его нет
        if not User.query.filter_by(username='testuser').first():
            user = User(
                username='testuser',
                email='test@example.com',
                password_hash=generate_password_hash('test123'),
                is_admin=False
            )
            db.session.add(user)

        db.session.commit()
        print(f"Добавлено {len(products)} тестовых товаров")
        print("Тестовый пользователь: testuser / test123")


if __name__ == "__main__":
    seed_database()