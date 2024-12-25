# Импортируем необходимые классы и функции из Django
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

# Импортируем формы и модели, используемые в приложении
from .forms import CommentForm, PostForm
from .models import Category, Comment, Post

# Константа для определения количества постов на странице
NUMBER_OF_POSTS = 10


# Класс AuthorView проверяет, является ли текущий пользователь автором объекта
class AuthorView(UserPassesTestMixin):
    def test_func(self):
        return self.get_object().author == self.request.user


# Класс PostView для управления созданием и редактированием постов
class PostView(AuthorView, LoginRequiredMixin):
    model = Post  # Указываем модель, с которой будет работать представление
    template_name = 'blog/create.html'  # Шаблон для отображения
    form_class = PostForm  # Форма для создания/редактирования поста
    pk_url_kwarg = 'post_id'  # Имя аргумента URL для получения ID поста

    # Переопределяем метод обработки отсутствия разрешений
    def handle_no_permission(self):
        return redirect('blog:post_detail', self.kwargs[self.pk_url_kwarg])

    # Метод для получения URL при успешном выполнении формы
    def get_success_url(self):
        return reverse('blog:profile', kwargs={'username': self.request.user.username})

    # Метод для передачи контекста в шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm(instance=self.get_object())  # Передаем форму с экземпляром поста
        return context


# Класс CommentView для управления комментариями
class CommentView(LoginRequiredMixin):
    model = Comment  # Указываем модель комментария
    form_class = CommentForm  # Форма для создания комментария
    template_name = 'blog/comment.html'  # Шаблон для отображения комментариев
    pk_url_kwarg = 'comment_id'  # Имя аргумента URL для получения ID комментария

    # Метод для получения URL при успешном выполнении формы
    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'post_id': self.kwargs['post_id']})


# Класс IndexListView для отображения списка постов на главной странице блога
class IndexListView(ListView):
    template_name = 'blog/index.html'  # Шаблон для главной страницы блога
    paginate_by = NUMBER_OF_POSTS  # Количество постов на странице
    queryset = Post.objects.filter_posts_for_publication().count_comments()  # Запрос для получения постов


# Класс PostDetailView для отображения детальной информации о посте
class PostDetailView(ListView):
    template_name = 'blog/detail.html'  # Шаблон для отображения деталей поста
    paginate_by = NUMBER_OF_POSTS  # Количество комментариев на странице

    # Метод для получения объекта поста по его ID
    def get_object(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        if self.request.user == post.author:
            return post  # Если пользователь автор поста, возвращаем его
        return get_object_or_404(Post.objects.filter_posts_for_publication(), pk=self.kwargs['post_id'])

    # Метод для получения комментариев к посту
    def get_queryset(self):
        return self.get_object().comments.all()

    # Метод для передачи контекста в шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()  # Передаем форму для добавления комментария
        context['post'] = self.get_object()  # Передаем объект поста в контекст
        return context


# Класс PostUpdateView для редактирования существующего поста
class PostUpdateView(PostView, UpdateView):
    pass  # Используем функциональность класса PostView


# Класс PostDeleteView для удаления поста
class PostDeleteView(PostView, DeleteView):
    pass  # Используем функциональность класса PostView


# Класс CommentCreateView для создания нового комментария
class CommentCreateView(CommentView, CreateView):
    def form_valid(self, form):
        form.instance.author = self.request.user  # Устанавливаем автора комментария
        form.instance.post = get_object_or_404(
            Post.objects.filter_posts_for_publication(),
            pk=self.kwargs['post_id']
        )  # Устанавливаем пост, к которому относится комментарий
        return super().form_valid(form)  # Вызываем родительский метод при успешной валидации формы


# Класс CreatePostView для создания нового поста
class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post  # Указываем модель поста
    form_class = PostForm  # Форма для создания поста
    template_name = 'blog/create.html'  # Шаблон для создания поста

    def form_valid(self, form):
        form.instance.author = self.request.user  # Устанавливаем автора поста
        return super().form_valid(form)  # Вызываем родительский метод при успешной валидации формы

    def get_success_url(self):
        return reverse('blog:profile', kwargs={'username': self.request.user.username})  # URL перенаправления после создания


# Класс CommentUpdateView для редактирования существующего комментария
class CommentUpdateView(CommentView, AuthorView, UpdateView):
    pass  # Используем функциональность класса CommentView и AuthorView


# Класс CommentDeleteView для удаления комментария
class CommentDeleteView(CommentView, AuthorView, DeleteView):
    pass  # Используем функциональность класса CommentView и AuthorView


# Класс CategoryDetailView для отображения постов в определенной категории
class CategoryDetailView(ListView):
    template_name = 'blog/category.html'  # Шаблон для отображения категории
    paginate_by = NUMBER_OF_POSTS  # Количество постов на странице
    slug_url_kwarg = 'category_slug'  # Имя аргумента URL для получения slug категории

    # Метод для получения объекта категории по slug
    def get_category(self):
        return get_object_or_404(Category, slug=self.kwargs[self.slug_url_kwarg], is_published=True)

    # Метод для передачи контекста в шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.get_category()  # Передаем объект категории в контекст
        return context

    # Метод для получения постов из выбранной категории
    def get_queryset(self):
        return self.get_category().posts.filter_posts_for_publication()  # Возвращаем посты из категории


# Класс ProfileView для отображения профиля пользователя
class ProfileView(ListView):
    template_name = 'blog/profile.html'  # Шаблон для отображения профиля пользователя
    paginate_by = NUMBER_OF_POSTS  # Количество постов на странице
    slug_url_kwarg = 'username'  # Имя аргумента URL для получения имени пользователя (slug)
def get_profile(self):
    # Получаем объект пользователя по имени пользователя (username).
    # Если пользователь не найден, возвращаем 404 ошибку.
    return get_object_or_404(User, username=self.kwargs['username'])

def get_queryset(self):
    # Получаем профиль автора, используя метод get_profile.
    author = self.get_profile()
    
    # Получаем количество постов автора с комментариями.
    posts = author.posts.count_comments()
    
    # Если автор является текущим пользователем, возвращаем все его посты.
    if author == self.request.user:
        return posts
    
    # В противном случае возвращаем только опубликованные посты автора.
    return posts.filter_posts_for_publication()

def get_context_data(self, **kwargs):
    # Получаем контекст из родительского класса.
    context = super().get_context_data(**kwargs)
    
    # Добавляем в контекст профиль пользователя, полученный методом get_profile.
    context['profile'] = self.get_profile()
    
    return context


class ProfileEditView(LoginRequiredMixin, UpdateView):
    # Указываем шаблон для редактирования профиля пользователя.
    template_name = 'blog/user.html'
    
    # Указываем поля, которые могут быть отредактированы в форме.
    fields = ('first_name', 'last_name', 'email')
    
    # Указываем аргумент URL для получения имени пользователя (slug).
    slug_url_kwarg = 'username'
    
    # Указываем поле модели, которое будет использоваться как slug.
    slug_field = 'username'

    def get_object(self, queryset=None):
        # Возвращаем текущего пользователя как объект для редактирования.
        return self.request.user

    def get_success_url(self):
        # Указываем URL для перенаправления после успешного редактирования профиля.
        return reverse('blog:profile',
                       kwargs={'username': self.kwargs[self.slug_url_kwarg]})


