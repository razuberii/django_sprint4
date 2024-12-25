# Импорт необходимых модулей из Django
from django.contrib import admin

# Импорт моделей, которые будут зарегистрированы в админке
from .models import Category, Comment, Location, Post

# Константы для настройки длины строк и количества постов на странице
LENGTH_STRING = 50  # Максимальная длина строки для отображения
NUMBER_OF_POSTS = 10  # Количество постов, отображаемых на одной странице

# Регистрация модели Post в админке с кастомизацией
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Кастомизация админки для модели Post."""

    # Поля, которые будут отображаться в списке постов
    list_display = (
        'title',  # Заголовок поста
        'text_short',  # Краткий текст поста (обрезанный)
        'location',  # Местоположение поста
        'category',  # Категория поста
        'pub_date',  # Дата публикации
        'is_published',  # Статус публикации
    )
    
    # Поля, которые можно редактировать непосредственно в списке
    list_editable = (
        'location',  # Местоположение поста
        'category',  # Категория поста
        'pub_date',  # Дата публикации
        'is_published',  # Статус публикации
    )
    
    # Поля, по которым можно производить поиск
    search_fields = (
        'title',  # Заголовок поста
        'text',  # Текст поста
        'location',  # Местоположение поста
    )
    
    # Количество постов на странице
    list_per_page = NUMBER_OF_POSTS

    @staticmethod
    @admin.display(description='Текст')  # Человекочитаемое имя для поля в админке
    def text_short(object: Post) -> str:
        """Возвращает обрезанный текст поста для отображения."""
        return f'{object.text[:LENGTH_STRING]}...'  # Обрезаем текст до LENGTH_STRING символов и добавляем многоточие


# Регистрация модели Category в админке с кастомизацией
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    # Поля, которые будут отображаться в списке категорий
    list_display = (
        'title',  # Заголовок категории
        'description_short',  # Краткое описание категории (обрезанное)
        'slug',  # Уникальный идентификатор категории
        'is_published',  # Статус публикации категории
        'created_at',  # Дата создания категории
    )
    
    # Поля, которые можно редактировать непосредственно в списке
    list_editable = (
        'slug',  # Уникальный идентификатор категории
    )
    
    # Фильтры для упрощения поиска категорий
    list_filter = (
        'title',  # Фильтр по заголовку категории
        'description',  # Фильтр по описанию категории
    )
    
    # Количество категорий на странице
    list_per_page = NUMBER_OF_POSTS

    @staticmethod
    @admin.display(description='Описание')  # Человекочитаемое имя для поля в админке
    def description_short(object: Category) -> str:
        """Возвращает обрезанное описание категории для отображения."""
        return f'{object.description[:LENGTH_STRING]}...'  # Обрезаем описание до LENGTH_STRING символов и добавляем многоточие


# Регистрация модели Location в админке с кастомизацией
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """Кастомизация админки для модели Location."""

    # Поля, которые будут отображаться в списке местоположений
    list_display = (
        'name',  # Название местоположения
        'is_published',  # Статус публикации местоположения
        'created_at',  # Дата создания местоположения
    )
    
    # Поля, которые можно редактировать непосредственно в списке
    list_editable = ('is_published',)  # Статус публикации местоположения
    
    # Фильтры для упрощения поиска местоположений
    list_filter = ('name',)  # Фильтр по названию местоположения
    
    # Количество местоположений на странице
    list_per_page = NUMBER_OF_POSTS


# Регистрация модели Comment в админке с кастомизацией
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Кастомизация админки для модели Comment."""

    # Поля, которые будут отображаться в списке комментариев
    list_display = (
        'text',  # Текст комментария
        'post',  # Пост, к которому относится комментарий
        'author',  # Автор комментария
        'created_at',  # Дата создания комментария
    )
    
    # Фильтры для упрощения поиска комментариев
    list_filter = ('text',)  # Фильтр по тексту комментария
    
    # Количество комментариев на странице
    list_per_page = NUMBER_OF_POSTS
