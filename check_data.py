import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, Product


def check_and_fix_data():
    with app.app_context():
        print("Проверка данных в базе...")

        # Проверяем все товары
        products = Product.query.all()

        for product in products:
            print(f"\nТовар ID {product.id}: {product.name}")

            # Исправляем описание если есть проблемы
            if product.description and 'Иухаил' in product.description:
                print(f"  Найдена ошибка в описании: {product.description[:50]}...")
                product.description = product.description.replace('Иухаил', 'Михаил')
                print(f"  Исправлено на: {product.description[:50]}...")

            # Устанавливаем категорию по умолчанию если пустая
            if not product.category:
                product.category = 'Другое'
                print(f"  Установлена категория по умолчанию: {product.category}")

        db.session.commit()
        print("\nПроверка завершена!")


if __name__ == "__main__":
    check_and_fix_data()