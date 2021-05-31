from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scopes, ArticleScopes


class CheckUniqueMainTag(BaseInlineFormSet):

    def clean(self):
        is_unique_field = True
        for form in self.forms:
            print(form.cleaned_data)
            if form.cleaned_data.get('article') and \
                    form.cleaned_data.get('is_main') and \
                    is_unique_field and \
                    not form.cleaned_data.get('DELETE'):
                is_unique_field = False
            elif not is_unique_field and \
                    form.cleaned_data.get('is_main') and \
                    not form.cleaned_data.get('DELETE'):
                raise ValidationError('Основной тэг может быть только один')
        return super().clean()  # вызываем базовый код переопределяемого метода


class TagsInline(admin.TabularInline):
    model = ArticleScopes
    extra = 1
    formset = CheckUniqueMainTag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        TagsInline,
    ]


@admin.register(Scopes)
class ScopesAdmin(admin.ModelAdmin):
    inlines = [
        TagsInline,
    ]
