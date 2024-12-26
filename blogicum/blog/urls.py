# Импортируем необходимые функции для работы с URL из Django
from django.urls import path

# Импортируем views из текущего приложения
from . import views

# Устанавливаем пространство имен для приложения 'blog'
app_name = 'blog'

# Определяем список маршрутов (URL patterns) для приложения 'blog'
urlpatterns = [
    # Главная страница блога, отображает список постов
    path(
        '',
        views.IndexListView.as_view(),  # Используем представление IndexListView для отображения главной страницы
        name='index'  # Имя маршрута для использования в шаблонах и редиректах
    ),
    # Страница детального просмотра конкретного поста по его ID
    path(
        'posts/<int:post_id>/',
        views.PostDetailView.as_view(),  # Используем представление PostDetailView для отображения поста
        name='post_detail'  # Имя маршрута для доступа к детальному просмотру поста
    ),
    # Страница редактирования поста по его ID
    path(
        'posts/<int:post_id>/edit/',
        views.PostUpdateView.as_view(),  # Используем представление PostUpdateView для редактирования поста
        name='edit_post'  # Имя маршрута для редактирования поста
    ),
    # Страница удаления поста по его ID
    path(
        'posts/<int:post_id>/delete/',
        views.PostDeleteView.as_view(),  # Используем представление PostDeleteView для удаления поста
        name='delete_post'  # Имя маршрута для удаления поста
    ),
    # Страница добавления комментария к посту по его ID
    path(
        'posts/<int:post_id>/comment/',
        views.CommentCreateView.as_view(),  # Используем представление CommentCreateView для добавления комментария
        name='add_comment'  # Имя маршрута для добавления комментария
    ),
    # Страница создания нового поста
    path(
        'posts/create/',
        views.CreatePostView.as_view(),  # Используем представление CreatePostView для создания нового поста
        name='create_post'  # Имя маршрута для создания поста
    ),
    # Страница редактирования комментария по ID поста и ID комментария
    path(
        'posts/<int:post_id>/edit_comment/<int:comment_id>/',
        views.CommentUpdateView.as_view(),  # Используем представление CommentUpdateView для редактирования комментария
        name='edit_comment'  # Имя маршрута для редактирования комментария
    ),
    # Страница удаления комментария по ID поста и ID комментария
    path(
        'posts/<int:post_id>/delete_comment/<int:comment_id>/',
        views.CommentDeleteView.as_view(),  # Используем представление CommentDeleteView для удаления комментария
        name='delete_comment'  # Имя маршрута для удаления комментария
    ),
    # Страница отображения постов в определенной категории по slug категории
    path(
        'category/<slug:category_slug>/',
        views.CategoryDetailView.as_view(),  # Используем представление CategoryDetailView для отображения постов в категории
        name='category_posts'  # Имя маршрута для просмотра постов по категории
    ),
    # Страница профиля пользователя по его имени пользователя (str)
    path(
        'profile/<str:username>/',
        views.ProfileView.as_view(),  # Используем представление ProfileView для отображения профиля пользователя
        name='profile'  # Имя маршрута для доступа к профилю пользователя
    ),
    # Страница редактирования профиля пользователя по его имени пользователя (str)
    path(
        'profile/<str:username>/edit/',
        views.ProfileEditView.as_view(),  # Используем представление ProfileEditView для редактирования профиля пользователя
        name='edit_profile'  # Имя маршрута для редактирования профиля пользователя
    ),
]
