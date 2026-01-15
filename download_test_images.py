import requests
import os


def download_test_images():
    # Создаем папку для изображений
    os.makedirs('static/uploads/products', exist_ok=True)

    # Тестовые URL изображений (можно заменить на свои)
    images = {
        'smartphone.jpg': 'https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=300&h=200&fit=crop',
        'laptop.jpg': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=300&h=200&fit=crop',
        'headphones.jpg': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=300&h=200&fit=crop',
        'smartwatch.jpg': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w-300&h=200&fit=crop',
        'jeans.jpg': 'https://images.unsplash.com/photo-1542272604-787c3835535d?w=300&h=200&fit=crop',
        'jacket.jpg': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=300&h=200&fit=crop',
        'tshirt.jpg': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=300&h=200&fit=crop',
        'dress.jpg': 'https://images.unsplash.com/photo-1562299062-9d5f734a1bd4?w=300&h=200&fit=crop',
        'book1.jpg': 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=300&h=200&fit=crop',
        'book2.jpg': 'https://images.unsplash.com/photo-1541963463532-d68292c34b19?w=300&h=200&fit=crop',
        'book3.jpg': 'https://images.unsplash.com/photo-1512820790803-83ca734da794?w=300&h=200&fit=crop',
        'fridge.jpg': 'https://images.unsplash.com/photo-1571175443880-49e1d25b2bc5?w=300&h=200&fit=crop',
        'washing_machine.jpg': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=300&h=200&fit=crop'
    }

    for filename, url in images.items():
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(f'static/uploads/products/{filename}', 'wb') as f:
                    f.write(response.content)
                print(f"Скачано: {filename}")
            else:
                print(f"Ошибка скачивания {filename}: {response.status_code}")
        except Exception as e:
            print(f"Ошибка при скачивании {filename}: {e}")

    print("Все изображения загружены!")


if __name__ == "__main__":
    download_test_images()