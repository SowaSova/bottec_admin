import os
from django.utils import timezone


def product_image_upload_to(instance, filename):
    """
    Генерирует имя файла на основе слага продукта и текущего времени.
    Формат имени: <slug>_<YYYYMMDDHHMMSS>.<расширение>
    """
    # Получаем расширение файла
    ext = os.path.splitext(filename)[1]

    # Генерируем таймстамп
    timestamp = timezone.now().strftime("%Y%m%d%H%M%S")

    # Формируем новое имя файла
    new_filename = f"{instance.slug}_{timestamp}{ext}"

    return new_filename
