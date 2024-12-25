from django.contrib.auth import get_user_model  # Импортируем функцию для получения модели пользователя
from django.contrib.auth.forms import UserCreationForm  # Импортируем форму для создания нового пользователя
from django.urls import reverse_lazy  # Импортируем функцию для получения URL по имени с отложенной оценкой
from django.views.generic import CreateView  # Импортируем базовый класс представления для создания объектов

# Определяем класс представления для регистрации нового пользователя
class UserCreateView(CreateView):
    model = get_user_model()  # Устанавливаем модель, с которой будет работать это представление (модель пользователя)
    template_name = 'registration/registration_form.html'  # Указываем путь к шаблону, который будет использоваться для отображения формы регистрации
    form_class = UserCreationForm  # Указываем форму, которая будет использоваться для создания нового пользователя
    success_url = reverse_lazy('blog:index')  # Указываем URL, на который будет перенаправлен пользователь после успешной регистрации (отложенное разрешение имени URL)
