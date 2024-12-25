from django.apps import AppConfig  # Импортируем класс AppConfig из Django для настройки приложения

# Определяем класс конфигурации приложения PagesConfig, который наследует от AppConfig
class PagesConfig(AppConfig):
    # Указываем тип поля для автоматического увеличения идентификаторов по умолчанию
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Задаем имя приложения, которое будет использоваться в Django
    name = 'pages'
