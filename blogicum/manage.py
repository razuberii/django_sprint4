#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""  # Докстринг, описывающий назначение этого файла: утилита командной строки Django для административных задач.

import os  # Импортируем модуль os для работы с операционной системой.
import sys  # Импортируем модуль sys для работы с параметрами командной строки.

def main():
    """Run administrative tasks."""  # Докстринг, описывающий функцию main, которая выполняет административные задачи.
    
    # Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE, указывающую на настройки проекта Django.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')
    
    try:
        # Импортируем функцию execute_from_command_line из модуля django.core.management.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Если импорт не удался, выбрасываем исключение с сообщением об ошибке.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc  # Указываем оригинальную ошибку, которая привела к ImportError.
    
    # Вызываем функцию execute_from_command_line с аргументами командной строки, переданными скрипту.
    execute_from_command_line(sys.argv)

# Проверяем, является ли этот файл основным модулем (т.е. запущен ли он напрямую).
if __name__ == '__main__':
    main()  # Если да, вызываем функцию main для выполнения административных задач.
