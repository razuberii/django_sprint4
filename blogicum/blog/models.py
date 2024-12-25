# Импорт необходимых модулей и классов из Django
from django.contrib.auth import get_user_model  # Импортируем функцию для получения модели пользователя
from django.db import models  # Импортируем базовый класс для создания моделей
from django.db.models import Count  # Импортируем функцию для подсчета количества связанных объектов
from django.utils import timezone  # Импортируем модуль для работы с временными зонами

# Импортируем базовые классы для создания полей CreatedAt и IsPublished
from core.models import CreatedAt, IsPublished

# Константы для ограничения длины строк
LENGTH_STRING = 20
MAX_LENGTH = 256

# Получаем модель пользователя, настроенную в проекте
User = get_user_model()


# Определение пользовательского QuerySet для фильтрации публикаций
class PublishedQuerySet(models.QuerySet):

    # Метод для фильтрации постов, доступных для публикации
    def filter_posts_for_publication(self):
        return self.filter(
            pub_date__lte=timezone.now(),  # Дата публикации должна быть меньше или равна текущему времени
            is_published=True,  # Публикация должна быть отмечена как опубликованная
            category__is_published=True,  # Категория должна быть опубликованной
        )

    # Метод для подсчета количества комментариев к постам
    def count_comments(self):
        return self.select_related(
            'category', 'location', 'author'  # Загружаем связанные объекты для оптимизации запросов
        ).annotate(comment_count=Count('comments')).order_by('-pub_date')  # Считаем комментарии и сортируем по дате публикации


# Определение модели Category (Категория)
class Category(CreatedAt, IsPublished):

    title = models.CharField('Заголовок', max_length=MAX_LENGTH)  # Поле для заголовка категории
    description = models.TextField('Описание')  # Поле для описания категории
    slug = models.SlugField(
        'Идентификатор',
        unique=True,  # Идентификатор должен быть уникальным
        help_text='Идентификатор страницы для URL; разрешены символы '
                  'латиницы, цифры, дефис и подчёркивание.'
    )

    class Meta:
        verbose_name = 'категория'  # Человекочитаемое имя модели в единственном числе
        verbose_name_plural = 'Категории'  # Человекочитаемое имя модели во множественном числе

    def __str__(self):
        return self.title[:LENGTH_STRING]  # Возвращаем заголовок категории с ограничением по длине


# Определение модели Location (Местоположение)
class Location(CreatedAt, IsPublished):

    name = models.CharField('Название места', max_length=MAX_LENGTH)  # Поле для названия местоположения

    class Meta:
        verbose_name = 'местоположение'  # Человекочитаемое имя модели в единственном числе
        verbose_name_plural = 'Местоположения'  # Человекочитаемое имя модели во множественном числе

    def __str__(self):
        return self.name[:LENGTH_STRING]  # Возвращаем название местоположения с ограничением по длине


# Определение модели Post (Публикация)
class Post(CreatedAt, IsPublished):

    title = models.CharField('Заголовок', max_length=MAX_LENGTH)  # Поле для заголовка поста
    text = models.TextField('Текст')  # Поле для текста поста
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        help_text='Если установить дату и время в будущем'
                  ' — можно делать отложенные публикации.'  # Подсказка о возможности отложенной публикации
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # Удаление поста при удалении автора
        verbose_name='Автор публикации',
        related_name='posts',  # Связь с постами автора
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,  # Удаление местоположения не приводит к удалению поста
        null=True,
        blank=True,
        verbose_name='Местоположение',
        related_name='posts'  # Связь с постами по местоположению
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,  # Удаление категории не приводит к удалению поста
        null=True,
        verbose_name='Категория',
        related_name='posts'  # Связь с постами по категории
    )
    image = models.ImageField(
        'Фото', blank=True, upload_to='posts_images/', null=True  # Поле для загрузки изображения поста
    )

    class Meta:
        verbose_name = 'публикация'  # Человекочитаемое имя модели в единственном числе
        verbose_name_plural = 'Публикации'  # Человекочитаемое имя модели во множественном числе
        ordering = ('-pub_date',)  # Сортировка постов по дате публикации в обратном порядке

    objects = PublishedQuerySet.as_manager()  # Использование пользовательского QuerySet как менеджера объектов

    def __str__(self):
        return self.title[:LENGTH_STRING]  # Возвращаем заголовок поста с ограничением по длине


# Определение модели Comment (Комментарий)
class Comment(CreatedAt):

    text = models.TextField('Текст')  # Поле для текста комментария
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,  # Удаление комментария при удалении поста
        verbose_name='Пост',
        related_name='comments'  # Связь с комментариями поста
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # Удаление комментария при удалении автора
        verbose_name='Автор комментария',
        related_name='comments'  # Связь с комментариями автора
    )

    class Meta:
        ordering = ('created_at',)  # Сортировка комментариев по времени создания
        verbose_name = 'комментарий'  # Человекочитаемое имя модели в единственном числе
        verbose_name_plural = 'Комментарии'  # Человекочитаемое имя модели во множественном числе

    def __str__(self):
        return self.text[:LENGTH_STRING]  # Возвращаем текст комментария с ограничением по длине
