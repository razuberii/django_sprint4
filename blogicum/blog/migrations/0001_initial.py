from django.conf import settings  # Импорт настроек проекта
from django.db import migrations, models  # Импорт необходимых классов для миграций и моделей
import django.db.models.deletion  # Импорт для управления зависимостями при удалении объектов


class Migration(migrations.Migration):
    # Определение класса миграции

    initial = True  # Указывает, что это первая миграция для данного приложения

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),  # Зависимость от модели пользователя
    ]

    operations = [
        # Операции, которые будут выполнены в этой миграции

        migrations.CreateModel(
            name='Category',  # Название модели
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # Автоматически создаваемый ID
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),  # Поле для статуса публикации
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),  # Дата и время создания записи
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')),  # Заголовок категории
                ('description', models.TextField(verbose_name='Описание')),  # Описание категории
                ('slug', models.SlugField(help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.', unique=True, verbose_name='Идентификатор')),  # Уникальный идентификатор для URL
            ],
            options={
                'verbose_name': 'категория',  # Человекочитаемое название модели в единственном числе
                'verbose_name_plural': 'Категории',  # Человекочитаемое название модели во множественном числе
            },
        ),

        migrations.CreateModel(
            name='Location',  # Название модели
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # Автоматически создаваемый ID
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),  # Поле для статуса публикации
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),  # Дата и время создания записи
                ('name', models.CharField(max_length=256, verbose_name='Название места')),  # Название местоположения
            ],
            options={
                'verbose_name': 'местоположение',  # Человекочитаемое название модели в единственном числе
                'verbose_name_plural': 'Местоположения',  # Человекочитаемое название модели во множественном числе
            },
        ),

        migrations.CreateModel(
            name='Post',  # Название модели
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # Автоматически создаваемый ID
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),  # Поле для статуса публикации
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),  # Дата и время создания записи
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')),  # Заголовок публикации
                ('text', models.TextField(verbose_name='Текст')),  # Основной текст публикации
                ('pub_date', models.DateTimeField(help_text='Если установить дату и время в будущем — можно делать отложенные публикации.', verbose_name='Дата и время публикации')),  # Дата и время публикации с возможностью отложенной публикации
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор публикации')),  # Связь с моделью пользователя (автор публикации)
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='blog.category', verbose_name='Категория')),  # Связь с моделью категории (может быть null)
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='blog.location', verbose_name='Местоположение')),  # Связь с моделью местоположения (может быть пустым или null)
            ],
            options={
                'verbose_name': 'публикация',  # Человекочитаемое название модели в единственном числе
                'verbose_name_plural': 'Публикации',  # Человекочитаемое название модели во множественном числе
                'ordering': ('-pub_date',),  # Сортировка по дате публикации (по убыванию)
            },
        ),
    ]
