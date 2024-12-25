# Импорт необходимых модулей и классов из Django
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

# Определение класса миграции
class Migration(migrations.Migration):

    # Зависимости от других миграций и моделей
    dependencies = [
        # Зависимость от модели пользователя, которая может быть заменена
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        # Зависимость от предыдущей миграции в приложении 'blog'
        ('blog', '0002_auto_20240329_2002'),
    ]

    # Операции, которые будут выполнены в этой миграции
    operations = [
        # Изменение параметров модели 'post'
        migrations.AlterModelOptions(
            name='post',
            options={
                'ordering': ('-pub_date',),  # Установка порядка сортировки по дате публикации (по убыванию)
                'verbose_name': 'публикация',  # Человекочитаемое имя модели в единственном числе
                'verbose_name_plural': 'Публикации',  # Человекочитаемое имя модели во множественном числе
            },
        ),
        # Добавление нового поля 'image' в модель 'post'
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts_images/', verbose_name='Фото'),  # Поле для загрузки изображений постов (может быть пустым)
        ),
        # Изменение поля 'description' в модели 'category'
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(verbose_name='Описание'),  # Поле для описания категории с человекочитаемым именем
        ),
        # Изменение поля 'title' в модели 'post'
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Заголовок'),  # Поле для заголовка поста с максимальной длиной 256 символов
        ),
        # Создание новой модели 'Comment'
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # Автоинкрементируемый ID комментария
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),  # Дата и время добавления комментария
                ('text', models.TextField(verbose_name='Текст')),  # Поле для текста комментария
                # Внешний ключ к модели пользователя (автора комментария)
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария')),
                # Внешний ключ к модели поста, к которому относится комментарий
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'комментарий',  # Человекочитаемое имя модели комментария в единственном числе
                'verbose_name_plural': 'Комментарии',  # Человекочитаемое имя модели комментария во множественном числе
                'ordering': ('created_at',),  # Установка порядка сортировки по дате создания комментария (по возрастанию)
            },
        ),
    ]
