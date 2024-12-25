# Импорт необходимых модулей и классов из Django
from django import forms  # Импортируем базовый класс для создания форм
from django.utils import timezone  # Импортируем модуль для работы с временными зонами

# Импорт моделей Comment и Post из приложения blog
from blog.models import Comment, Post


# Определение формы для модели Post
class PostForm(forms.ModelForm):

    # Метод инициализации формы
    def init(self, *args, **kwargs):
        # Вызов метода инициализации родительского класса
        super(PostForm, self).init(*args, **kwargs)
        # Установка текущей даты и времени в качестве начального значения для поля pub_date
        self.fields['pub_date'].initial = timezone.now()

    # Вложенный класс Meta для определения метаданных формы
    class Meta:
        model = Post  # Указываем, что форма связана с моделью Post
        exclude = ('author',)  # Исключаем поле author из формы (оно будет автоматически определяться)
        widgets = {
            # Настройка виджета для поля pub_date
            'pub_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',  # Указываем тип поля для выбора даты и времени
                'format': '%Y-%m-%dT%H:%M'  # Формат отображения даты и времени
            }),
        }


# Определение формы для модели Comment
class CommentForm(forms.ModelForm):
    # Вложенный класс Meta для определения метаданных формы
    class Meta:
        model = Comment  # Указываем, что форма связана с моделью Comment
        exclude = ('author', 'post', 'is_published')  # Исключаем поля author, post и is_published из формы
