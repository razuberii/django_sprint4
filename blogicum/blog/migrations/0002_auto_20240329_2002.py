from django.db import migrations, models  # Импорт классов для работы с миграциями и моделями


class Migration(migrations.Migration):
    # Определение класса миграции

    dependencies = [
        ('blog', '0001_initial'),  # Зависимость от предыдущей миграции в приложении 'blog'
    ]

    operations = [
        # Операции, которые будут выполнены в этой миграции

        migrations.AlterModelOptions(
            name='post',  # Имя модели, для которой изменяются параметры
            options={
                'default_related_name': 'posts',  # Установка стандартного имени для обратной связи
                'ordering': ('-pub_date',),  # Установка порядка сортировки по дате публикации (по убыванию)
                'verbose_name': 'публикация',  # Человекочитаемое название модели в единственном числе
                'verbose_name_plural': 'Публикации',  # Человекочитаемое название модели во множественном числе
            },
        ),

        migrations.AlterField(
            model_name='category',  # Имя модели, для которой изменяется поле
            name='description',  # Имя поля, которое изменяется
            field=models.TextField(default=True, verbose_name='Описание'),  # Изменение поля description на TextField с значением по умолчанию True
        ),

        migrations.AlterField(
            model_name='category',  # Имя модели, для которой изменяется поле
            name='is_published',  # Имя поля, которое изменяется
            field=models.BooleanField(default=True, help_text='Снимите галочку, чтобы скрыть публикацию.', verbose_name='Опубликовано'),  # Изменение поля is_published с добавлением подсказки
        ),

        migrations.AlterField(
            model_name='location',  # Имя модели, для которой изменяется поле
            name='is_published',  # Имя поля, которое изменяется
            field=models.BooleanField(default=True, help_text='Снимите галочку, чтобы скрыть публикацию.', verbose_name='Опубликовано'),  # Изменение поля is_published с добавлением подсказки
        ),

        migrations.AlterField(
            model_name='post',  # Имя модели, для которой изменяется поле
            name='is_published',  # Имя поля, которое изменяется
            field=models.BooleanField(default=True, help_text='Снимите галочку, чтобы скрыть публикацию.', verbose_name='Опубликовано'),  # Изменение поля is_published с добавлением подсказки
        ),

        migrations.AlterField(
            model_name='post',  # Имя модели, для которой изменяется поле
            name='title',  # Имя поля, которое изменяется
            field=models.CharField(max_length=256),  # Изменение поля title на CharField с максимальной длиной 256 символов
        ),
    ]
