from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField('Scopes', through='ArticleScopes', related_name='scopes')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scopes(models.Model):

    topic = models.CharField(max_length=100, verbose_name='Тэг статьи')
    articles = models.ManyToManyField(Article, through='ArticleScopes', related_name='articles')

    class Meta:
        verbose_name = 'Тэг статьи'
        verbose_name_plural = 'Тэги статей'

    def __str__(self):
        return self.topic


class ArticleScopes(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article')
    scopes = models.ForeignKey(Scopes, on_delete=models.CASCADE, related_name='scope')
    is_main = models.BooleanField(verbose_name='Основной тэг')