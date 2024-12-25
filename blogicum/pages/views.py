from django.shortcuts import render  # Импортируем функцию render для рендеринга шаблонов
from django.views.generic import TemplateView  # Импортируем класс TemplateView для создания представлений на основе шаблонов


# Определяем класс AboutView, наследующий от TemplateView
class AboutView(TemplateView):
    template_name = 'pages/about.html'  # Указываем путь к шаблону для страницы "О нас"


# Определяем класс RulesView, наследующий от TemplateView
class RulesView(TemplateView):
    template_name = 'pages/rules.html'  # Указываем путь к шаблону для страницы "Правила"


# Обработчик для страницы "Не найдено" (404)
def page_not_found(request, *args, **kwargs):
    return render(request, 'pages/404.html', status=404)  # Рендерим шаблон 404 с соответствующим статусом


# Обработчик для ошибки CSRF (403)
def csrf_failure(request, *args, **kwargs):
    return render(request, 'pages/403csrf.html', status=403)  # Рендерим шаблон 403 с соответствующим статусом


# Обработчик для внутренней ошибки сервера (500)
def internal_error(request, *args, **kwargs):
    return render(request, 'pages/500.html', status=500)  # Рендерим шаблон 500 с соответствующим статусом
